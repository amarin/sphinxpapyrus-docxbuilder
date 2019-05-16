# -*- coding: utf-8 -*-
"""
Translate docutils node strong formatting.
each strong start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import STRONG
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "strong"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing strong node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = STYLES[STRONG]


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing strong node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = None
