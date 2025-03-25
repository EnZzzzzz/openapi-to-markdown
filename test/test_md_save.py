from unittest import TestCase
import unittest

from openapi_markdown.openapi import *


class TestMdSave(TestCase):

    def test_header_level_1(self):
        content = Header("title", 1).export()
        self.assertEqual(content, "# title\n\n")

    def test_header_level_2(self):
        content = Header("title", 2).export()
        self.assertEqual(content, "## title\n\n")

    def test_content_bold(self):
        content = Content("content", bold=True).export()
        self.assertEqual(content, "**content**")


if __name__ == '__main__':
    # python -m unittest test_md_save.py
    unittest.main()
