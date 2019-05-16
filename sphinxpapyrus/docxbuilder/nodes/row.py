# -*- coding: utf-8 -*-
"""
Translate docutils node row formatting.
each row start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "row"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing row node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing row node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.tables[-1][1] += 1
    visitor.tables[-1][2] = 0
