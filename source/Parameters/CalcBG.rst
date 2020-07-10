.. _CalcBG:


 .. list-table:: Terms Used
   :header-rows: 1
   :widths: 40, 70, 30

Background
~~~~~~~~~~

 .. list-table:: Terms Used
   :header-rows: 1
   :widths: 40, 70, 30
   
   * - Name
     - Definition  
     - Task
   * -  `BaseTe <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html?highlight=baseTe#cmdoption-arg-BaseTe>`__
     - Base temperature for initiating sensesance degree days (SDD) for leaf off. [°C]
     - LAI
   * -  `BaseT <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html?highlight=baseTe#cmdoption-arg-BaseT>`__
     - Base Temperature for initiating growing degree days (GDD) for leaf growth. [°C]
     - LAI
   * -  `LAI_max <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html#cmdoption-arg-LAIMax>`__
     - full leaf-on summertime value
     - LAI
   * -  `LAI_min <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html#cmdoption-arg-LAIMin>`__
     - leaf-off wintertime value
     - LAI
   * -  `GDD <https://suews.readthedocs.io/en/latest/notation.html?highlight=GDD#term-GDD>`__
     - Growing degree days
     - LAI
   * -  `SDD <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=SDD#cmdoption-arg-sdd-dectr>`__
     - Senescence degree days
     - LAI
   * -  `DecTr <https://suews-docs.readthedocs.io/en/latest/notation.html?highlight=DecTr#term-DecTr>`__
     - Deciduous trees and shrubs
     - All
   * - `EveTr <https://suews-docs.readthedocs.io/en/latest/notation.html?highlight=DecTr#term-EveTr>`__
     - Evergreen trees and shrubs
     - All
   * - `Grass <https://suews-docs.readthedocs.io/en/latest/notation.html?highlight=DecTr#term-Grass>`__
     - Grass surface
     - All
   * - :math:`\alpha_LAImax`
     - Albedo of vegetation when LAI is equal to LAI_max
     - Albedo
   * - \alpha_LAImin
     - Albedo of vegetation when LAI is equal to LAI_min
     - Albedo
   * - `SWIN <https://suews-docs.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/Input_Options.html?highlight=Kdown#cmdoption-arg-kdown>`__
     - Incoming shortwave radiation (Kdown) [W m-2]
     - Conductances
   * - `SWOUT <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=Kup#cmdoption-arg-kup>`__
     - Outgoing shortwave radiation (Kup) [W m-2]
     - Conductances
   * - `SMD <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=SMD#cmdoption-arg-smd>`__
     - Soil moisture deficit for bare soil surface [mm]
     - Conductances
   * - :math: `Z0 <https://supy.readthedocs.io/en/latest/data-structure/df_state.html?highlight=z0#cmdoption-arg-z0m-in>`__
     - Roughness length for momentum [m]
     - Roughness
   * - `d <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=displacement%20height#cmdoption-arg-zdm>`__
     - Zero-plane displacement height [m]
     - Roughness
   * - `Obukhov length <https://supy.readthedocs.io/en/latest/data-structure/df_output.html?highlight=Obukhov%20Length%20#cmdoption-arg-lob>`__
     - Stability parameter
     - Roughness
   * - :math: `USTAR`__
     - Friction velocity
     - Roughness
