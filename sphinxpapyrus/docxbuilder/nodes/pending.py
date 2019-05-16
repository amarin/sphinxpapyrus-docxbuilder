# -*- coding: utf-8 -*-
"""
Translate docutils node pending formatting.
each pending start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "pending"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing pending node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing pending node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
