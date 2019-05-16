# -*- coding: utf-8 -*-
"""
Translate docutils node target formatting.
each target start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "target"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing target node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing target node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
