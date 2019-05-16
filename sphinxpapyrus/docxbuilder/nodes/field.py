# -*- coding: utf-8 -*-
"""
Translate docutils node field formatting.
each field start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "field"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing field node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing field node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.tables[-1][1] += 1
    visitor.tables[-1][2] = 0
