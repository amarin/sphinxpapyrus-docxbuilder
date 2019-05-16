# -*- coding: utf-8 -*-
"""
Translate docutils node status formatting.
each status start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "status"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing status node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing status node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
