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

from notion_python_sdk.type.database_update_database_request_description import DatabaseUpdateDatabaseRequestDescription
from notion_python_sdk.type.database_update_database_request_title import DatabaseUpdateDatabaseRequestTitle

class RequiredDatabaseUpdateDatabaseRequest(TypedDict):
    pass

class OptionalDatabaseUpdateDatabaseRequest(TypedDict, total=False):
    title: DatabaseUpdateDatabaseRequestTitle

    description: DatabaseUpdateDatabaseRequestDescription

    # The properties of a database to be changed in the request, in the form of a JSON object. If updating an existing property, then the keys are the names or IDs of the properties as they appear in Notion, and the values are [property schema objects](ref:property-schema-object). If adding a new property, then the key is the name of the new database property and the value is a [property schema object](ref:property-schema-object).
    properties: str

class DatabaseUpdateDatabaseRequest(RequiredDatabaseUpdateDatabaseRequest, OptionalDatabaseUpdateDatabaseRequest):
    pass
