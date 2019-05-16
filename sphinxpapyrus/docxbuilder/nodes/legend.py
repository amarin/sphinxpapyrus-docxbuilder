# -*- coding: utf-8 -*-
"""
Translate docutils node legend formatting.
each legend start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "legend"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing legend node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing legend node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
