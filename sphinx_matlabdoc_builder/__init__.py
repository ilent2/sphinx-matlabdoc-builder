"""
    sphinx_matlabdoc_builder
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A Sphinx extension for generating Matlab HTML docs.
    :copyright: Copyright 2019 Isaac Lenton (aka ilent2)
    :license: BSD, see LICENSE for details.
"""

from .matlab_doc_builder import MatlabDocBuilder

def setup(app):
    app.add_builder(MatlabDocBuilder)

