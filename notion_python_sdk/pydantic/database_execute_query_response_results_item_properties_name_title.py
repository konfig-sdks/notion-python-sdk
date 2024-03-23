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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_name_title_item import DatabaseExecuteQueryResponseResultsItemPropertiesNameTitleItem

DatabaseExecuteQueryResponseResultsItemPropertiesNameTitle = typing.List[DatabaseExecuteQueryResponseResultsItemPropertiesNameTitleItem]
