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

from notion_python_sdk.type.page_update_properties_response_cover import PageUpdatePropertiesResponseCover
from notion_python_sdk.type.page_update_properties_response_created_by import PageUpdatePropertiesResponseCreatedBy
from notion_python_sdk.type.page_update_properties_response_icon import PageUpdatePropertiesResponseIcon
from notion_python_sdk.type.page_update_properties_response_last_edited_by import PageUpdatePropertiesResponseLastEditedBy
from notion_python_sdk.type.page_update_properties_response_parent import PageUpdatePropertiesResponseParent
from notion_python_sdk.type.page_update_properties_response_properties import PageUpdatePropertiesResponseProperties

class RequiredPageUpdatePropertiesResponse(TypedDict):
    pass

class OptionalPageUpdatePropertiesResponse(TypedDict, total=False):
    object: str

    id: str

    created_time: str

    last_edited_time: str

    created_by: PageUpdatePropertiesResponseCreatedBy

    last_edited_by: PageUpdatePropertiesResponseLastEditedBy

    cover: PageUpdatePropertiesResponseCover

    icon: PageUpdatePropertiesResponseIcon

    parent: PageUpdatePropertiesResponseParent

    archived: bool

    properties: PageUpdatePropertiesResponseProperties

    url: str

class PageUpdatePropertiesResponse(RequiredPageUpdatePropertiesResponse, OptionalPageUpdatePropertiesResponse):
    pass