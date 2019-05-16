# -*- coding: utf-8 -*-
"""
Translate docutils node date formatting.
each date start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "date"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing date node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing date node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
