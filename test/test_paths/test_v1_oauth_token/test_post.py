# coding: utf-8

"""
    Notion API

    Notion is a new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import notion_python_sdk
from notion_python_sdk.paths.v1_oauth_token import post
from notion_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1OauthToken(ApiTestMixin, unittest.TestCase):
    """
    V1OauthToken unit test stubs
        Create a token
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
