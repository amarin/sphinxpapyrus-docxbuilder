# -*- coding: utf-8 -*-
"""
Translate docutils node generated formatting.
each generated start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "generated"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing generated node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing generated node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
