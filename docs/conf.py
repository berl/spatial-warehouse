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


# -- Project information -----------------------------------------------------

project = 'starspace'
copyright = '2019, Ambrose J. Carr'
author = 'Ambrose J. Carr'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'numpydoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'sphinxcontrib.programoutput',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.intersphinx',
    'm2r',
]

# intersphinx mapping for outside starfish linking
intersphinx_mapping = {'xarray': ('http://xarray.pydata.org/en/stable', None),
                       'numpy': ('https://docs.scipy.org/doc/numpy/', None),
                       'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
                       'trackpy': ('https://soft-matter.github.io/trackpy/v0.3.2/',  None),
                       'skimage': ('https://scikit-image.org/docs/dev/', None)}

# numpydoc settings
numpydoc_class_members_toctree = False
numpydoc_show_inherited_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# from recommonmark.parser import CommonMarkParser
#
# source_parsers = {
#     '.md': CommonMarkParser,
# }
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# html_theme = 'bootstrap'

# import sphinx_bootstrap_theme
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_theme_options = {
#     'source_link_position': "footer",
#     'bootswatch_theme': "flatly", # https://bootswatch.com/
#     'navbar_sidebarrel': False,
#     'bootstrap_version': "3",
#     'navbar_links': [
#                      ("Introduction", "introduction/introduction"),
#                      ("Installation", "installation/installation"),
#                      ("API", "api/index"),
#                      ],

#     }

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'starspacedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'starspace', 'Starspace Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'starspace', 'Starspace Documentation',
     author, 'Starspace', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# See https://stackoverflow.com/a/45565445/56887
autodoc_mock_imports = ['_tkinter']

sphinx_gallery_conf = {
    'ignore_pattern': r'__init__\.py',
    'examples_dirs': [
        '../conversion_examples',
    ],
    'gallery_dirs': [
        'conversion_examples',
    ],
    'filename_pattern': '/exec_',
}