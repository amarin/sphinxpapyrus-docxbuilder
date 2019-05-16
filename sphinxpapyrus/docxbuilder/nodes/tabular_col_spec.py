# -*- coding: utf-8 -*-
"""
Translate docutils node tabular_col_spec formatting.
each tabular_col_spec start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "tabular_col_spec"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing tabular_col_spec node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing tabular_col_spec node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
