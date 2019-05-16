# -*- coding: utf-8 -*-
"""
Translate docutils node hlist formatting.
each hlist start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "hlist"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing hlist node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing hlist node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
