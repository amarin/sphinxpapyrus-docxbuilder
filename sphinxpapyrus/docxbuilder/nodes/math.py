# -*- coding: utf-8 -*-
"""
Translate docutils node math formatting.
each math start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Element
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "math"


def visit(visitor: DocxTranslator, node: Element):
    """Start processing math node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Element)

    # TODO: support to convert from latex to docx
    eq = node.get('latex')
    text = eq if eq else node.astext()
    visitor.r = visitor._add_run(text, style=visitor.r_style)
    visitor.r = None
    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing math node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
