from lmfit import Model, Parameters, Parameter
import numpy as np
import pandas as pd
from atmosp import calculate as ac
import numpy as np
from scipy.optimize import minimize
from pathlib import Path
import supy as sp
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from platypus.core import *
from platypus.types import *
from platypus.algorithms import *
import random
import pickle
import os
from shutil import copyfile





def cal_des_dta(ta, pa, dta=1.0):
    """Calculate slope of es(Ta), i.e., saturation evaporation pressure `es` as function of air temperature `ta [K]`
    Parameters
    ----------
    ta : numeric
        Air temperature [K]
    pa : numeric
        Air pressure [Pa]
    dta : float, optional
        change in ta for calculating that in es, by default 1.0 K
    """

    des = ac('es', p=pa, T=ta + dta/2) - ac('es', p=pa, T=ta - dta/2)
    des_dta = des/dta
    try:
        # try to pack as Series
        des_dta = pd.Series(des_dta, index=ta.index)
    except AttributeError as ex:
        print(ex, 'cannot pack into pd.Series')
        pass
    return des_dta


def cal_rs_obs(qh, qe, ta, rh, pa,RA):
    """Calculate surface resistance based on observations, notably turbulent fluxes.
    Parameters
    ----------
    qh : numeric
        sensible heat flux [W m-2]
    qe : numeric
        latent heat flux [W m-2]
    ta : numeric
        air temperature [K]
    rh : numeric
        relative humidity [%]
    pa : numeric
        air pressure [Pa]
    Returns
    -------
    numeric
        Surface resistance based on observations [s m-1]
    """

    # surface resistance at water surface [s m-1]
    #rav = 100
    rav=RA

    # psychrometric constant [Pa K-1] as a function of air pressure
    ser_gamma = 0.665e-3 * pa

    # air density [kg m-3]
    val_rho = 1.27

    # heat capacity of air [J kg-1 K-1]
    val_cp = 1005

    # slope of es(Ta) curve at Ta
    ser_des_dTa = cal_des_dta(ta, pa, dta=1.0)
    #
    arr_e = ac('e', p=pa, T=ta, RH=rh)
    arr_es = ac('es', p=pa, T=ta)
    arr_vpd = arr_es-arr_e
    #
    ser_rs_1 = ((ser_des_dTa / ser_gamma)*(qh / qe) - 1) * rav
    ser_rs_2 = (val_rho * val_cp * arr_vpd / (ser_gamma * qe))
    ser_rs = ser_rs_1 + ser_rs_2

    try:
        # try to pack as Series
        ser_rs = pd.Series(ser_rs, index=ta.index)
    except AttributeError as ex:
        print(ex, 'cannot pack into pd.Series')
        pass

    return ser_rs







def cal_gs_obs(qh, qe, ta, rh, pa,RA):
    """Calculate surface conductance based on observations, notably turbulent fluxes.
    Parameters
    ----------
    qh : numeric
        Sensible heat flux [W m-2]
    qe : numeric
        Latent heat flux [W m-2]
    ta : numeric
        Air temperature [K]
    rh : numeric
        Relative humidity [%]
    pa : numeric
        Air pressure [Pa]
    Returns
    -------
    numeric
        Surface conductance based on observations [mm s-1]
    """
    rs_obs = cal_rs_obs(qh, qe, ta, rh, pa,RA)
    gs_obs = 1e3/rs_obs
    return gs_obs


def cal_g_lai(lai, g1, lai_max):
    """Calculate LAI-related correction coefficient for surface conductance.
    Parameters
    ----------
    lai : numeric
        Leaf area index [m2 m-2]
    g1 : numeric
        LAI-related correction parameter [-]
    lai_max : numeric
        Maximum LAI [m2 m-2]
    Returns
    -------
    numeric
        LAI-related correction coefficient [-]
    """
    g_lai = lai/lai_max*g1
    return g_lai


def cal_g_kd(kd, g2, kd_max=1200.):
    """Calculate solar radiation-related correction coefficient for surface conductance.
    Parameters
    ----------
    kd : numeric
        Incoming solar radiation [W m-2]
    g2 : numeric
        Solar radiation-related correction parameter [-]
    kd_max : numeric, optional
        Maximum incoming solar radiation [W m-2], by default 1200.
    Returns
    -------
    numeric
        Solar radiation-related correction coefficient [-]
    """
    g_kd_nom = kd/(g2+kd)
    g_kd_denom = kd_max/(g2+kd_max)
    g_kd = g_kd_nom/g_kd_denom
    return g_kd


def cal_g_dq(dq, g3, g4):
    """Calculate air humidity-related correction coefficient for surface conductance.
    Parameters
    ----------
    dq : numeric
        Specific humidity deficit [k kg-1]
    g3 : numeric
        Specific humidity-related correction parameter [-]
    g4 : numeric
        Specific humidity-related correction parameter [-]
    Returns
    -------
    numeric
        Air humidity-related correction coefficient
    """
    g_dq = g3+(1-g3)*g4**dq
    return g_dq


def cal_g_ta(ta_c, g5, tl=-20., th=55.):
    """Calculate air temperature-related correction coefficient for surface conductance.
    Parameters
    ----------
    ta_c : numeric
        Air temperature [degC]
    g5 : numeric
        Air temperature-related correction parameter
    tl : numeric, optional
        Low temperature limit [degC], by default -10.
    th : numeric, optional
        High temperature limit [degC], by default 55.
    Returns
    -------
    numeric
        Air temperature-related correction coefficient
    """

    tc = (th-g5)/(g5-tl)
    # set a threshold for avoiding numeric difficulty
    #tc = np.min([tc, 20])
    # g_ta = ((ta_c-tl)*(th-ta_c)**tc)/((g5-tl)*(th-g5)**tc)
    g_ta_nom = (ta_c-tl)*np.power((th-ta_c), tc)
    g_ta_denom = (g5-tl)*np.power((th-g5), tc)
    g_ta = g_ta_nom/g_ta_denom

    return g_ta


def cal_g_smd(smd, g6, s1=5.56):
    """Calculate soil moisture-related correction coefficient for surface conductance.
    Parameters
    ----------
    smd : numeric
        Soil moisture deficit [mm].
    g6 : numeric
        Soil moisture-related correction parameter.
    s1 : numeric, optional
        Wilting point (WP=s1/g6, indicated as deficit [mm]) related parameter, by default 5.56
    Returns
    -------
    numeric
        Soil moisture-related correction coefficient
    """
    # Wilting point calculated following SUEWS
    wp = s1/g6
    #wp = 140

    g_smd_nom = 1-np.exp(g6*(smd-wp))
    g_smd_denom = 1-np.exp(g6*(0-wp))
    g_smd = g_smd_nom/g_smd_denom
    return g_smd


def cal_gs_mod(kd, ta_k, rh, pa, smd, lai, g_cst, g_max=30., lai_max=6., s1=5.56):
    """Model surface conductance/resistance using phenology and atmospheric forcing conditions.
    Parameters
    ----------
    kd : numeric
        Incoming solar radiation [W m-2]
    ta_k : numeric
        Air temperature [K]
    rh : numeric
        Relative humidity [%]
    pa : numeric
        Air pressure
    smd : numeric
        Soil moisture deficit [mm]
    lai : numeric
        Leaf area index [m2 m-2]
    g_cst : size-6 array
        Parameters to determine surface conductance/resistance:
        g1 (LAI related), g2 (solar radiation related),
        g3 (humidity related), g4 (humidity related),
        g5 (air temperature related),
        g6 (soil moisture related)
    g_max : numeric, optional
        Maximum surface conductance [mm s-1], by default 30
    lai_max : numeric, optional
        Maximum LAI [m2 m-2], by default 6
    s1 : numeric, optional
        Wilting point (WP=s1/g6, indicated as deficit [mm]) related parameter, by default 5.56
    Returns
    -------
    numeric
        Modelled surface conductance [mm s-1]
    """

    # broadcast g1 – g6
    # print('g_cst', g_cst)
    g1, g2, g3, g4, g5, g6 = g_cst
    # print(g1, g2, g3, g4, g5, g6)
    # lai related
    g_lai = cal_g_lai(lai, g1, lai_max)
    # print('g_lai', g_lai)

    # kdown related
    g_kd = cal_g_kd(kd, g2)
    # print('g_kd', g_kd)
    # dq related
    # ta_k = ta_c+273.15
    dq = ac('qvs', T=ta_k, p=pa)-ac('qv', T=ta_k, p=pa, RH=rh)
    g_dq = cal_g_dq(dq, g3, g4)
    # print('g_dq', g_dq)
    # ta related
    ta_c = ta_k - 273.15
    g_ta = cal_g_ta(ta_c, g5)
    # print('g_ta', g_ta)
    # smd related
    g_smd = cal_g_smd(smd, g6, s1)
    # print('g_smd', g_smd)
    # combine all corrections
    gs_c = g_lai*g_kd*g_dq*g_ta*g_smd
    gs = g_max*gs_c

    return gs,g_lai,g_kd,g_dq,g_ta,g_smd,g_max






def IQR_compare(ob_name,sim_name,df_obs,df_sel_pos,ax):
    y=df_obs[ob_name].groupby(
            [df_obs.index.hour.rename('hr'),
            df_obs.index.minute.rename('min')])
    idx = [pd.datetime(2014, 1, 1, h, m) for h, m in sorted(y.groups.keys())]
    idx = pd.date_range(idx[0], idx[-1], freq='1h')
    
    df_var=df_sel_pos[[sim_name]]
    grp_sdf_var = df_var.groupby(
        [df_var.index.hour.rename('hr'),
        df_var.index.minute.rename('min')])

    idx = [pd.datetime(2014, 1, 1, h, m)
        for h, m in sorted(grp_sdf_var.groups.keys())]
    idx = pd.date_range(idx[0], idx[-1], freq='1h')
    # calculate quartiles
    quar_sel_pos_clm75 = grp_sdf_var.quantile(
        .75).unstack().set_index(idx)
    quar_sel_pos_clm25 = grp_sdf_var.quantile(
        .25).unstack().set_index(idx)
    quar_sel_pos_clm50 = grp_sdf_var.quantile(
        .5).unstack().set_index(idx)
    
    x_data=[i for i in range(0,24)]

    for var in quar_sel_pos_clm75.columns.levels[0]:
        df_x75 = quar_sel_pos_clm75.loc[:, var]
        df_x25 = quar_sel_pos_clm25.loc[:, var]
        df_x50 = quar_sel_pos_clm50.loc[:, var]
        y0 = df_x50
        y1, y2 = df_x75, df_x25

        ax.plot(x_data,y0[0], label='Model',color='b', linewidth=4)
        ax.fill_between(x_data, y1[0], y2[0], alpha=0.3)
        
        
    
    line = ax.lines[0]
    y25=y.quantile(.25)
    y5=y.quantile(.5)
    y75=y.quantile(.75)
    ax.plot(x_data,y5,color='r', linewidth=4,label='Data')
    ax.fill_between(x_data, y25, y75, alpha=0.3)

    ax.set_xlim(0,23)
    
    
def obs_sim(ob_name,sim_name,df_obs,df_sel_pos,ax):
    
        
        df_QE_comp = pd.concat([df_obs, df_sel_pos], axis=1,
                                join='inner').loc[:, [sim_name, ob_name]]
        
        fig_comp_QE = sns.regplot(x='Obs', y='Sim',
                            data=df_QE_comp.rename(
                                columns={ob_name: 'Obs', sim_name: 'Sim'}),
                            fit_reg=True,ax=ax,color='b').figure
        ax.set_ylabel('')    
        ax.set_xlabel('')
        ax.set_title('')

        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()
        #ax.set_aspect(abs(x1 - x0) / abs(y1 - y0))
        sns.lineplot(x=[x0,x1],y=[x0,x1],ax=ax,color='k',label='1-1',linewidth=2)
        ax.lines[1].set_linestyle("--")

def func_parse_date(year, doy, hour, min):
        dt = pd.to_datetime(' '.join(
            [str(k) for k in [year, doy, hour, min]]),
            format='%Y %j %H %M')
        return dt

def read_forcing(name,year):
    copyfile("./runs/data/"+name+"_"+str(year)+"_data_60.txt", "runs/run/input/Kc_2012_data_60.txt")
    #os.rename("./data/"+obs_n+"_"+str(year)+"_data_60.txt", "runs/run/input/Kc_2012_data_60.txt")
    df_forcing=pd.read_csv('runs/run'+'/Input/'+'kc'+'_'+'2012'+'_data_60.txt',sep=' ',
                                    parse_dates={'datetime': [0, 1, 2, 3]},
                                    keep_date_col=True,
                                    date_parser=func_parse_date)

    df_forcing= df_forcing.set_index('datetime')
    return df_forcing


def generate_array_dif(attrs_site, attr,level):
    dar = [0.75,0.5,.25]
    dar[level] = attrs_site[attr].values[0]
    return dar


def generate_array_same(attrs_site, attr):
    a = attrs_site[attr].values[0]
    return [a, a, a]


def modify_attr(df_state_init, name):
    all_sites_info =  pd.read_csv('site_info.csv')
    site_info=all_sites_info[all_sites_info['Site Id'] == name]
    df = pd.DataFrame(
        {'Site': [name],
        'Latitude': [site_info['Latitude (degrees)']],
        'Longitude': [site_info['Longitude (degrees)']]})

    all_attrs = pd.read_csv('all_attrs.csv')
    attrs_site = all_attrs[all_attrs.site == name]
    df_state_init.loc[:, 'emissionsmethod'] = 0
    df_state_init.loc[:,'roughlenheatmethod']=1

    if attrs_site.land.values[0] == 'DecTr':
        ar = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
        level = 1
        df_state_init.albmin_dectr=attrs_site['albmin'].values[0]
        df_state_init.albmax_dectr=attrs_site['albmax'].values[0]
        df_state_init.albdectr_id=df_state_init.albmin_dectr
        df_state_init.loc[:, 'dectreeh'] = attrs_site.height.values[0]

    elif attrs_site.land.values[0] == 'EveTr':
        ar = [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]
        level = 0
        df_state_init.albmin_evetr=attrs_site['albmin'].values[0]
        df_state_init.albmax_evetr=attrs_site['albmax'].values[0]
        df_state_init.albevetr_id=df_state_init.albmin_evetr
        df_state_init.loc[:, 'evetreeh'] = attrs_site.height.values[0]

    elif attrs_site.land.values[0] == 'Grass':
        ar = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
        level = 2
        df_state_init.albmin_grass=attrs_site['albmin'].values[0]
        df_state_init.albmax_grass=attrs_site['albmax'].values[0]
        df_state_init.loc[:,'roughlenmommethod']=1
        df_state_init.albgrass_id=df_state_init.albmin_grass
        df_state_init.loc[:,'z0m_in']=attrs_site.height.values[0]*.1
        df_state_init.loc[:,'zdm_in']=attrs_site.height.values[0]*.7

    else:
        print('The land cover type is not found! using the default one')

    df_state_init.loc[:, 'sfr'] = ar
    df_state_init.loc[:, 'lat'] = df.Latitude.values[0].values[0]
    df_state_init.loc[:, 'lng'] = df.Longitude.values[0].values[0]
    df_state_init.loc[:, 'z'] = attrs_site.meas.values[0]
    df_state_init.loc[:, 'laimin'] = generate_array_dif(attrs_site, 'laimin',level)
    df_state_init.loc[:, 'laimax'] = generate_array_dif(attrs_site, 'laimax',level)
    df_state_init.loc[:, 'gddfull'] = generate_array_same(attrs_site, 'gddfull')
    df_state_init.loc[:, 'sddfull'] = generate_array_same(attrs_site, 'sddfull')
    df_state_init.loc[:, 'basete'] = generate_array_same(attrs_site, 'basete')
    df_state_init.loc[:, 'baset'] = generate_array_same(attrs_site, 'baset')
    df_state_init.lai_id = df_state_init.loc[:, 'laimin']
    
    

    return df_state_init,level

def modify_attr_2(df_state_init,g_max,s1):
    df_state_init.maxconductance=g_max
    df_state_init.s1=s1
    return df_state_init


def gs_plot_test(g1,g2,g3,g4,g5,g6,g_max,s1,name,year,alpha=1,helen=0):

    path_runcontrol = Path('runs/run'+'/') / 'RunControl.nml'
    df_state_init = sp.init_supy(path_runcontrol)
    df_state_init,level=modify_attr(df_state_init,name)
    grid = df_state_init.index[0]
    df_forcing_run = sp.load_forcing_grid(path_runcontrol, grid)


    df_state_init.g1=g1*alpha
    df_state_init.g2=g2
    df_state_init.g3=g3
    df_state_init.g4=g4
    df_state_init.g5=g5
    df_state_init.g6=g6
    f_state_init=modify_attr_2(df_state_init,g_max,s1)
    df_output, df_state_final = sp.run_supy(df_forcing_run, df_state_init, save_state=False)


    df_obs=pd.read_csv('runs/run'+'/Input/'+'kc'+'_2012_data_60.txt',sep=' ',
                                    parse_dates={'datetime': [0, 1, 2, 3]},
                                    keep_date_col=True,
                                    date_parser=func_parse_date)

    df_obs= df_obs.set_index('datetime')

    fig,axs=plt.subplots(4,1,figsize=(8,15))
    plt.subplots_adjust(hspace=.8)
    plt.rc('font', size=15)

    ax=axs[0]
    df_obs_temp=df_obs.replace(-999,np.nan)
    
    df=df_output.SUEWS.loc[grid,:]
    df=df.resample('1h',closed='left',label='right').mean()
    
    IQR_compare('qe','QE',df_obs_temp,df,ax)
    ax.legend()
    ax.set_title('QE (test data set-fitted g1-g6)')
    ax.set_ylabel('QE (W m$^{-2}$)')
    ax.set_xlabel('Time (UTC)')


    df=df_output.SUEWS.loc[grid,:]
    df=df.resample('1h',closed='left',label='right').mean()
    df_temp=df_obs_temp[df_obs_temp.qe<700]
    
    plt.rc('font', size=15)

    data_for_plot={'IQR':{'obs':df_obs_temp,'model':df}}
    data_for_plot['obs_sim']={'obs':df_temp,'model':df.loc[df_temp.index,:]}

    if helen==0:
        with open('outputs/surface_conductance/'+name+'-'+str(year)+'.pkl','wb') as f:
            pickle.dump(data_for_plot, f)
    elif helen==1:
        with open('outputs/surface_conductance/'+name+'-'+str(year)+'-Helen.pkl','wb') as f:
            pickle.dump(data_for_plot, f)

    ax=axs[1]
    obs_sim('qe','QE',df_temp,df.loc[df_temp.index,:],ax)

    ax.set_ylabel('Model')
    ax.set_xlabel('Obs')
    ax.set_title('QE-test data-all season-MAE='+str(np.round(np.mean(abs(df.loc[df_temp.index,:].QE-df_temp.qe)),2)))
    

    ax=axs[2]
    df_output.SUEWS.QE.loc[grid,:].resample('1h',closed='left',label='right').mean().plot(ax=ax,label='model')
    ax.legend()
    ax=axs[3]
    df_obs[df_obs.qe>0].qe.plot(ax=ax,label='obs')
    ax.legend()
    
  