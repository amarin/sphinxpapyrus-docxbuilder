# -*- coding: utf-8 -*-
"""
Translate docutils node download_reference formatting.
each download_reference start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "download_reference"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing download_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing download_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
