# -*- coding: utf-8 -*-
"""
Translate docutils node desc_name formatting.
each desc_name start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import STRONG
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "desc_name"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing desc_name node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r = visitor.p.add_run()
    visitor.r_style = STYLES[STRONG]


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing desc_name node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r = None
    visitor.r_style = None
