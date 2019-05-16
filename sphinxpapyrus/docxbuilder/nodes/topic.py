# -*- coding: utf-8 -*-
"""
Translate docutils node topic formatting.
each topic start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "topic"


def visit(visitor: DocxTranslator, node: None):
    """Start processing topic node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: None):
    """Finish processing topic node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
