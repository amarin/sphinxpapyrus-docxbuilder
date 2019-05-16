# -*- coding: utf-8 -*-
"""
Translate docutils node literal_block formatting.
each literal_block start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import LITERAL_BLOCK
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "literal_block"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing literal_block node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.append(STYLES[LITERAL_BLOCK])
    visitor.p = visitor._add_paragraph(style=visitor.p_style[-1])
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing literal_block node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p = None
    visitor.p_style.pop()
