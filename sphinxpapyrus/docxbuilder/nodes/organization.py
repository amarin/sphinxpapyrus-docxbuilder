# -*- coding: utf-8 -*-
"""
Translate docutils node organization formatting.
each organization start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "organization"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing organization node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing organization node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
