# -*- coding: utf-8 -*-
"""
Translate docutils node bullet_list formatting.
each bullet_list start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "bullet_list"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing bullet_list node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_level += 1
    numId = visitor._get_new_num(abstractNumId=11)
    visitor.numIds.append(numId)
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing bullet_list node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_level -= 1
    visitor.numIds.pop()
