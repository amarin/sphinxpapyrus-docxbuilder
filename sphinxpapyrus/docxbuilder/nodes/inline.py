# -*- coding: utf-8 -*-
"""
Translate docutils node inline formatting.
each inline start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "inline"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing inline node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing inline node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
