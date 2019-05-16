# -*- coding: utf-8 -*-
"""
Translate docutils node warning formatting.
each warning start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import INTENCE_QUOTE
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "warning"


def visit(visitor: DocxTranslator, node: None):
    """Start processing warning node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.append(STYLES[INTENCE_QUOTE])
    visitor.p_level += 1
    

def depart(visitor: DocxTranslator, node: None):
    """Finish processing warning node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_style.pop()
    visitor.p_level -= 1
