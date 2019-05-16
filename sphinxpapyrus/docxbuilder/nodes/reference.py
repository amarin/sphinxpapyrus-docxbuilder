# -*- coding: utf-8 -*-
"""
Translate docutils node reference formatting.
each reference start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import REFERENCE
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "reference"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    # TODO: add hyperlink
    visitor.r_style = STYLES[REFERENCE]
    visitor.r = visitor.p.add_run(style=visitor.r_style)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = None
