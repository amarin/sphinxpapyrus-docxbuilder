# -*- coding: utf-8 -*-
"""
Translate docutils node definition formatting.
each definition start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "definition"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing definition node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_level += 1


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing definition node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_level -= 1
