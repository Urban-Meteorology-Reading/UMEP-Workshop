.. _FAQ:

FAQ (Frequently Asked Questions)
--------------------------------

Here are common questions that appear throughout the workshop.

**Daily shading**

* I can see shadow patterns during the sunshine hours which is logical. Is it also possible to get a complete dark profile during nights? Because in the shadow animation I can only see the pictures during the day.(What IF I want to have for the complete day)?
    The animation is only for daytime when it comes to using the Shadow casting tool. This is because no data are created at night. You can have a look in the output folder and see the ``geotiff`` that are created.

* On the 21. Dec there is not really a clear difference between Building Shadows and Building+Veg Shadows as there was on 21. June, is that correct?
    Yes. You are in Sweden with very low sun elevations and 4-5 level buildings. That results in no vegetation shadows reaching the ground.


**Software installation**

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

* Jupyter notebooks are not?
    The recommended version ``2020.6.30`` seems to have installation issues due to a third-party package that prevents installation.
If unfortunately such issue happens, please manually install a development version of SuPy manually following these steps:

    1. Prepare utility functions in QGIS-python console by running the following:
