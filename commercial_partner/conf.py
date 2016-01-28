import sys
import os
import shlex
extensions = ['sphinx.ext.graphviz',]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'eTicketing Manual - Commercial Partners'
copyright = u'2016, Parks Australia'
author = u'Parks Australia'

version = '0.0'
release = '0.0.1'

language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
latex_elements = {
'papersize': 'a4paper',
# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',
}

latex_documents = [
  (master_doc, 'UserManual-CommercialPartner.tex', u'eTicketing Manual - Commercial Partners',
   u'Parks Australia', 'manual'),
]

