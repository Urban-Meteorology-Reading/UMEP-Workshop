.. _CalcBG:



Background
~~~~~~~~~~

For Leaf Area Index

.. list-table:: Terms Used in LAI
   :header-rows: 1
   :widths: 40, 70
   
   * - Name
     - Definition 
   * -  :math:`BaseTe`,`SuPy <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html?highlight=baseTe#cmdoption-arg-BaseTe>`__
     -  Base temperature for initiating sensence degree days (SDD) for leaf off. [°C]
   * -  :math:`BaseT1`,  `SUEWS <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html?highlight=baseTe#cmdoption-arg-BaseT>`__ 
     -  Base Temperature for initiating growing degree days (GDD) for leaf growth. [°C] 
   * -  math:`LAI_max`  `SUEWS<https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html#cmdoption-arg-LAIMax>`__
      - maximum LAI
   * -  LAI_min, `SUEWS <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html#cmdoption-arg-LAIMin>`__
     -  leaf-off wintertime value  
   * -  `GDD <https://suews.readthedocs.io/en/latest/notation.html?highlight=GDD#term-GDD>`__
     -  Growing degree days
   * -  SDD, `SuPy <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=SDD#cmdoption-arg-sdd-dectr>`__
     -  Senescence degree days
    
 
 
All or Multiple
 
.. list-table:: Terms Used in All/Multiple
   :header-rows: 1
   :widths: 40, 70
  
   * -  DecTr, `SUEWS <https://suews-docs.readthedocs.io/en/latest/notation.html?highlight=DecTr#term-DecTr>`__
     -  Deciduous trees and shrubs
   * -  EveTr , `SUEWS <https://suews-docs.readthedocs.io/en/latest/notation.html?highlight=DecTr#term-EveTr>`__
     -  Evergreen trees and shrubw
   * -  Grass, `SUEWS<https://suews-docs.readthedocs.io/en/latest/notation.html?highlight=DecTr#term-Grass>`__
     -  Grass surface 
   * -  SWIN, `SUEWS <https://suews-docs.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html?highlight=Kdown#cmdoption-arg-kdown>`__
     -  Incoming shortwave radiation (Kdown) [W m-2]
   * -  `SWOUT <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=Kup#cmdoption-arg-kup>`__
     -  Outgoing shortwave radiation (Kup) [W m-2]

     
   
Albedo
  
.. list-table:: Terms Used in Albedo
   :header-rows: 1
   :widths: 40, 70
     
   * - :math:`alpha_LAImax`
     - Albedo of vegetation when LAI is equal to LAI_max
   * - \alpha_LAImin
     - Albedo of vegetation when LAI is equal to LAI_min
     
Conductances

.. list-table:: Terms Used in Conductances
   :header-rows: 1
   :widths: 40, 70 
  
   * - SMD 'SuPy Y<https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=SMD#cmdoption-arg-smd>`__
     - Soil moisture deficit for bare soil surface [mm]
    
     

Roughness

.. list-table:: Terms Used in Roughness
   :header-rows: 1
   :widths: 40, 70, 30        
     
   * - :math:`z_0`, `SuPy <https://supy.readthedocs.io/en/latest/data-structure/df_state.html?highlight=z0#cmdoption-arg-z0m-in`
     - Roughness length for momentum [m]
   * - d, 'SuPy <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=displacement%20height#cmdoption-arg-zdm>`__
     - Zero-plane displacement height [m]
   * - Obukhov length, `SuPy <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=Obukhov%20Length%20#cmdoption-arg-lob>`__
     - Stability parameter
   * - :math:`USTAR`
     - Friction velocity

