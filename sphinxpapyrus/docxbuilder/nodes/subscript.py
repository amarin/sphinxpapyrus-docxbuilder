# -*- coding: utf-8 -*-
"""
Translate docutils node subscript formatting.
each subscript start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import SUBSCRIPT
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "subscript"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing subscript node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = STYLES[SUBSCRIPT]


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing subscript node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = None
