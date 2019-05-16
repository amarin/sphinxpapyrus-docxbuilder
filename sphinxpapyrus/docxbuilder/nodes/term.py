# -*- coding: utf-8 -*-
"""
Translate docutils node term formatting.
each term start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import DEFINITION_LIST
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "term"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing term node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.append(STYLES[DEFINITION_LIST])
    visitor.p = visitor._add_paragraph(style=visitor.p_style[-1])


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing term node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p = None
    visitor.p_style.pop()
