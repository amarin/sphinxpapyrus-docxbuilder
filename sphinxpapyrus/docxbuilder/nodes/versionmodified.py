# -*- coding: utf-8 -*-
"""
Translate docutils node versionmodified formatting.
each versionmodified start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "versionmodified"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing versionmodified node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing versionmodified node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
