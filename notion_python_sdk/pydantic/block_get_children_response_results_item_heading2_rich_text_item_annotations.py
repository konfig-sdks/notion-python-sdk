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


class BlockGetChildrenResponseResultsItemHeading2RichTextItemAnnotations(BaseModel):
    bold: typing.Optional[bool] = Field(None, alias='bold')

    italic: typing.Optional[bool] = Field(None, alias='italic')

    strikethrough: typing.Optional[bool] = Field(None, alias='strikethrough')

    underline: typing.Optional[bool] = Field(None, alias='underline')

    code: typing.Optional[bool] = Field(None, alias='code')

    color: typing.Optional[str] = Field(None, alias='color')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
