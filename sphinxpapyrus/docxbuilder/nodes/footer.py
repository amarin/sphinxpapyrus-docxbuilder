# -*- coding: utf-8 -*-
"""
Translate docutils node footer formatting.
each footer start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "footer"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing footer node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing footer node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
