# encoding: utf-8
"""
    sphinxpapyrus.docxwriter.writer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Custom docutils writer for docx.

    :copyright: Copyright 2018 by nakandev.
    :license: MIT, see LICENSE for details.
"""

import os

from docutils.writers import Writer

from docx import Document as DocumentLoader
from docx.document import Document
from sphinx.builders import Builder

from sphinxpapyrus.docxbuilder.utils import package_dir

from sphinx.util.console import bold
from sphinx.util import logging
logger = logging.getLogger(__name__)


class DocxWriter(Writer):
    """Writer class"""
    supported = ('docx',)
    settings_spec = ('No options here.', '', ())
    settings_defaults = {}

    output = None

    def __init__(self, builder):
        assert isinstance(builder, Builder)
        super(Writer, self).__init__()

        self.builder = builder

        style_file = builder.config.docx_style
        if style_file:
            style_dir = self.builder.srcdir
            style_full_path = os.path.join(style_dir, style_file)

        else:
            style_dir = os.path.join(package_dir, 'templates')
            style_full_path = os.path.join(style_dir, 'style.docx')

        self.docx = DocumentLoader(style_full_path)
        assert isinstance(self.docx, Document)
        self._set_coreproperties()
        self.docx._body.clear_content()

    def _set_coreproperties(self):
        """Set core properties of DocX document"""
        new_core_properties = self.builder.config.docx_coreproperties
        for name, value in new_core_properties.items():
            setattr(self.docx.core_properties, name, value)

    def translate(self):
        """Call translate """
        logger.info(bold('prepare translator'))
        visitor = self.builder.create_translator(
            self.document,
            self.builder,
            self.docx
        )
        logger.info(bold("translate nodes ..."))
        self.document.walkabout(visitor)

        assert isinstance(self.docx, Document)
        self.output = self.docx._body

    def save(self, filename):
        """Actual save for docx file"""
        self.docx.save(filename)
