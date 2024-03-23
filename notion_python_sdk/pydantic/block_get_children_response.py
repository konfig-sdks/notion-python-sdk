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

from notion_python_sdk.pydantic.block_get_children_response_results import BlockGetChildrenResponseResults

class BlockGetChildrenResponse(BaseModel):
    object: typing.Optional[str] = Field(None, alias='object')

    results: typing.Optional[BlockGetChildrenResponseResults] = Field(None, alias='results')

    next_cursor: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='next_cursor')

    has_more: typing.Optional[bool] = Field(None, alias='has_more')

    type: typing.Optional[str] = Field(None, alias='type')

    block: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='block')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
