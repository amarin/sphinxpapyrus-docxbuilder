# -*- coding: utf-8 -*-
"""
Translate docutils node option_argument formatting.
each option_argument start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "option_argument"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing option_argument node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing option_argument node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
