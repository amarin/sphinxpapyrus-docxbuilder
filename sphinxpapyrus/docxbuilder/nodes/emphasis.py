# -*- coding: utf-8 -*-
"""
Translate docutils node emphasis formatting.
each emphasis start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import EMPHASIS
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "emphasis"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing emphasis node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = STYLES[EMPHASIS]
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing emphasis node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = None
