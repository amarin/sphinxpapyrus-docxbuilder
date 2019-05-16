# -*- coding: utf-8 -*-
import os

from sphinx.util import logging

package_dir = os.path.abspath(os.path.dirname(__file__))
logger = logging.getLogger(__name__)


class StylesEnum(object):
    """Simple Enum-like object with attributes defined from dict"""

    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items()]
