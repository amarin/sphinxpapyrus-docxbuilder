# -*- coding: utf-8 -*-
from docx.oxml.xmlchemy import BaseOxmlElement
from docx.oxml.xmlchemy import ZeroOrOne

# monkey patch
from docx.oxml import register_element_cls


class CT_TrPr(BaseOxmlElement):
    tblHeader = ZeroOrOne('w:tblHeader')


register_element_cls('w:trPr', CT_TrPr)



