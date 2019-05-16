# -*- coding: utf-8 -*-
"""
Translate docutils node comment formatting.
each comment start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "comment"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing comment node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing comment node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
