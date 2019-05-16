# -*- coding: utf-8 -*-
"""
Translate docutils node literal_strong formatting.
each literal_strong start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "literal_strong"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing literal_strong node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing literal_strong node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
