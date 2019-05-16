# -*- coding: utf-8 -*-
"""
Translate docutils node acronym formatting.
each acronym start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "acronym"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing acronym node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing acronym node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
