# -*- coding: utf-8 -*-
"""
Translate docutils node danger formatting.
each danger start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "danger"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing danger node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing danger node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
