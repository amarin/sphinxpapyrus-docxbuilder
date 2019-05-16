# -*- coding: utf-8 -*-
"""
Translate docutils node line_block formatting.
each line_block start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import LINE_BLOCK
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "line_block"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing line_block node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.append(STYLES[LINE_BLOCK])


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing line_block node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.pop()
