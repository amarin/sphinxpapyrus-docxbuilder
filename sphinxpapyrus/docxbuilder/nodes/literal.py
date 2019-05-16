# -*- coding: utf-8 -*-
"""
Translate docutils node literal formatting.
each literal start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import LITERAL
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "literal"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing literal node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = STYLES[LITERAL]
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing literal node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = None
