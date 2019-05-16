# -*- coding: utf-8 -*-
"""
Translate docutils node footnote formatting.
each footnote start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "footnote"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing footnote node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    text = node.children[0].astext().strip()
    visitor.p = visitor._add_paragraph('[%s] ' % (text))
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing footnote node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p = None
