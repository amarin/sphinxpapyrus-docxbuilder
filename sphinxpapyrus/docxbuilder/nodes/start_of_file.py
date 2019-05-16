# -*- coding: utf-8 -*-
"""
Translate docutils node start_of_file formatting.
each start_of_file start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "start_of_file"


def visit(visitor: DocxTranslator, node: None):
    """Start processing start_of_file node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.docnames.append(node['docname'])


def depart(visitor: DocxTranslator, node: None):
    """Finish processing start_of_file node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.docnames.pop()
