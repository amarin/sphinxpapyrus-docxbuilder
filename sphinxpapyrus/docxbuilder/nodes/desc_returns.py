# -*- coding: utf-8 -*-
"""
Translate docutils node desc_returns formatting.
each desc_returns start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "desc_returns"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing desc_returns node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing desc_returns node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
