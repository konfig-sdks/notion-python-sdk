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

from notion_python_sdk.type.block_append_children_response_results_item_heading2_rich_text import BlockAppendChildrenResponseResultsItemHeading2RichText

class RequiredBlockAppendChildrenResponseResultsItemHeading2(TypedDict):
    pass

class OptionalBlockAppendChildrenResponseResultsItemHeading2(TypedDict, total=False):
    rich_text: BlockAppendChildrenResponseResultsItemHeading2RichText

    color: str

    is_toggleable: bool

class BlockAppendChildrenResponseResultsItemHeading2(RequiredBlockAppendChildrenResponseResultsItemHeading2, OptionalBlockAppendChildrenResponseResultsItemHeading2):
    pass
