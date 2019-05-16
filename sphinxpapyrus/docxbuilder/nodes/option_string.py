# -*- coding: utf-8 -*-
"""
Translate docutils node option_string formatting.
each option_string start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "option_string"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing option_string node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing option_string node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
