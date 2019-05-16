# -*- coding: utf-8 -*-
"""
Translate docutils node hint formatting.
each hint start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "hint"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing hint node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing hint node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
