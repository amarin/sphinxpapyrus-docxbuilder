# -*- coding: utf-8 -*-
"""
Translate docutils node productionlist formatting.
each productionlist start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "productionlist"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing productionlist node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing productionlist node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
