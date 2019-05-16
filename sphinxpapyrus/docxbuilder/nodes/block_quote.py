# -*- coding: utf-8 -*-
"""
Translate docutils node block_quote formatting.
each block_quote start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import BLOCK_QUOTE
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "block_quote"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing block_quote node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.append(STYLES[BLOCK_QUOTE])
    visitor.p_level += 1
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing block_quote node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.pop()
    visitor.p_level -= 1
