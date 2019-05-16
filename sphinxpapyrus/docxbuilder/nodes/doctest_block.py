# -*- coding: utf-8 -*-
"""
Translate docutils node doctest_block formatting.
each doctest_block start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import DOCTEST_BLOCK
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "doctest_block"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing doctest_block node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.append(STYLES[DOCTEST_BLOCK])
    visitor.p = visitor._add_paragraph(style=visitor.p_style)
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing doctest_block node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p = None
    visitor.p_style.pop()
