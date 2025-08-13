# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
from datetime import datetime

project = "Awesome Data Analysis"
copyright = f"{datetime.now().year}, Pavel Grigoryev"
author = "Pavel Grigoryev"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]
html_css_files = ["custom.css"]

sys.path.insert(0, os.path.abspath(".."))

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
]

html_sidebars = {"**": []}

myst_all_links_external = True

html_theme = "sphinx_book_theme"

html_theme_options = {
    "show_navbar_depth": 1,
    "show_toc_level": 2,
    "collapse_navbar": True,
    "use_fullscreen_button": True,
    "use_download_button": True,
    "use_repository_button": True,
    "repository_url": "https://github.com/PavelGrigoryevDS/awesome-data-analysis",
}

source_suffix = {
    ".md": "markdown",
}
