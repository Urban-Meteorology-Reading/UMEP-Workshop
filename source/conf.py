# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# import guzzle_sphinx_theme
# import recommonmark
# from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------

project = "UMEP Workshop"
copyright = "2020, Sue Grimmond, Fredrik Lindberg, Ting Sun and Kit Benjamin"
author = "Sue Grimmond, Fredrik Lindberg, Ting Sun and Kit Benjamin"

# The full version, including alpha/beta/rc tags
release = "20200626"


html_static_path = ['_static']

# -- General configuration ---------------------------------------------------

# master_doc='Home'

default_role='any'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    # "recommonmark",
    "sphinx_rtd_theme",
    # 'guzzle_sphinx_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "Urban-Meteorology-Reading", # Username
    "github_repo": "UMEP-Workshop.io", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root
}
# html_theme = 'guzzle_sphinx_theme'
# html_theme_path = guzzle_sphinx_theme.html_theme_path()
# html_theme = "alabaster"

# Register the theme as an extension to generate a sitemap.xml
# extensions.append("guzzle_sphinx_theme")

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": project,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# some text replacement defintions
rst_epilog = """
.. |km^-1| replace:: km\ :sup:`-1`
.. |mm^-1| replace:: mm\ :sup:`-1`
.. |m^-1| replace:: m\ :sup:`-1`
.. |m^-2| replace:: m\ :sup:`-2`
.. |m^-3| replace:: m\ :sup:`-3`
.. |m^3| replace:: m\ :sup:`3`
.. |s^-1| replace:: s\ :sup:`-1`
.. |kg^-1| replace:: kg\ :sup:`-1`
.. |K^-1| replace:: K\ :sup:`-1`
.. |W^-1| replace:: W\ :sup:`-1`
.. |h^-1| replace:: h\ :sup:`-1`
.. |ha^-1| replace:: ha\ :sup:`-1`
.. |QF| replace:: Q\ :sub:`F`
.. |Qstar| replace:: Q\ :sup:`*`
.. |d^-1| replace:: d\ :sup:`-1`
.. |d^-2| replace:: d\ :sup:`-2`
.. |)^-1| replace:: )\ :sup:`-1`
.. |Recmd| replace:: **Recommended in this version.**
.. |NotRecmd| replace:: **Not recommended in this version.**
.. |NotAvail| replace:: **Not available in this version.**
.. |NotUsed| replace:: **Not used in this version.**

.. _GitHub page: https://github.com/Urban-Meteorology-Reading/UMEP-Workshop.io/issues/new?assignees=&labels=docs&template=docs-issue-report.md&title=

.. only:: html

    .. note::

      1. Got stuck? Please check out the `help page <NeedHelp>`.
      2. Please report issues with the manual on the `GitHub page`_.


"""


# # app setup hook
# def setup(app):
#     app.add_config_value('recommonmark_config', {
#         #'url_resolver': lambda url: github_doc_root + url,
#         # 'auto_toc_tree_section': 'Workshop Structure',
#         'enable_math': True,
#         'enable_inline_math': True,
#         'enable_eval_rst': True,
#         'enable_auto_doc_ref': True,
#     }, True)
#     app.add_transform(AutoStructify)
