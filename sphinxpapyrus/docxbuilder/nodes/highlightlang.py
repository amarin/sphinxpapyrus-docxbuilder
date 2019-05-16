# -*- coding: utf-8 -*-
"""
Translate docutils node highlightlang formatting.
each highlightlang start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "highlightlang"


def visit(visitor: DocxTranslator, node: None):
    """Start processing highlightlang node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: None):
    """Finish processing highlightlang node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
