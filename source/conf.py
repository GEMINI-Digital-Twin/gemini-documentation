import os
import sys

import git
from pathlib import Path


def get_gemini_parent_root(path):
    git_repo = git.Repo(path, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")

    return Path(git_root).parent


gemini_root_dir = get_gemini_parent_root(os.getcwd())

sys.path.insert(0, os.path.join(gemini_root_dir, 'gemini-model', 'src'))
sys.path.insert(0, os.path.join(gemini_root_dir, 'gemini-framework', 'src'))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GEMINI Geothermal Digital Twin'
copyright = '2024, TNO'
author = 'Ryvo Octaviano, Demetris Palochis, Leila Hashemi, Jonah Poort, Pejman Shoeibi Omrani'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.coverage',
              'sphinx.ext.napoleon',
              'sphinxcontrib.jquery']

templates_path = ['_templates']
exclude_patterns = []
autoclass_content = 'both'
autodoc_default_options = {

}

# Enable numref
numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
