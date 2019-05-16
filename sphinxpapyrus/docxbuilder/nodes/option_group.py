# -*- coding: utf-8 -*-
"""
Translate docutils node option_group formatting.
each option_group start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "option_group"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing option_group node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    row = visitor.tables[-1][1]
    col = visitor.tables[-1][2]
    table = visitor.tables[-1][0]
    cell = table.cell(row, col)
    visitor.p_parents.append(cell)
    visitor.p = cell.paragraphs[0]
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing option_group node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p = None
    visitor.p_parents.pop()
    visitor.tables[-1][2] += 1
