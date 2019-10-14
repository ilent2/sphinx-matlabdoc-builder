"""
    sphinx_matlabdoc_builder.matlab_doc_builder
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A Sphinx extension for generating Matlab HTML docs.
    Based on sphinxcontrib.htmlhelp
    :copyright: Copyright 2019 Isaac Lenton (aka ilent2)
    :license: BSD, see LICENSE for details.
"""

import html
import os
from os import path

from docutils import nodes

from sphinx import addnodes
from sphinx.util.nodes import NodeMatcher
from sphinx.util.osutil import make_filename_from_project, relpath
from sphinx.locale import __
from sphinx.builders.html import StandaloneHTMLBuilder

def chm_htmlescape(s: str, quote: bool = True) -> str:
    """
    chm_htmlescape() is a wrapper of html.escape().
    .hhc/.hhk files don't recognize hex escaping, we need convert
    hex escaping to decimal escaping. for example: ``&#x27;`` -> ``&#39;``
    html.escape() may generates a hex escaping ``&#x27;`` for single
    quote ``'``, this wrapper fixes this.
    """
    s = html.escape(s, quote)
    s = s.replace('&#x27;', '&#39;')    # re-escape as decimal
    return s

# Class from HTMLHelp
class ToCTreeVisitor(nodes.NodeVisitor):
    def __init__(self, document):
        super().__init__(document)
        self.body = []  # type: List[str]
        self.depth = 0

    def append(self, text):
        self.body.append('  '*self.depth + text)

    def astext(self):
        return '\n'.join(self.body)

    def unknown_visit(self, node):
        pass

    def unknown_departure(self, node):
        pass

    def visit_bullet_list(self, node):
        self.depth += 1

    def depart_bullet_list(self, node):
        self.depth -= 1

    def visit_list_item(self, node):
        self.depth += 1

    def depart_list_item(self, node):
        self.append('</tocitem>')
        self.depth -= 1

    def visit_reference(self, node):
        title = chm_htmlescape(node.astext(), True)
        self.append('<tocitem target="{}">{}'.format(node['refuri'], title))
        raise nodes.SkipNode

class MatlabDocBuilder(StandaloneHTMLBuilder):
    """
    HTML builder that also outputs Matlab helptoc.xml file
    for generating Matlab documentation.
    """
    name = 'matlabdoc'
    epilog = __('The Matlab documentation files are in %(outdir)s.')

    # don't copy the reST source
    copysource = False

    # don't add links
    add_permalinks = False

    # don't add sidebar etc.
    embedded = True

    # don't generate search index or include search page
    search = False

    def handle_finish(self):
        self.build_toc_file()
        super().handle_finish()

    def build_toc_file(self):
        """Create a ToC file helptoc.xml in outdir."""

        filename = path.join(self.outdir, 'helptoc.xml')

        with open(filename, 'w', encoding='utf-8') as f:

            f.write("""<?xml version='1.0' encoding="utf-8"?>\n""")
            f.write("""<toc version="2.0">\n""")
            f.write('<tocitem target="{}">{}\n'.format(
                self.config.master_doc + '.html', self.config.project))

            toctree = self.env.get_and_resolve_doctree(self.config.master_doc, self,
                                                       prune_toctrees=False)
            visitor = ToCTreeVisitor(toctree)
            matcher = NodeMatcher(addnodes.compact_paragraph, toctree=True)
            for node in toctree.traverse(matcher):  # type: addnodes.compact_paragraph
                node.walkabout(visitor)

            f.write(visitor.astext() + '\n')

            f.write('</tocitem>\n')
            f.write('</toc>\n')

