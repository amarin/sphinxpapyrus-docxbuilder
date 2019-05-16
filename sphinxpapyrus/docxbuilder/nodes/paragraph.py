# -*- coding: utf-8 -*-
"""
Translate docutils node paragraph formatting.
each paragraph start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "paragraph"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing paragraph node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    if not visitor.p:
        visitor.p = visitor._add_paragraph(style=visitor.p_style)

    if isinstance(node.parent, nodes.list_item):
        if visitor.is_first_list_item:
            visitor._multilevel_list_numbering(
                visitor.p,
                visitor.p_level - 1,
                visitor.numIds[-1]
            )
        else:
            visitor._multilevel_list_numbering(
                visitor.p,
                visitor.p_level - 1,
                15
            )
        visitor.is_first_list_item = False
    visitor.r = visitor.p.add_run()
    

def depart(visitor: DocxTranslator, node: Node):
    """Finish processing paragraph node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.r = None
    visitor.p = None
