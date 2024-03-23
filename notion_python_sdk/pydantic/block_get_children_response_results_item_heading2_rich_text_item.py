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

from notion_python_sdk.pydantic.block_get_children_response_results_item_heading2_rich_text_item_annotations import BlockGetChildrenResponseResultsItemHeading2RichTextItemAnnotations
from notion_python_sdk.pydantic.block_get_children_response_results_item_heading2_rich_text_item_text import BlockGetChildrenResponseResultsItemHeading2RichTextItemText

class BlockGetChildrenResponseResultsItemHeading2RichTextItem(BaseModel):
    type: typing.Optional[str] = Field(None, alias='type')

    text: typing.Optional[BlockGetChildrenResponseResultsItemHeading2RichTextItemText] = Field(None, alias='text')

    annotations: typing.Optional[BlockGetChildrenResponseResultsItemHeading2RichTextItemAnnotations] = Field(None, alias='annotations')

    plain_text: typing.Optional[str] = Field(None, alias='plain_text')

    href: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='href')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )