# -*- coding: utf-8 -*-
"""
Translate docutils node desc_signature formatting.
each desc_signature start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "desc_signature"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing desc_signature node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p = visitor._add_paragraph()


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing desc_signature node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p = None
