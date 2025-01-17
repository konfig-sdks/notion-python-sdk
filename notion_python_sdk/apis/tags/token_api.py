# coding: utf-8

"""
    Notion API

    Notion is a new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from notion_python_sdk.paths.v1_oauth_token.post import GenerateAccess
from notion_python_sdk.apis.tags.token_api_raw import TokenApiRaw


class TokenApi(
    GenerateAccess,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TokenApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TokenApiRaw(api_client)
