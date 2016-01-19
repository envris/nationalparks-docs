import sys
import os
import shlex
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'User Manual - Commercial Partners'
copyright = u'2016, Parks Australia'
author = u'Parks Australia'
version = '0.0'
release = '0.0.1'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
htmlhelp_basename = 'UserManual-CTO'
latex_elements = {
    'papersize': 'A4paper',
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt',
}

latex_documents = [
  (master_doc, 'UserManual-CommercialPartners.tex', u'eTicketing Manual - Commercial Tour Operator',
   u'Parks Australia', 'manual'),
]
