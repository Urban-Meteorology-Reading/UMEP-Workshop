 .. _CalcParam:
 
Preparing to Calculate your own parameters
------------------------------------------

**This will take:** ~  XX minutes (note there are 5 topics)

**Prior to this activity**

- `Install and run notebooks Jupyter Notebooks <https://umep-workshop.readthedocs.io/en/latest/Jupyter/JN1.html>`_
- Basics for running SuPy

**Activity**

In these tutorials you can calculate various SUEWS parameters before running the model for the specific site and vegetation type. The parameters discussed here are: 
 
 - LAI 
 - albedo
 - surface roughness length and displacement height
 - surface conductances. 

The Figures below shows the order in which parameters should be derived:

These tutorials are based on the calculations undertaken in Omidvar et al. (2020).

.. _fig_params:

.. figure:: SUEWS_Parameters.png
   :alt: params.


In this example we use meteorological observations from AmeriFlux (https://ameriflux.lbl.gov/) network. The data required are air temperature, incoming shortwave radiation, upwelling shortwave radiation, station pressure, relative humidity, wind speed, precipitation, net all-wave radiation, sensible heat flux and latent heat flux, ideally storage heat flux (os soil heat flux if a simple surface), and the momentum flux. Wind direction is also very helpful.

**Reference**

- Omidvar H, T Sun, S Grimmond, D Bilesbach, A Black, J Chen, Z Duan, Z Gao, H Iwata, JP McFadden. Surface [Urban] Energy and Water Balance Scheme in non-urban areas: developments, parameters and performance, (in review)


Steps to using these notebooks:
==============================

Terms in the notebooks are defined `here <CalcBG>`


1-  Download the following files and codes (all the files are available `here <https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/tree/master/source/Parameters/files>`_. You need to unzip the folders):

 -  `data <https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/blob/master/source/Parameters/files/data.zip>`_ : data that are necessary to calculate parameters (put them in the same directory as notebooks).
 - Utility functions: these are the utility functions that are called in notebooks. Put them in the same directory as notebooks. 
 
   - `Albedo and LAI utility <https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/blob/master/source/Parameters/files/alb_LAI_util.py>`_
   
   - `Conductance utility <https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/blob/master/source/Parameters/files/gs_util.py>`_
   
   - `Roughness utility <https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/blob/master/source/Parameters/files/z0_util.py>`_
 
 - CSV files containing site information and parameters. Put them in the same directory as the notebook:
  
   - `site information <https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/blob/master/source/Parameters/files/site_info.csv>`_
   - `site parameters <https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/blob/master/source/Parameters/files/all_attrs.csv>`_ . You can then change these parameters if you like to tune the sites.
   
 - `runs <https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/blob/master/source/Parameters/files/runs.zip>`_ folder contains SUEWS files which are used by SuPy
 
 - `figs <https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/blob/master/source/Parameters/files/figs.zip>`_ folder to write the figure into (it can be empty initially). Put them in the same directory as the notebook.
 
 - `outputs <https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/blob/master/source/Parameters/files/outputs.zip>`_ folder to write down pickle files. The structure of the file should be as it is in the link, but the folders (LAI, albedo etc.) can be empty initially. Put them in the same directory as notebook.
 
 **Note**: after downloading the above files an folders, the structure of the directory where you are running the notebooks should be as same as `here <https://github.com/hamidrezaomidvar/SUEWS_parameters_docs/tree/master/docs/source/steps>`_.
 
2- Download `this <https://github.com/Urban-Meteorology-Reading/SUEWS_parameters/blob/master/environment.yml>`_ environment file. Go to the directory where the file is. Type 

.. code::

      conda env create -f environment.yml

After all the packages are installed, type 

.. code::

      conda activate SUEWS_parameters


This activates the the created environment. In the same environment, open Jupyter notebook.
 
3- Then you can run each notebook in the same order as the tutorials taht follow. `

