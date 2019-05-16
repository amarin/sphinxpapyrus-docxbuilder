# -*- coding: utf-8 -*-
"""
Translate docutils node hlistcol formatting.
each hlistcol start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "hlistcol"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing hlistcol node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing hlistcol node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
