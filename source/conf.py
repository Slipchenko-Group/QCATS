# Configuration file for the Sphinx documentation builder.
#
# This file contains the most common options. For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------

project = 'QCATS'
copyright = f'{datetime.now().year}, QCATS Organizing Committee'
author = 'QCATS Organizing Committee'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',             # Allows using Markdown (.md) files instead of just RST
    'sphinx_design',           # Enables responsive cards, tabs, and grids for speaker/schedule layouts
    'sphinxcontrib.bibtex',    # Optional: For managing a "Selected Publications" or tribute citation list
    'sphinx.ext.todo',
]

# Configure MyST Parser to enable extra Markdown features (like tables, colon fences, etc.)
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# Use the PyData Sphinx Theme for a clean, professional, non-manual academic portal look
html_theme = 'pydata_sphinx_theme'
#html_theme = 'shibuya'

# Theme options are theme-specific and customize the look and feel of a theme.
html_theme_options = {
    # Top navbar brand text/logo settings
    "logo": {
        "text": "QCATS 2027",
    },
    
    # Configure what shows up on the left sidebar.
    # For a conference site, we often want to turn off the left sidebar on main pages 
    # to give the speaker grid, tables, and photo gallery full page width.
    #"page_sidebar_items": [],  # Removes secondary right-sidebar by default if empty
    
    # Header navigation configuration
    "header_links_before_dropdown": 6,  # Shows all your main pages directly in the top bar without collapsing
    
    # Optional: Add an announcement banner at the very top (e.g., registration reminders)
    #"announcement": "✨ Registration is now open! Early bird deadline is approaching fast. ✨",
    
    # Icon links (e.g., to the hosting University department page or an organizing GitHub repo)
    # "icon_links": [
    #     {
    #         "name": "Department Home",
    #         "url": "https://www.purdue.edu/chemistry/",  # Replace with actual department/university URL
    #         "icon": "fa-solid fa-university",
    #         "type": "fontawesome",
    #     }
    # ],
    
    # Footer customization
    "footer_start": ["copyright"],
    #"footer_end": ["theme-version"],
    
    # # Color mode configuration (Light by default, but allows toggling)
    # "light_css_variables": {
    #     "color-brand-primary": "#002F6C",    # Customize this to match your institution's primary colors
    #     "color-brand-content": "#002F6C",
    # },

    # # Clean up the color variables using PyData's native primary/secondary controls:
    # "colors": {
    #     "primary": "navy",       # Try built-in color keywords first to test
    #     "secondary": "indigo",
    # },
}

# Add any paths that contain custom static files (such as images, custom CSS) here.
html_static_path = ['_static']
html_css_files = ['custom.css']
html_baseurl = 'https://slipchenko-group.github.io/QCATS/'

# Set the master document (usually index.rst or index.md)
master_doc = 'index'

# -- BibTeX Configuration (Optional) -----------------------------------------
# Path to your bibliography file if displaying the scientist's papers
bibtex_bibfiles = ['refs.bib']
