# -*- coding: utf-8 -*-
"""
Translate docutils node table formatting.
each table start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "table"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing table node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor._add_paragraph_between_table(node)
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing table node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
