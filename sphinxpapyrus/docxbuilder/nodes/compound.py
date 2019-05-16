# -*- coding: utf-8 -*-
"""
Translate docutils node compound formatting.
each compound start will processed with visit() and finished with depart()
"""
from docutils.nodes import Element
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "compound"


def visit(visitor: DocxTranslator, node: Element):
    """Start processing compound node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Element)

    if 'toctree-wrapper' in node.get('classes', None):
        numbered = node.get('numbered', 0)
        if numbered > 0 and visitor.numbered_level <= visitor.section_level:
            visitor.numbered = numbered
            visitor.numbered_level = visitor.section_level


def depart(visitor: DocxTranslator, node: Element):
    """Finish processing compound node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Element)

    if 'toctree-wrapper' in node.get('classes', None):
        numbered = node.get('numbered', 0)
        if numbered > 0 and visitor.numbered_level <= visitor.section_level:
            visitor.numbered = 0

