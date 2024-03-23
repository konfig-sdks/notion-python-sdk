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

from notion_python_sdk.type.block_get_details_response_created_by import BlockGetDetailsResponseCreatedBy
from notion_python_sdk.type.block_get_details_response_heading2 import BlockGetDetailsResponseHeading2
from notion_python_sdk.type.block_get_details_response_last_edited_by import BlockGetDetailsResponseLastEditedBy
from notion_python_sdk.type.block_get_details_response_parent import BlockGetDetailsResponseParent

class RequiredBlockGetDetailsResponse(TypedDict):
    pass

class OptionalBlockGetDetailsResponse(TypedDict, total=False):
    object: str

    id: str

    parent: BlockGetDetailsResponseParent

    created_time: str

    last_edited_time: str

    created_by: BlockGetDetailsResponseCreatedBy

    last_edited_by: BlockGetDetailsResponseLastEditedBy

    has_children: bool

    archived: bool

    type: str

    heading_2: BlockGetDetailsResponseHeading2

class BlockGetDetailsResponse(RequiredBlockGetDetailsResponse, OptionalBlockGetDetailsResponse):
    pass