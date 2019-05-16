# -*- coding: utf-8 -*-
"""
Translate docutils node substitution_reference formatting.
each substitution_reference start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "substitution_reference"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing substitution_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing substitution_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
