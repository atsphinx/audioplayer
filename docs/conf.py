from atsphinx.audioplayer import __version__ as version

# -- Project information
project = "atsphinx-audioplayer"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = version

# -- General configuration
extensions = [
    "atsphinx.audioplayer",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_design",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "furo"
html_static_path = ["_static"]

# -- Extension configuration
# For sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}


def setup(app):
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
