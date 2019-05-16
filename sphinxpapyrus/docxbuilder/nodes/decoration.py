# -*- coding: utf-8 -*-
"""
Translate docutils node decoration formatting.
each decoration start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "decoration"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing decoration node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing decoration node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
