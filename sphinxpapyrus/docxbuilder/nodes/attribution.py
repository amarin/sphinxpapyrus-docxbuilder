# -*- coding: utf-8 -*-
"""
Translate docutils node attribution formatting.
each attribution start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "attribution"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing attribution node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing attribution node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
