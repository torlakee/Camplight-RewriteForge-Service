# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Add your source code directory to sys.path --------------------------------
sys.path.insert(0, os.path.abspath('../../src'))

# -- Project information -----------------------------------------------------
project = 'RewriteForge'
copyright = '2025, .'
author = '.'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",              # Auto-imports docstrings
    "sphinx.ext.napoleon",             # Supports Google & NumPy style docstrings
    "sphinx_autodoc_typehints",        # Type hints in signatures and docs
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output options -----------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']