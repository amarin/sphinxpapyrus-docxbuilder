# -*- coding: utf-8 -*-
"""
Translate docutils node tbody formatting.
each tbody start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "tbody"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing tbody node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing tbody node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
