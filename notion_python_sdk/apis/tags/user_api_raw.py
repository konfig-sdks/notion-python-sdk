# coding: utf-8

"""
    Notion API

    Notion is a new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from notion_python_sdk.paths.v1_users_me.get import GetTokenBotUserRaw
from notion_python_sdk.paths.v1_users_user_id.get import GetUserByIdRaw
from notion_python_sdk.paths.v1_users.get import ListAllUsersRaw


class UserApiRaw(
    GetTokenBotUserRaw,
    GetUserByIdRaw,
    ListAllUsersRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
