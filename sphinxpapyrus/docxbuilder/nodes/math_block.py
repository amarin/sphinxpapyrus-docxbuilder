# -*- coding: utf-8 -*-
"""
Translate docutils node math_block formatting.
each math_block start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "math_block"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing math_block node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing math_block node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
