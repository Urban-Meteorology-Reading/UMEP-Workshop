.. _Consider1:

Model Inputs
------------

- `Files required to run SUEWS <https://suews.readthedocs.io/en/latest/input_files/input_files.html>`_
- The data are needed for every grid (can be any shape) area in the doamin to be modelled.

Forcing data
============

- `Meteorological variables needed <https://suews.readthedocs.io/en/latest/input_files/met_input.html>`_

Data Sources
~~~~~~~~~~~~~

- Observations
- Climate data e.g. ERA5, projections
- Coupled Model e.g. WRF

Height consideration of the forcing data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Height summary <Height>`


Site Information
================



- `Site parameters <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_SiteInfo.html>`_

 .. list-table:: Site parameters
   :header-rows: 1
   :widths: 40, 70, 50

   * - Name
     - Type
     - How to determine
   * - SUEWS_AnthropogenicEmission.txt 
     - `Function <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_AnthropogenicEmission.html>`_
     - :ref:`T1-QF`
   * - SUEWS_BiogenCO2.txt 
     - `Function, Biophysical <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_BiogenCO2.html>`_
     - :ref:`T1-w`
   * - SUEWS_Conductance.txt
     - `Biophysical <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_Conductance.html>`_
     - :ref:`T1-gs`_
   * - SUEWS_Irrigation.txt
     - `Function <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_Irrigation.html>`_
     - :ref:`T1-w`,  :ref:`T1-f`
   * - SUEWS_NonVeg.txt
     - `Materials <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_NonVeg.html>`_
     -  :ref:`T1-m`
   * - SUEWS_OHMCoefficients.txt
     - `Materials <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_OHMCoefficients.html>`_
     - :ref:`T1-m`
   * - SUEWS_Profiles.txt
     - `Function <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_Profiles.html>`_
     - :ref:`T1-f`
   * - SUEWS_SiteSelect.txt
     - `all <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_SiteSelect.html>`_
     - :ref:`T1-a`
   * - SUEWS_Snow.txt
     - `Function,materials <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_Snow.html>`_
     -  :ref:`T1-w`,  :ref:`T1-f`
   * - SUEWS_Soil.txt
     - `Materials <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_Soil.html>`_
     -  :ref:`T1-w`
   * - SUEWS_Veg.txt
     - `Materials <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_Veg.html>`_
     -  :ref:`T1-a`
   * - SUEWS_Water.txt
     - `Materials <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_Water.html>`_
     -  :ref:`T1-m`
   * - SUEWS_WithinGridWaterDist.txt
     - `Function <https://suews.readthedocs.io/en/latest/input_files/SUEWS_SiteInfo/SUEWS_WithinGridWaterDist.html>`_
     -  :ref:`T1-w`




Initial Conditions
==================

- `Initial conditions <https://suews.readthedocs.io/en/latest/input_files/Initial_Conditions/Initial_Conditions.html>`

- Conducting a model spinup for a number of years allows for the influence of the conditions selected to begin with being no longer critical.
- Key ones to consider 
  
   - leaf area index (leaf-on, leaf-off)
   - soil moisture state
   
 - less critical
  
   - surface state (as long as modelling for a long period
   

