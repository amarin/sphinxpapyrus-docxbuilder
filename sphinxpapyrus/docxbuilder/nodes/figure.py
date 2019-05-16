# -*- coding: utf-8 -*-
"""
Translate docutils node figure formatting.
each figure start will processed with visit() and finished with depart()
"""

from docutils.nodes import Node
from docx.enum.table import WD_TABLE_ALIGNMENT

from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "figure"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing figure node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p = visitor._add_paragraph()
    visitor.p.alignment = WD_TABLE_ALIGNMENT.CENTER
    visitor.p.paragraph_format.keep_with_next = True
    visitor.r = visitor.p.add_run()
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing figure node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r = None
    visitor.p = None
