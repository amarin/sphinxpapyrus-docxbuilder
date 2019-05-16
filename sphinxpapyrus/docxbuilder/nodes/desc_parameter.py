# -*- coding: utf-8 -*-
"""
Translate docutils node desc_parameter formatting.
each desc_parameter start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "desc_parameter"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing desc_parameter node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing desc_parameter node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
