.. _FAQ:

FAQ (Frequently Asked Questions)
--------------------------------

Here are common questions that appear throughout the workshop.

**General**

* I have a Mac computer. Can I still participate in the workshop?
   Yes, QGIS and UMEP are software independent but some of the tutorials are just for windows users. The tutorial on Lidar processing, `section 4.4 <https://umep-workshop.readthedocs.io/en/latest/GettingData/GIS3.html>`__ is for Windows user only. Otherwise, all other activities is for all OS. Installation of UMEP can be a bit cjallenging on a Mac, but help instructions are included below (see below).

**Daily shading**

* I can see shadow patterns during the sunshine hours which is logical. Is it also possible to get a complete dark profile during nights? Because in the shadow animation I can only see the pictures during the day.(What IF I want to have for the complete day)?
    The animation is only for daytime when it comes to using the Shadow casting tool. This is because no data are created at night. You can have a look in the output folder and see the ``geotiff`` that are created.

* On the 21. Dec there is not really a clear difference between Building Shadows and Building+Veg Shadows as there was on 21. June, is that correct?
    Yes. You are in Sweden with very low sun elevations and 4-5 level buildings. That results in no vegetation shadows reaching the ground.

**LIDAR processing**

* I cannot start the FUSION viewer in QGIS. What I have been doing wrong?
    One common misstake is that FUSION is not installed on your computer. To use FUSION within QGIS yo first need to install the actual software form `<http://forsys.sefs.uw.edu/fusion/fusionlatest.html>`__. Then you should install the plugin FUSION for processing and make the settings according to the tutorial instructions.

**Software installation - Mac**

.. _supy_umep_install:

* SuPy couldn't be installed automatically on my Mac. What should I do?
    The recommended version ``2020.6.30`` seems to have installation issues due to a third-party package that prevents installation.
    If unfortunately such issue happens, please manually install a development version of SuPy manually following these steps:

    1. Prepare utility functions in QGIS-python console by running the following:

    .. code-block:: python

        import sys, subprocess, os
        from pathlib import Path
        import platform

        # locate QGIS-python interpreter
        def locate_py():
            try:
                # non-Linux
                path_py = os.environ["PYTHONHOME"]
            except Exception:
                # Linux
                path_py = sys.executable

            # convert to Path for eaiser processing
            path_py = Path(path_py)

            # pre-defined paths for python executable
            dict_pybin = {
                "Darwin": path_py / "bin" / "python3",
                "Windows": path_py / "python3.exe",
                "Linux": path_py,
            }

            # python executable
            path_pybin = dict_pybin[platform.system()]

            if path_pybin.exists():
                return path_pybin
            else:
                raise RuntimeError("UMEP cannot locate the Python interpreter used by QGIS!")

        # install supy
        def install_supy(ver=None):

            str_ver = f"=={ver}" if ver else ""
            try:
                path_pybin = locate_py()
                list_cmd = f"{str(path_pybin)} -m pip install supy{str_ver} -U --user".split()
                list_info = subprocess.check_output(list_cmd, encoding="UTF8").split("\n")
                str_info = list_info[-2].strip()
                str_info = (
                    str_info
                    if len(str_info) > 0
                    else f"supy{str_ver} has already been installed!"
                )
                return str_info
            except Exception:
                raise RuntimeError(f"UMEP couldn't install supy{str_ver}!") from Exception

    This code snippet should determine the actual path of Python interpreter QGIS is using.

    2. install a development version of SuPy:

    Also in the QGIS-python console, run this:

    .. code-block:: python

        install_supy(ver='2020.7.8dev0')

    3. restart your QGIS

    .. note:: If this issue persists, please `raise an issue in the UMEP repo <https://github.com/UMEP-dev/UMEP/issues/new/choose>`_ and let Ting Sun know by ``@sunt05``.



.. _jn_install:

* Jupyter notebooks CANNOT be launched? What should I do?
   Please check the following in your command line tool (e.g., Terminal on macOS, OSGeo4W prompt on Windows given QGIS installed):

   .. note:: if using OSGeo4W prompt, please run ``py3_env`` first to switch to your python3 environment.

   1. Check if Jupyter notebook is installed:

    .. code-block:: shell

        python3 -m pip show notebook

    if not, please install it:

    .. code-block:: shell

        python3 -m pip install notebook --user --upgrade

   2. Jupyter notebook is installed but cannot be properly launched:

    try to re-install it:

    uninstall it first:

    .. code-block:: shell

        python3 -m pip uninstall notebook -y

    then install it:

    .. code-block:: shell

        python3 -m pip install notebook --user --upgrade

**Errors related to parameters derivation**

* I am getting errors related to pandas and SuPy, when running the notebooks for parameter derivation.
    This can happen because of various reasons when running notebooks in `this <https://umep-workshop.readthedocs.io/en/latest/Parameters/tutorials/CP2.html>`_ page; however, the most frequent reason is because ``Python``, ``SuPy`` and ``pandas`` versions does not match the required ones in the `yml file <https://github.com/Urban-Meteorology-Reading/SUEWS_parameters/blob/master/environment.yml>`_ (see instructions in step 2 of `this page <https://umep-workshop.readthedocs.io/en/latest/Parameters/CalcParam.html#steps-to-using-these-notebooks>`_). If you are using different version than the `yml file <https://github.com/Urban-Meteorology-Reading/SUEWS_parameters/blob/master/environment.yml>`_, you need to upgrade/downgrade the rquired packages.  
    