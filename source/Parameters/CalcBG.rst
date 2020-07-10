.. _CalcBG:



Background
~~~~~~~~~~

.. list-table:: Terms Used in LAI
   :header-rows: 1
   :widths: 40, 70, 30, 30
   
   * - Name
     - Definition  
     - SupY
     - SUEWS 
   * -  `BaseTe`
     -  Base temperature for initiating sensence degree days (SDD) for leaf off. [°C]
     - 'SuPy <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html?highlight=baseTe#cmdoption-arg-BaseTe>`__,
     - `SUEWS
   * -  `BaseT 
     -
     -  `SUEWS <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html?highlight=baseTe#cmdoption-arg-BaseT>`__
   * -  `LAI_max <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html#cmdoption-arg-LAIMax>`__
     - full leaf-on summertime value
     -
   * -  `LAI_min <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html#cmdoption-arg-LAIMin>`__
     - leaf-off wintertime value
     -
     -
   * -  `GDD <https://suews.readthedocs.io/en/latest/notation.html?highlight=GDD#term-GDD>`__
     - Growing degree days
     -
     -
   * -  `SDD <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=SDD#cmdoption-arg-sdd-dectr>`__
     - Senescence degree days
     - 
     -
 
.. list-table:: Terms Used in All/Multiple
   :header-rows: 1
   :widths: 40, 70, 30
 
 
   * -  `DecTr <https://suews-docs.readthedocs.io/en/latest/notation.html?highlight=DecTr#term-DecTr>`__
     - Deciduous trees and shrubs
     - 
   * - `EveTr <https://suews-docs.readthedocs.io/en/latest/notation.html?highlight=DecTr#term-EveTr>`__
     - Evergreen trees and shrubs
     - 
   * - `Grass <https://suews-docs.readthedocs.io/en/latest/notation.html?highlight=DecTr#term-Grass>`__
     - Grass surface
     - 
    * - `SWIN <https://suews-docs.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html?highlight=Kdown#cmdoption-arg-kdown>`__
     - Incoming shortwave radiation (Kdown) [W m-2]
     - 
   * - `SWOUT <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=Kup#cmdoption-arg-kup>`__
     - Outgoing shortwave radiation (Kup) [W m-2]
     - 
     
  
.. list-table:: Terms Used in Albedo
   :header-rows: 1
   :widths: 40, 70, 30
     
   * - :math:`\alpha_LAImax`
     - Albedo of vegetation when LAI is equal to LAI_max
     - 
   * - \alpha_LAImin
     - Albedo of vegetation when LAI is equal to LAI_min
     - 
     
 .. list-table:: Terms Used in Conductances
   :header-rows: 1
   :widths: 40, 70, 30    
  
   * - `SMD <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=SMD#cmdoption-arg-smd>`__
     - Soil moisture deficit for bare soil surface [mm]
     - 
     
 .. list-table:: Terms Used in Roughness
   :header-rows: 1
   :widths: 40, 70, 30        
     
   * - :math:`z_0`__
     - Roughness length for momentum [m] '<https://supy.readthedocs.io/en/latest/data-structure/df_state.html?highlight=z0#cmdoption-arg-z0m-in`
     - 
   * - `d <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=displacement%20height#cmdoption-arg-zdm>`__
     - Zero-plane displacement height [m]
     - Roughness
   * - `Obukhov length <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=Obukhov%20Length%20#cmdoption-arg-lob>`__
     - Stability parameter
     - Roughness
   * - :math:`USTAR`
     - Friction velocity
     - 
