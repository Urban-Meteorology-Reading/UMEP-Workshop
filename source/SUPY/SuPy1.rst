.. _SuPy1:

Preparation for using SuPy
--------------------------

**This will take:** ~30 mins

**Prior to this activity**

- Be familiar with SUEWS in UMEP

- `Introduction to Jupyter Notebooks <JN0>`

- `Jupyter Notebook Cheatsheet <https://cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/>`_


.. note:: 
 It is very important you do the right thing at this point.
  
  #. If you are a **Windows** user without a version of Python on you computer except for QGIS if so go `here <jpt_win>`
  #. If you already have Jupyter Notebooks installed use that
  #. Otherwise follow `these instructions <jpt_gen>`


**Activity**

- *Installation of Jupyter Notebooks - follow the appropriate instructions for your operating system*
- If you already have Python3 and Jupyter Notebooks installed you do not need to do this.
- If you are a **Windows** user, `install the QGIS version <jpt_win>` **OR** you can go to `Anaconda-based approach <jpt_gen>` for **General (all platforms)**.


.. _jpt_win:

**Windows+QGIS:** ``osgeo``-based approach

.. raw:: html

   <div style="text-align: center; margin-bottom: 2em;">
   <iframe width="100%" height="350" src="https://www.youtube.com/embed/bvZOOYZ0QOU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
   </div>


- With your already `installed QGIS <QGIS1>`,  go to the start menu in Windows, locate **OSGeo4W Shell** and open it. If you automatically do not have administrative rights you need to right-click on **OSGeo4W Shell**, *Open file Location*, Right-click on **OSGeo4W Shell** again and choose *Run as Administrator*; type the following two commands:

.. code-block:: SHELL

   py3_env
   pip install notebook

- To start Jupyter Notebook type:

.. code-block:: SHELL

   jupyter notebook


.. _jpt_gen:

**(or) General OS installation (all platforms)**: `Anaconda-based approach <https://docs.anaconda.com/anaconda/install/>`_

- Download Anaconda3:

.. raw:: html

   <div style="text-align: center; margin-bottom: 2em;">
   <iframe width="100%" height="350" src="https://www.youtube.com/embed/AnPHtLf7gYc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
   </div>

- Install Anaconda3 (Jupyter Notebook included):

.. raw:: html

   <div style="text-align: center; margin-bottom: 2em;">
   <iframe width="100%" height="350" src="https://www.youtube.com/embed/qCZW5Esh3O8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
   </div>

- Launch Jupyter Notebook:

.. raw:: html

   <div style="text-align: center; margin-bottom: 2em;">
   <iframe width="100%" height="350" src="https://www.youtube.com/embed/PG2laJaHNsU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
   </div>

** Everyone**

- Install Jupyter Notebook Extensions (Optional, but recommended):
After you have completed the above, you are likely to want to install some Jupyter extensions. We `recommend <JN0>` these.
The method to `install the extensions is here <https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html>`_


.. note::
   If you use Anaconda for Python, it is better to choose `conda-forge <https://conda-forge.org/#about>`_ channel for package installation to have better compatibility with various scientific libraries.






