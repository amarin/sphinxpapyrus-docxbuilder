# -*- coding: utf-8 -*-
"""
Translate docutils node list_item formatting.
each list_item start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "list_item"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing list_item node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.is_first_list_item = True
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing list_item node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
