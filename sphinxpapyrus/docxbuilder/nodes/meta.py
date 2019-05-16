# -*- coding: utf-8 -*-
"""
Translate docutils node meta formatting.
each meta start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "meta"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing meta node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    # only valid for HTML ?
    # TODO: check if some meta can be saved in docx document metadata
    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing meta node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
