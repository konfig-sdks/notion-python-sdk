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

from notion_python_sdk.pydantic.page_get_page_response_properties_name_title_item_annotations import PageGetPageResponsePropertiesNameTitleItemAnnotations
from notion_python_sdk.pydantic.page_get_page_response_properties_name_title_item_text import PageGetPageResponsePropertiesNameTitleItemText

class PageGetPageResponsePropertiesNameTitleItem(BaseModel):
    type: typing.Optional[str] = Field(None, alias='type')

    text: typing.Optional[PageGetPageResponsePropertiesNameTitleItemText] = Field(None, alias='text')

    annotations: typing.Optional[PageGetPageResponsePropertiesNameTitleItemAnnotations] = Field(None, alias='annotations')

    plain_text: typing.Optional[str] = Field(None, alias='plain_text')

    href: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='href')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )