# -*- coding: utf-8 -*-
"""
Translate docutils node contact formatting.
each contact start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "contact"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing contact node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing contact node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
