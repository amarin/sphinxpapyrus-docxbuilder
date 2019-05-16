# -*- coding: utf-8 -*-
"""
Translate docutils node line formatting.
each line start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "line"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing line node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    text = node.astext()
    visitor.p = visitor._add_paragraph(text, style=visitor.p_style)
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing line node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p = None
