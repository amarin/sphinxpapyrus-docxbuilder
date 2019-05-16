# -*- coding: utf-8 -*-
"""
Translate docutils node pending_xref formatting.
each pending_xref start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "pending_xref"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing pending_xref node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing pending_xref node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
