# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Study'
author = 'Roleran'

release = '0.1'
version = '0.1.0'

# -- General configuration
# myst_parser 会把 Markdown 里的本地图片交给 Sphinx 复制到网页。
# 之前的 recommonmark 只改了图片地址，没有把 png 放进构建结果，所以线上是坏图。

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# 笔记里的表格是普通 Markdown 表格，需要打开这个扩展。
myst_enable_extensions = [
    'colon_fence',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
