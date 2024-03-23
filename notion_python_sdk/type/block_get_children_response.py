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

from notion_python_sdk.type.block_get_children_response_results import BlockGetChildrenResponseResults

class RequiredBlockGetChildrenResponse(TypedDict):
    pass

class OptionalBlockGetChildrenResponse(TypedDict, total=False):
    object: str

    results: BlockGetChildrenResponseResults

    next_cursor: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    has_more: bool

    type: str

    block: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class BlockGetChildrenResponse(RequiredBlockGetChildrenResponse, OptionalBlockGetChildrenResponse):
    pass