# -*- coding: utf-8 -*-
"""
Translate docutils node caution formatting.
each caution start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "caution"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing caution node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing caution node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
