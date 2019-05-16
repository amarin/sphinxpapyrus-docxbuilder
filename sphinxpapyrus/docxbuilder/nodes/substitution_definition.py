# -*- coding: utf-8 -*-
"""
Translate docutils node substitution_definition formatting.
each substitution_definition start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "substitution_definition"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing substitution_definition node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing substitution_definition node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
