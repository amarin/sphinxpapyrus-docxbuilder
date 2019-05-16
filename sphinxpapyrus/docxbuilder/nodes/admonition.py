# -*- coding: utf-8 -*-
"""
Translate docutils node admonition formatting.
each admonition start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "admonition"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing admonition node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing admonition node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
