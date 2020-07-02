.. _Intro1:

Introduction
--------------------


Topics to be Covered
~~~~~~~~~~~~~~~~~~~~~

The three main software tools that will be used in the workshop are:

- **UMEP** - this is an urban climate services tool that has a large number of tools and models. It is an application add-on to QGIS
- **SUEWS** - this is an energy, water and carbon balance model that can be used to simulate urban and non-urban areas. This is both a standalone model but also within UMEP. The UMEP environment is a good place to start to use SUEWS
- **SuPY** - this is a Python interface to SUEWS which allows SUEWS to be rapidly used to address research questions. It also used to couple SUEWS to other programs (e.g. DASH. STEBBS, EnergyPlus)

Two user environments that we will use are:

- **QGIS** -  a geographic information system for analysing spatial data.
- **Jupyter Notebooks** - this allows for a project to be developed with comments, code, graphics etc that contains all of the analyses of a project.

There are two main programming languages involved in the software

- **Python** - the QGIS add-ins are written in Python as is SuPY. This has the advantage of having a large number of code libraries for graphics, statistics, *etc*
- **Fortran** - SUEWS is written in this. This has the advantage of being more computationally efficient for processing larger volumes of data. It is also the language that many weather and climate models are written in.

SUEWS coupling

- SUEWS is in UMEP, SuPY, and coupled to WRF, as well as being a standalone code.
- SUEWS can be forced (i.e. the meteorological data that is needed to run the model) in the following way:

  - Observations
  - ERA5 data (or other reanalysis data)
  - WRF (or other weather/climate model that it is coupled to)
  - Climate projections

SUEWS requires the urban form and function to be characterised

- form (e.g. land cover, building heights)
- function (e.g. population density, energy use diurnal pattern for work days and non-work days, irrigation behaviour, snow clearing behaviour)

These characteristics need to be provided for each grid (or spatial unit) to be modelled. A spatial unit does not need to be a rectangular grid (if not within a Weather/cliamte model), but can be for example census data or other governance related spatial units.

Some `background <Background>` reading for the Workshop will help you understand the models and provide details options that will be useful later.


People
~~~~~~

Hosted By

- Sue Grimmond
- Fredrick Lindberg (lead UMEP developer)
- Ting Sun (lead SuPy developer and current lead on SUEWS)

Contributors to the workshop

- Kit Benjamin (tester of all the Workshop activities)
- Nils Wallenberg (GIS and UMEP assistant during the Workshop)
- Oskar Bäcklin (GIS and UMEP assistant during the Workshop)
- Vicky Lucas (and others) at IEA, University of Reading (Videos)

Acknowledgements
~~~~~~~~~~~~~~~~

- ERC Synergy urbisphere
- Newton Fund/Met Office CSSP China
- NERC
- FORMAS: Swedish Research Council for Sustainable Development

A large number of individuals have worked on the development of the software (SUEWS, UMEP, SuPy) and the collection of the various datasets that are used in the tutorials. These are all gratefully acknowledged.

We thank the following organisations whose **data** are used, including:

- AmeriFlux
- ECMWF ERA5
- LUMA

Feedback
~~~~~~~~

- If you find problems with the Manuals (Workshop, UMEP, SUEWS, SuPy) please raise a GitHib issue so it can be fixed for others in the group (i.e. saving everyone time)
- Do you have suggestions of other tutorials?
- What other topics would you like to see covered? Please add to GitHub or contact Sue





