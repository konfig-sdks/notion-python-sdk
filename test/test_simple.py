# coding: utf-8

"""
    Notion API

    Notion is a new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from notion_python_sdk import Notion

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        notion = Notion(
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(notion)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
