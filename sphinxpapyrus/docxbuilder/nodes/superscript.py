# -*- coding: utf-8 -*-
"""
Translate docutils node superscript formatting.
each superscript start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import SUPERSCRIPT
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "superscript"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing superscript node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = STYLES[SUPERSCRIPT]
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing superscript node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = None
