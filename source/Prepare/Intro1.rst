Introduction
--------------------

- Welcome to the `urbisphere <http://urbisphere.eu/>`_ 2020 Modelling Workshop

Given this is our first *urbisphere* Modelling workshop our main goal is to get everyone familiar with several modelling tools that already exist.

As this is an online workshop (rather than being at University of Reading as planned) we will meet twice a day via TEAMS formally but we will keep the TEAMS channels open throughout each session so you can ask questions of each other and the people ready to provide help.

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

- **Python** - the QGIS addins are written in Python as is SuPY. This has the advantage of haveing a large number of code libraries for graphics, statistics, *etc*
- **Fortran** - SUEWS is written in this. This has the advantage of being more computationally efficient for processing larger volumes of data. It is also the language that many weather and climate models are written in.

SUEWS coupling

- SUEWS is in UMEP, SuPY, and coupled to WRF, as well as being a standalone code.
- SUEWS can be forced (i.e. the meteorological data that is needed to run the model) in the following way:
  - Observations
  - ERA5 data (or other renalysis data)
  - WRF (or other weather/cliamte model that it is coupled to)
  - Climate projections

SUEWS requires the urban form and function to be characterised

- form (e.g. land cover, building heights)
- function (e.g. population density, energy use diurnal pattern for work days and non-work days, irrigation behaviour, snow clearing behaviour)

These characteristics need to be provided for each grid (or spatial unit) to be modelled. A spatial unit does not need to be a rectangular grid (if not within a Weather/cliamte model), but can be for example census data or other governance related spatial units. 

The Background <Background> page provides some links to background reading.


People
~~~~~~

Hosted By 

- Sue Grimmond 
- Fredrick Lindberg (lead UMEP developer)
- Ting Sun (lead SuPY developer and current lead on SUEWS)

Contributors to the workshop

- Kit Benjamin (tester of all the Worskhop activties)
- Nils Wallenberg 
- Oskar Bäcklin
- Vicky Lucas (and others) at IEA, University of Reading (Videos)

Ackowledgments

- ERC Synergy urbisphere
- Newton Fund/Met Office CSSP China Project Viewpoint
- NERC

Workshop History

- 8-10 July 2020 - Version 1 of the workshop. Given to urbisphere. 'Program <Prog1>'

Feedback
~~~~~~~~

- Problems with the Manuals (Workshop, UMEP, SUEWS, SuPY) - please complete the GitHib input so it get fixed for others in the group 
- What other topcis would you like to see covered? Please add to GitHub or contact Sue





