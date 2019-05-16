# -*- coding: utf-8 -*-
"""
Translate docutils node enumerated_list formatting.
each enumerated_list start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "enumerated_list"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing enumerated_list node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_level += 1
    numId = visitor._get_new_num(abstractNumId=15)
    visitor.numIds.append(numId)
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing enumerated_list node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p_level -= 1
    visitor.numIds.pop()
