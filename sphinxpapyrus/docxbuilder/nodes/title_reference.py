# -*- coding: utf-8 -*-
"""
Translate docutils node title_reference formatting.
each title_reference start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import TITLE_REFERENCE
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "title_reference"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing title_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = STYLES[TITLE_REFERENCE]
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing title_reference node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r_style = None
