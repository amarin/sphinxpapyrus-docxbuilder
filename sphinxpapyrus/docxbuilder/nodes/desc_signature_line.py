# -*- coding: utf-8 -*-
"""
Translate docutils node desc_signature_line formatting.
each desc_signature_line start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "desc_signature_line"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing desc_signature_line node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing desc_signature_line node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
