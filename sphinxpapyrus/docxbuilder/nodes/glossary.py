# -*- coding: utf-8 -*-
"""
Translate docutils node glossary formatting.
each glossary start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "glossary"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing glossary node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing glossary node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
