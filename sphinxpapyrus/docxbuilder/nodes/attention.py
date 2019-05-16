# -*- coding: utf-8 -*-
"""
Translate docutils node attention formatting.
each attention start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "attention"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing attention node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing attention node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
