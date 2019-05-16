# -*- coding: utf-8 -*-
"""
Translate docutils node manpage formatting.
each manpage start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "manpage"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing manpage node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    return visitor.visit_literal_emphasis(node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing manpage node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.depart_literal_emphasis(node)
