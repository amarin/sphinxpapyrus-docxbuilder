# -*- coding: utf-8 -*-
"""
Translate docutils node text formatting.
each text start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "Text"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing text node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    if visitor.p:
        if isinstance(node.parent, nodes.field_name):
            text = node.astext() + ':'
        elif isinstance(node.parent, nodes.literal_block):
            text = node.astext().replace('\n\n', '\n')
        elif isinstance(node.parent, nodes.doctest_block):
            text = node.astext().replace('\n\n', '\n')
        else:
            text = node.astext().replace('\n', ' ')
        visitor.r = visitor._add_run(text, style=visitor.r_style)

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing text node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
