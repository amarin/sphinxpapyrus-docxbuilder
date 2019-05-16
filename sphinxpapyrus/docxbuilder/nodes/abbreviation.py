# -*- coding: utf-8 -*-
"""
Translate docutils node abbreviation formatting.
each abbreviation start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "abbreviation"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing abbreviation node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing abbreviation node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
