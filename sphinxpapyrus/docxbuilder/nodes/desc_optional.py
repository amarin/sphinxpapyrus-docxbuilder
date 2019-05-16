# -*- coding: utf-8 -*-
"""
Translate docutils node desc_optional formatting.
each desc_optional start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "desc_optional"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing desc_optional node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing desc_optional node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
