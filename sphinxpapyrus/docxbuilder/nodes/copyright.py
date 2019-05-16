# -*- coding: utf-8 -*-
"""
Translate docutils node copyright formatting.
each copyright start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "copyright"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing copyright node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing copyright node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
