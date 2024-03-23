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

from notion_python_sdk.type.block_update_block_by_id_response_heading2_rich_text_item_annotations import BlockUpdateBlockByIdResponseHeading2RichTextItemAnnotations
from notion_python_sdk.type.block_update_block_by_id_response_heading2_rich_text_item_text import BlockUpdateBlockByIdResponseHeading2RichTextItemText

class RequiredBlockUpdateBlockByIdResponseHeading2RichTextItem(TypedDict):
    pass

class OptionalBlockUpdateBlockByIdResponseHeading2RichTextItem(TypedDict, total=False):
    type: str

    text: BlockUpdateBlockByIdResponseHeading2RichTextItemText

    annotations: BlockUpdateBlockByIdResponseHeading2RichTextItemAnnotations

    plain_text: str

    href: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class BlockUpdateBlockByIdResponseHeading2RichTextItem(RequiredBlockUpdateBlockByIdResponseHeading2RichTextItem, OptionalBlockUpdateBlockByIdResponseHeading2RichTextItem):
    pass