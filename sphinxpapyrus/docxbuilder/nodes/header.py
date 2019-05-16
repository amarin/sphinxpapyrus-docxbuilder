# -*- coding: utf-8 -*-
"""
Translate docutils node header formatting.
each header start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "header"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing header node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing header node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
