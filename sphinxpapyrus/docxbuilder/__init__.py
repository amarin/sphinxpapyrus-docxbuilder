# -*- coding: utf-8 -*-
"""
    sphinxpapyrus.docxbuilder
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A Sphinx extension for Word (.docx) file output.

    :copyright: Copyright 2018 by nakandev.
    :license: MIT, see LICENSE for details.
"""
from sphinx.application import Sphinx

__version__ = '0.1.0'


def setup(app):
    """Setup docxbuilder as Sphinx plugin"""
    assert isinstance(app, Sphinx)
    from sphinxpapyrus.docxbuilder.builder import DocxBuilder
    app.add_builder(DocxBuilder)

    app.add_config_value('docx_documents', [], 'env')
    app.add_config_value('docx_style', None, 'env')
    app.add_config_value('docx_coreproperties', {}, 'env')
    app.add_config_value('docx_pagebreak_level', None, 'env')
    app.add_config_value('docx_imagetable_align', None, 'env')

    return {
        'version': 'builtin',
        'parallel_read_safe': False,
        'parallel_write_safe': False,
    }
