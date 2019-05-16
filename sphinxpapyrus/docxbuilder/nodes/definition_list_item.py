# -*- coding: utf-8 -*-
"""
Translate docutils node definition_list_item formatting.
each definition_list_item start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "definition_list_item"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing definition_list_item node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing definition_list_item node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
