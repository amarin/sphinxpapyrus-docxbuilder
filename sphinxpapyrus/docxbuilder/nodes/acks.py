# -*- coding: utf-8 -*-
"""
Translate docutils node acks formatting.
each acks start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "acks"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing acks node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing acks node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
