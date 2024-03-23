# coding: utf-8

"""
    Notion API

    Notion is a new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from notion_python_sdk.type.database_execute_query_request_sorts import DatabaseExecuteQueryRequestSorts

class RequiredDatabaseExecuteQueryRequest(TypedDict):
    pass

class OptionalDatabaseExecuteQueryRequest(TypedDict, total=False):
    # When supplied, limits which pages are returned based on the [filter conditions](ref:post-database-query-filter).
    filter: str

    sorts: DatabaseExecuteQueryRequestSorts

    # When supplied, returns a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.
    start_cursor: str

    # The number of items from the full list desired in the response. Maximum: 100
    page_size: int

class DatabaseExecuteQueryRequest(RequiredDatabaseExecuteQueryRequest, OptionalDatabaseExecuteQueryRequest):
    pass