.. _Ht1:

Heights that need to be considered in SUEWS
--------------------------------------------


.. list-table:: Heights important for SUEWS
   :header-rows: 1
   :widths: 40, 7, 50, 50

   * - Name
     - Symbol
     - Definition
     - Comment
   * - Height of Forcing data for Local scale SUEWS application
     -
     - Height above ground level
     - This should be above the RSL
   * - Roughness SubLayer
     - RSL
     - Layer that is directly influenced by individual roughness elements
     - includes the UCL but is below the ISL
   * - Urban canopy layer
     - UCL
     - Height of the roughness elements (RE)
     - Building, trees and other RE
   * - Inertial sub layer or Constant flux layer
     - ISL
     - The layer where the influence of the individual RE are blended
     -
   * - Height above ground level
     - agl
     -
     - height of RE, height of ISL, mid-height of building
   * - Height above sea level
     - asl
     - Altitude of land surface
     - can be different between model grids (e.g. ERA5 grid and SUEWS grids)

.. _fig_height:

.. figure:: heights.png
   :alt: Heights.

   Critical heights that need to be considered: rural ERA5 surface-level data are “lifted” to the SUEWS forcing height z_a after altitude differences (above sea level, asl) are accounted for the forcing height needs to consider the urban canopy height  (:math:`z_H`) to ensure that is within the inertial sub-layer and above the roughness sub-layer (RSL). The SUEWS RSL module is used to determine the variables (air temperature :math:`T`, specific humidity :math:`q` and wind speed :math:`U`) at the height desired within the RSL for an application. Figure not to scale.