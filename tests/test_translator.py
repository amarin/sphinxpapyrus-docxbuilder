# -*- coding: utf-8 -*-
from importlib import import_module
from unittest import TestCase

module_name = 'sphinxpapyrus.docxbuilder.translator'


class TestTranslator(TestCase):
    f"""Test module {module_name}"""

    def test_00_import(self):
        f"""Check if module {module_name} is importable"""
        try:
            imported_module = import_module(module_name)
        except Exception as exc:
            self.fail(f"Cant import {module_name}: {exc}")
