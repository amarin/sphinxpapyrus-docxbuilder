# -*- coding: utf-8 -*-
"""
Translate docutils node citation formatting.
each citation start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "citation"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing citation node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing citation node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
