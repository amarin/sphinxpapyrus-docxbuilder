# -*- coding: utf-8 -*-
"""
Translate docutils node sidebar formatting.
each sidebar start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "sidebar"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing sidebar node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing sidebar node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
