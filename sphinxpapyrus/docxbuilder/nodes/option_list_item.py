# -*- coding: utf-8 -*-
"""
Translate docutils node option_list_item formatting.
each option_list_item start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "option_list_item"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing option_list_item node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing option_list_item node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.tables[-1][1] += 1
    visitor.tables[-1][2] = 0
