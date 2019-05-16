# -*- coding: utf-8 -*-
"""
Translate docutils node version formatting.
each version start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "version"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing version node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing version node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
