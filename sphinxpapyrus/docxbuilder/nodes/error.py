# -*- coding: utf-8 -*-
"""
Translate docutils node error formatting.
each error start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "error"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing error node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing error node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
