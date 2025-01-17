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

from notion_python_sdk.type.block_append_children_response_results_item_created_by import BlockAppendChildrenResponseResultsItemCreatedBy
from notion_python_sdk.type.block_append_children_response_results_item_heading2 import BlockAppendChildrenResponseResultsItemHeading2
from notion_python_sdk.type.block_append_children_response_results_item_last_edited_by import BlockAppendChildrenResponseResultsItemLastEditedBy
from notion_python_sdk.type.block_append_children_response_results_item_parent import BlockAppendChildrenResponseResultsItemParent

class RequiredBlockAppendChildrenResponseResultsItem(TypedDict):
    pass

class OptionalBlockAppendChildrenResponseResultsItem(TypedDict, total=False):
    object: str

    id: str

    parent: BlockAppendChildrenResponseResultsItemParent

    created_time: str

    last_edited_time: str

    created_by: BlockAppendChildrenResponseResultsItemCreatedBy

    last_edited_by: BlockAppendChildrenResponseResultsItemLastEditedBy

    has_children: bool

    archived: bool

    type: str

    heading_2: BlockAppendChildrenResponseResultsItemHeading2

class BlockAppendChildrenResponseResultsItem(RequiredBlockAppendChildrenResponseResultsItem, OptionalBlockAppendChildrenResponseResultsItem):
    pass
