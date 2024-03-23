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


class PageUpdatePropertiesRequest(BaseModel):
    # The property values to update for the page. The keys are the names or IDs of the property and the values are property values. If a page property ID is not included, then it is not changed.
    properties: typing.Optional[str] = Field(None, alias='properties')

    # Whether the page is archived (deleted). Set to true to archive a page. Set to false to un-archive (restore) a page.
    archived: typing.Optional[bool] = Field(None, alias='archived')

    # A page icon for the page. Supported types are [external file object](https://developers.notion.com/reference/file-object) or [emoji object](https://developers.notion.com/reference/emoji-object).
    icon: typing.Optional[str] = Field(None, alias='icon')

    # A cover image for the page. Only [external file objects](https://developers.notion.com/reference/file-object) are supported.
    cover: typing.Optional[str] = Field(None, alias='cover')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )