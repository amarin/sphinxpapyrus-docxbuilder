# -*- coding: utf-8 -*-
"""
Translate docutils node citation_reference formatting.
each citation_reference start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "citation_reference"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing citation_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing citation_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
