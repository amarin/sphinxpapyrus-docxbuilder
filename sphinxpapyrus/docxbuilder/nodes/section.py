# -*- coding: utf-8 -*-
"""
Translate docutils node section formatting.
each section start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "section"


def visit(visitor: DocxTranslator, node: None):
    """Start processing section node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.section_level += 1
    if visitor.numbered:
        numId = visitor._get_new_num(abstractNumId=12)
        visitor.section_numIds.append(numId)


def depart(visitor: DocxTranslator, node: None):
    """Finish processing section node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.section_level -= 1
    if visitor.numbered:
        visitor.section_numIds.pop()
