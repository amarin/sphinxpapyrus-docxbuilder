# -*- coding: utf-8 -*-
"""
Translate docutils node number_reference formatting.
each number_reference start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Element
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "number_reference"


def visit(visitor: DocxTranslator, node: Element):
    """Start processing number_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Element)

    text = node.children[0].astext()
    visitor.r = visitor.p.add_run(text, style=visitor.r_style)
    raise nodes.SkipNode

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing number_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
