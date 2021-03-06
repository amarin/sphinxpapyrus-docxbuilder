# -*- coding: utf-8 -*-
"""
Translate docutils node tip formatting.
each tip start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "tip"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing tip node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing tip node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
