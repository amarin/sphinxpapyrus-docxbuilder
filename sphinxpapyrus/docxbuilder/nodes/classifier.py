# -*- coding: utf-8 -*-
"""
Translate docutils node classifier formatting.
each classifier start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "classifier"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing classifier node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing classifier node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
