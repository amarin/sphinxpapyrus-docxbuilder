# -*- coding: utf-8 -*-
"""
Translate docutils node desc_parameterlist formatting.
each desc_parameterlist start will processed with visit()
and finished with depart()
"""
from docutils.nodes import Element
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

node_name = "desc_parameterlist"


def visit(visitor: DocxTranslator, node: Element):
    """Start processing desc_parameterlist node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Element)

    params = [child.astext() for child in node.children]
    text = '(' + ', '.join(params) + ')'
    visitor.r = visitor.p.add_run(text)


def depart(visitor: DocxTranslator, node: Element):
    """Finish processing desc_parameterlist node"""
    assert isinstance(visitor, DocxTranslator)
    assert isinstance(node, Element)

    visitor.r = None
