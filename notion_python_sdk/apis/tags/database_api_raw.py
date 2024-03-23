# coding: utf-8

"""
    Notion API

    Notion is a new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from notion_python_sdk.paths.v1_databases.post import CreateNewDatabaseRaw
from notion_python_sdk.paths.v1_databases_database_id_query.post import ExecuteQueryRaw
from notion_python_sdk.paths.v1_databases_database_id.get import GetDatabaseRaw
from notion_python_sdk.paths.v1_databases_database_id.patch import UpdateDatabaseRaw


class DatabaseApiRaw(
    CreateNewDatabaseRaw,
    ExecuteQueryRaw,
    GetDatabaseRaw,
    UpdateDatabaseRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass