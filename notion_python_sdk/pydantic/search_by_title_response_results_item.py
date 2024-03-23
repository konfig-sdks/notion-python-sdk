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

from notion_python_sdk.pydantic.search_by_title_response_results_item_cover import SearchByTitleResponseResultsItemCover
from notion_python_sdk.pydantic.search_by_title_response_results_item_created_by import SearchByTitleResponseResultsItemCreatedBy
from notion_python_sdk.pydantic.search_by_title_response_results_item_icon import SearchByTitleResponseResultsItemIcon
from notion_python_sdk.pydantic.search_by_title_response_results_item_last_edited_by import SearchByTitleResponseResultsItemLastEditedBy
from notion_python_sdk.pydantic.search_by_title_response_results_item_parent import SearchByTitleResponseResultsItemParent
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties import SearchByTitleResponseResultsItemProperties

class SearchByTitleResponseResultsItem(BaseModel):
    object: typing.Optional[str] = Field(None, alias='object')

    id: typing.Optional[str] = Field(None, alias='id')

    created_time: typing.Optional[str] = Field(None, alias='created_time')

    last_edited_time: typing.Optional[str] = Field(None, alias='last_edited_time')

    created_by: typing.Optional[SearchByTitleResponseResultsItemCreatedBy] = Field(None, alias='created_by')

    last_edited_by: typing.Optional[SearchByTitleResponseResultsItemLastEditedBy] = Field(None, alias='last_edited_by')

    cover: typing.Optional[SearchByTitleResponseResultsItemCover] = Field(None, alias='cover')

    icon: typing.Optional[SearchByTitleResponseResultsItemIcon] = Field(None, alias='icon')

    parent: typing.Optional[SearchByTitleResponseResultsItemParent] = Field(None, alias='parent')

    archived: typing.Optional[bool] = Field(None, alias='archived')

    properties: typing.Optional[SearchByTitleResponseResultsItemProperties] = Field(None, alias='properties')

    url: typing.Optional[str] = Field(None, alias='url')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )