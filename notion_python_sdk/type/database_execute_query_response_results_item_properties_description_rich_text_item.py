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

from notion_python_sdk.type.database_execute_query_response_results_item_properties_description_rich_text_item_annotations import DatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichTextItemAnnotations
from notion_python_sdk.type.database_execute_query_response_results_item_properties_description_rich_text_item_text import DatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichTextItemText

class RequiredDatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichTextItem(TypedDict):
    pass

class OptionalDatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichTextItem(TypedDict, total=False):
    type: str

    text: DatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichTextItemText

    annotations: DatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichTextItemAnnotations

    plain_text: str

    href: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class DatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichTextItem(RequiredDatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichTextItem, OptionalDatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichTextItem):
    pass