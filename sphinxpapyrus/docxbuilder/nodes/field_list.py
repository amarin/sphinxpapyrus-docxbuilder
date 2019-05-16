# -*- coding: utf-8 -*-
"""
Translate docutils node field_list formatting.
each field_list start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "field_list"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing field_list node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor._add_paragraph_between_table(node)
    item_num = len(node.children)
    table = visitor.p_parents[-1].add_table(rows=item_num, cols=2)
    twidth = sum([cell.width for cell in table.row_cells(0)])
    for i in range(item_num):
        table.column_cells(0)[i].width = int(
            twidth * (1 - visitor.item_width_rate))
        table.column_cells(1)[i].width = int(
            twidth * (visitor.item_width_rate))
    visitor.tables.append([table, 0, 0])
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing field_list node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.tables.pop()
