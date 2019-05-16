# -*- coding: utf-8 -*-
"""
Translate docutils node transition formatting.
each transition start will processed with visit() and finished with depart()
"""
from docutils import nodes
from docutils.nodes import Node

from sphinxpapyrus.docxbuilder.templates.styles.definitions import STYLES
from sphinxpapyrus.docxbuilder.templates.styles.names import TRANSITION
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "transition"


def visit(visitor: DocxTranslator, node: Node):
    """Start processing transition node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)

    # TODO: change from style to image
    visitor.docx.add_paragraph('', style=STYLES[TRANSITION])
    visitor.p = None
    raise nodes.SkipNode


def depart(visitor: DocxTranslator, node: Node):
    """Finish processing transition node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Node)
