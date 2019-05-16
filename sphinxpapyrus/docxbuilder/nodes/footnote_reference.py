# -*- coding: utf-8 -*-
"""
Translate docutils node footnote_reference formatting.
each footnote_reference start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import FOOTNOTE_REFERENCE
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "footnote_reference"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing footnote_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    text = node.astext()
    # text = nodes.Text(node.get('title', '#'))
    visitor.r = visitor.p.add_run(
        '[%s]' % (text),
        style=STYLES[FOOTNOTE_REFERENCE]
    )
    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing footnote_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
