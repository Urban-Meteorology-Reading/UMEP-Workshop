 .. _CalcParam:
 
Calculating your own parameters
--------------------------------
In these tutorials you can calculate various SUEWS parameters before running the model for the specific site and vegetation type. The parameters discussed here are: 
 
 - LAI 
 - albedo
 - surface roughness length and displacement height
 - surface conductances. 

The Figures below shows the order in which parameters should be derived:

These tutorials are based on the calcuations undertaken in Omidvar et al. (2020).

.. _fig_params:

.. figure:: SUEWS_Parameters.png
   :alt: params.


In this example we use meteorological observations from AmeriFlux (https://ameriflux.lbl.gov/) network. The data required are air temperature, incoming shortwave radiation, upwelling shortwave radiation, station pressure, relative humidity, wind speed, precipitation, net all-wave radiation, sensible heat flux and latent heat flux, ideally storage heat flux (os soil heat flux if a simple surface), and the momentum flux. Wind direction is also very helpful.

**Reference**

- Omidvar H, T Sun, S Grimmond, D Bilesbach, A Black, J Chen, Z Duan, Z Gao, H Iwata, JP McFadden. Surface [Urban] Energy and Water Balance Scheme in non-urban areas: developments, parameters and performance, (in review)

Leaf Area Index
===============

- `LAI <https://suews-parameters-docs.readthedocs.io/en/latest/steps/LAI.html>`_

Albedo
======
- `Albedo <https://suews-parameters-docs.readthedocs.io/en/latest/steps/albedo.html>`_


Roughmess Parameters
=====================

- `Roughness related  <https://suews-parameters-docs.readthedocs.io/en/latest/steps/roughness.html>`_

-  `SuPy- roughness <https://suews-parameters-docs.readthedocs.io/en/latest/steps/roughness-SuPy.html>`_ 


Surface Conductance Parameters
==============================

-  `Surface conductance <https://suews-parameters-docs.readthedocs.io/en/latest/steps/conductance.html>`_
