# -*- coding: utf-8 -*-
"""
Translate docutils node raw formatting.
each raw start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "raw"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing raw node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    # TODO: support raw HTML translation
    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing raw node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
