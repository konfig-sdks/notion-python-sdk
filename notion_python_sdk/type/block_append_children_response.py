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

from notion_python_sdk.type.block_append_children_response_results import BlockAppendChildrenResponseResults

class RequiredBlockAppendChildrenResponse(TypedDict):
    pass

class OptionalBlockAppendChildrenResponse(TypedDict, total=False):
    object: str

    results: BlockAppendChildrenResponseResults

    next_cursor: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    has_more: bool

    type: str

    block: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class BlockAppendChildrenResponse(RequiredBlockAppendChildrenResponse, OptionalBlockAppendChildrenResponse):
    pass
