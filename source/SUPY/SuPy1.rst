.. _SuPy1:

Preparation for using SuPy
--------------------------

**This will take:** ~30 mins

Prior to this activity
~~~~~~~~~~~~~~~~~~~~~~

- Installation (M)

1. Windows+QGIS: ``osgeo``-based approach

   - Follow `this <QGIS1>` to install QGIS

   - In your start menu in Windows, locate **OSGeo4W Shell** and open it. If you automatically do not have administrative rights you need to right-click on **OSGeo4W Shell**, *Open file Location*, Right-click on **OSGeo4W Shell** again and choose *Run as Administrator*; type the following two commands:

   .. code-block:: SHELL

      py3_env
      pip install notebook

   - To start Jupyter Notebook type:

   .. code-block:: SHELL

      jupyter notebook

2. General (all platforms): `Anaconda-based approach <https://docs.anaconda.com/anaconda/install/>`_

3. Jupyter Notebook Extension: `Installation <https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html>`_

- `Introduction to Jupyter Notebooks (BLM course material) <https://blm.readthedocs.io/en/latest/JupyterNotebook.html>`_

- `Jupyter Notebook Cheatsheet <https://cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/>`_

.. note::
   If you use Anaconda for Python, better to choose `conda-forge` channel for package installation due to better compatibility with various scientific libraries.


Activity
~~~~~~~~

**Jupyter Notebooks: setting up your research-oriented coding workshop**



- Basic operations (L)
   - command/edit mode
   - code/markdown cell
      - run your code
      - take notes
   - add cells above/below
   - cut (delete) / copy / paste cells
   - merge/split cells


- Advanced tips (L)
   - structuring your notebook
      - main storyline
      - scratch pad
   - note-taking in markdown
      - basics
      - equation
   - magic with ``line/cell-magic``
      - terminal commands
      - external modules (e.g., Fortran)



Next Activity
~~~~~~~~~~~~~~~~

`First use of SuPy <SuPy2>`: a quickstart to SuPy