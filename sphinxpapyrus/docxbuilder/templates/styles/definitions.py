# -*- coding: utf-8 -*-
from sphinxpapyrus.docxbuilder.templates.styles.names import BLOCK_QUOTE
from sphinxpapyrus.docxbuilder.templates.styles.names import BULLET_LIST
from sphinxpapyrus.docxbuilder.templates.styles.names import CODE_BLOCK_CAPTION
from sphinxpapyrus.docxbuilder.templates.styles.names import DEFINITION_LIST
from sphinxpapyrus.docxbuilder.templates.styles.names import \
    DEFINITION_LIST_ITEM
from sphinxpapyrus.docxbuilder.templates.styles.names import DOCTEST_BLOCK
from sphinxpapyrus.docxbuilder.templates.styles.names import EMPHASIS
from sphinxpapyrus.docxbuilder.templates.styles.names import EMPTY_BULLET_LIST
from sphinxpapyrus.docxbuilder.templates.styles.names import ENUMERATED_LIST
from sphinxpapyrus.docxbuilder.templates.styles.names import FIELD_LIST
from sphinxpapyrus.docxbuilder.templates.styles.names import FIELD_LIST_ITEM
from sphinxpapyrus.docxbuilder.templates.styles.names import FOOTNOTE_REFERENCE
from sphinxpapyrus.docxbuilder.templates.styles.names import HEADING1
from sphinxpapyrus.docxbuilder.templates.styles.names import HEADING2
from sphinxpapyrus.docxbuilder.templates.styles.names import HEADING3
from sphinxpapyrus.docxbuilder.templates.styles.names import HEADING4
from sphinxpapyrus.docxbuilder.templates.styles.names import HEADING5
from sphinxpapyrus.docxbuilder.templates.styles.names import HEADING6
from sphinxpapyrus.docxbuilder.templates.styles.names import IMAGE_CAPTION
from sphinxpapyrus.docxbuilder.templates.styles.names import INTENCE_QUOTE
from sphinxpapyrus.docxbuilder.templates.styles.names import LINE_BLOCK
from sphinxpapyrus.docxbuilder.templates.styles.names import LITERAL
from sphinxpapyrus.docxbuilder.templates.styles.names import LITERAL_BLOCK
from sphinxpapyrus.docxbuilder.templates.styles.names import LITERAL_EMPHASIS
from sphinxpapyrus.docxbuilder.templates.styles.names import OPTION_LIST
from sphinxpapyrus.docxbuilder.templates.styles.names import OPTION_LIST_ITEM
from sphinxpapyrus.docxbuilder.templates.styles.names import REFERENCE
from sphinxpapyrus.docxbuilder.templates.styles.names import STRONG
from sphinxpapyrus.docxbuilder.templates.styles.names import SUBSCRIPT
from sphinxpapyrus.docxbuilder.templates.styles.names import SUBTITLE
from sphinxpapyrus.docxbuilder.templates.styles.names import SUPERSCRIPT
from sphinxpapyrus.docxbuilder.templates.styles.names import TABLE_CAPTION
from sphinxpapyrus.docxbuilder.templates.styles.names import TABLE_LIST
from sphinxpapyrus.docxbuilder.templates.styles.names import TABLE_NORMAL
from sphinxpapyrus.docxbuilder.templates.styles.names import TITLE
from sphinxpapyrus.docxbuilder.templates.styles.names import TITLE_REFERENCE
from sphinxpapyrus.docxbuilder.templates.styles.names import TRANSITION
from sphinxpapyrus.docxbuilder.utils import StylesEnum

STYLES = {
    # paragraph styles
    TITLE: 'Title',
    SUBTITLE: 'Subtitle',
    HEADING1:  'Heading 1',
    HEADING2:  'Heading 2',
    HEADING3:  'Heading 3',
    HEADING4:  'Heading 4',
    HEADING5:  'Heading 5',
    HEADING6:  'Heading 6',
    BULLET_LIST:  'Bullet List',
    ENUMERATED_LIST:  'Enumerated List',
    EMPTY_BULLET_LIST:  'Empty Bullet List',
    DEFINITION_LIST:  'Definition List',
    DEFINITION_LIST_ITEM:  'Definition List Item',
    FIELD_LIST:  'Field List',
    FIELD_LIST_ITEM:  'Field List Item',
    OPTION_LIST:  'Option List',
    OPTION_LIST_ITEM:  'Option List Item',
    LITERAL_BLOCK:  'Literal Block',
    BLOCK_QUOTE:  'Quote',
    LINE_BLOCK:  'Line Block',
    DOCTEST_BLOCK:  'Doctest Block',
    TRANSITION:  'Horizontal Line',
    TABLE_CAPTION:  'Caption',
    IMAGE_CAPTION:  'Caption',
    CODE_BLOCK_CAPTION:  'Code Block Caption',
    # character styles
    STRONG:  'Strong',
    EMPHASIS:  'Emphasis',
    LITERAL_EMPHASIS:  'Literal Emphasis',
    SUBSCRIPT:  'Subscript',
    SUPERSCRIPT:  'Superscript',
    TITLE_REFERENCE:  'Book Title',
    LITERAL:  'Literal',
    REFERENCE:  'Hyperlink',
    FOOTNOTE_REFERENCE:  'Default Paragraph Font',
    # table styles
    TABLE_NORMAL:  'Sphinx Table Normal',
    TABLE_LIST: 'Sphinx Table List',
    INTENCE_QUOTE:  'Intense Quote',
}
