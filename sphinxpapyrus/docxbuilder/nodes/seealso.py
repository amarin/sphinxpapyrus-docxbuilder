# -*- coding: utf-8 -*-
"""
Translate docutils node seealso formatting.
each seealso start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import INTENCE_QUOTE
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "seealso"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing seealso node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.append(STYLES[INTENCE_QUOTE])
    visitor.p_level += 1


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing seealso node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.pop()
    visitor.p_level -= 1
