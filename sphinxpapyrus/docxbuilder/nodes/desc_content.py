# -*- coding: utf-8 -*-
"""
Translate docutils node desc_content formatting.
each desc_content start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "desc_content"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing desc_content node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_level += 1
    visitor.p = visitor._add_paragraph()


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing desc_content node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_level -= 1
    visitor.p = None
