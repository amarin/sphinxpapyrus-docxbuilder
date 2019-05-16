# -*- coding: utf-8 -*-
"""
Translate docutils node rubric formatting.
each rubric start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "rubric"


def visit(visitor: DocxTranslator, node: None):
    """Start processing rubric node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: None):
    """Finish processing rubric node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
