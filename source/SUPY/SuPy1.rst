.. _SuPy1:

Preparation for using SuPy
--------------------------

**This will take:** ~30 mins

**Prior to this activity**

- Be familiar with SUEWS in UMEP
- `Introduction to Jupyter Notebooks <Jupyter/JN0>`_
- `Jupyter Notebook Cheatsheet <https://cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/>`_


**Activity**

- *Installation of Jupyter Notebooks - follow the appropriate inststructcions for your operating system*
- If you already have Python and Jupyter Notebooks installed you do not need to do this. If you are a **Windows** user install the QGIS version **OR** you can go to **General**


**Windows+QGIS:** ``osgeo``-based approach

   - With your already `installed <QGIS1>`  go to the start menu in Windows, locate **OSGeo4W Shell** and open it. If you automatically do not have administrative rights you need to right-click on **OSGeo4W Shell**, *Open file Location*, Right-click on **OSGeo4W Shell** again and choose *Run as Administrator*; type the following two commands:

   .. code-block:: SHELL

      py3_env
      pip install notebook

   - To start Jupyter Notebook type:

   .. code-block:: SHELL

      jupyter notebook


**General (all platforms)**: `Anaconda-based approach <https://docs.anaconda.com/anaconda/install/>`_


After you have completed the above follow these instructions to install Jupyter Notebook Extensions: `Installation <https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html>`_


.. note::
   If you use Anaconda for Python, it is better to choose `conda-forge` channel for package installation to have better compatibility with various scientific libraries.






