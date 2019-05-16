# -*- coding: utf-8 -*-
"""
Translate docutils node centered formatting.
each centered start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "centered"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing centered node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing centered node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
