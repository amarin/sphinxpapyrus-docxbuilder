# -*- coding: utf-8 -*-
"""
Translate docutils node authors formatting.
each authors start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "authors"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing authors node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing authors node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
