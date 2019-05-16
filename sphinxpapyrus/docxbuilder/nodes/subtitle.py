# -*- coding: utf-8 -*-
"""
Translate docutils node subtitle formatting.
each subtitle start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "subtitle"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing subtitle node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing subtitle node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
