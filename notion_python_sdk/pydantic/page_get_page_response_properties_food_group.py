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

from notion_python_sdk.pydantic.page_get_page_response_properties_food_group_select import PageGetPageResponsePropertiesFoodGroupSelect

class PageGetPageResponsePropertiesFoodGroup(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    type: typing.Optional[str] = Field(None, alias='type')

    select: typing.Optional[PageGetPageResponsePropertiesFoodGroupSelect] = Field(None, alias='select')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
