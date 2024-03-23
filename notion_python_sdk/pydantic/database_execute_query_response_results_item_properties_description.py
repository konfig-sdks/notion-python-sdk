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

from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_description_rich_text import DatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichText

class DatabaseExecuteQueryResponseResultsItemPropertiesDescription(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    type: typing.Optional[str] = Field(None, alias='type')

    rich_text: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesDescriptionRichText] = Field(None, alias='rich_text')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
