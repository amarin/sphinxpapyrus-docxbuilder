# -*- coding: utf-8 -*-
"""
Translate docutils node literal_emphasis formatting.
each literal_emphasis start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import LITERAL_EMPHASIS
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "literal_emphasis"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing literal_emphasis node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = STYLES[LITERAL_EMPHASIS]


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing literal_emphasis node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = None
