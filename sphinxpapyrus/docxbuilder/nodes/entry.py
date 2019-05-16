# -*- coding: utf-8 -*-
"""
Translate docutils node entry formatting.
each entry start will processed with visit() and finished with depart()
"""
from docutils.nodes import Element
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "entry"


def visit(visitor: DocxTranslator, node: Element):
    """Start processing entry node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Element)

    row = visitor.tables[-1][1]
    col = visitor.tables[-1][2]
    table = visitor.tables[-1][0]
    cell = table.cell(row, col)
    visitor.p_parents.append(cell)
    visitor.p = cell.paragraphs[0]
    if 'morerows' in node or 'morecols' in node:
        mrow = node.get('morerows', 0)
        mcol = node.get('morecols', 0)
        cell.merge(table.cell(row + mrow, col + mcol))
        

def depart(visitor: DocxTranslator, node: Element):
    """Finish processing entry node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Element)

    visitor.p_parents.pop()
    visitor.tables[-1][2] += 1
    col = visitor.tables[-1][2]
    row = visitor.tables[-1][1]
    table = visitor.tables[-1][0]
    if row > 0:
        for x in range(col + 1, len(table.rows[row].cells) - 1):
            head = table.cell(row - 1, x)
            now = table.cell(row, x)
            if head._tc != now._tc:
                break
            visitor.tables[-1][2] += 1
    col = visitor.tables[-1][2]
    for x in range(col, len(table.rows[row].cells) - 1):
        next1 = table.cell(row, x - 1)
        next2 = table.cell(row, x)
        if next1._tc != next2._tc:
            break
        visitor.tables[-1][2] += 1
