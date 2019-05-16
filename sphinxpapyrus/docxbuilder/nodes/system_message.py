# -*- coding: utf-8 -*-
"""
Translate docutils node system_message formatting.
each system_message start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "system_message"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing system_message node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing system_message node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
