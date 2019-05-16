# -*- coding: utf-8 -*-
"""
Translate docutils node option_list formatting.
each option_list start will processed with visit() and finished with depart()
"""
from docutils.nodes import Element
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "option_list"


def visit(visitor: DocxTranslator, node: Element):
    """Start processing option_list node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Element)

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
    """Finish processing option_list node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.tables.pop()
