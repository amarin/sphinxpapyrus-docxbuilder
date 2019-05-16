# -*- coding: utf-8 -*-
"""
Translate docutils node desc_type formatting.
each desc_type start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "desc_type"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing desc_type node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing desc_type node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
