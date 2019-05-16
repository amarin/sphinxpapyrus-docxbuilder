# -*- coding: utf-8 -*-
"""
Translate docutils node important formatting.
each important start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "important"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing important node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing important node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
