# -*- coding: utf-8 -*-
"""
Translate docutils node caption formatting.
each caption start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node
from docx.enum.table import WD_TABLE_ALIGNMENT

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import CODE_BLOCK_CAPTION
from sphinxpapyrus.docxbuilder.templates.styles.names import IMAGE_CAPTION
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "caption"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing caption node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    prefix = visitor._fignum_prefix(node.parent)
    if isinstance(node.parent, nodes.figure):
        visitor.p = visitor._add_paragraph(
            prefix + u' ',
            style=STYLES[IMAGE_CAPTION]
        )
        visitor.p.alignment = WD_TABLE_ALIGNMENT.CENTER

    elif isinstance(node.parent, nodes.container):
        visitor.p = visitor._add_paragraph(
            prefix + u' ',
            style=STYLES[CODE_BLOCK_CAPTION]
        )
        visitor.p.paragraph_format.keep_with_next = True
        pass


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing caption node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    visitor.p = None
