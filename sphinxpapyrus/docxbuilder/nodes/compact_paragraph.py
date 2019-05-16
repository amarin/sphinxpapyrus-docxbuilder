# -*- coding: utf-8 -*-
"""
Translate docutils node compact_paragraph formatting.
each compact_paragraph start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "compact_paragraph"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing compact_paragraph node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing compact_paragraph node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
