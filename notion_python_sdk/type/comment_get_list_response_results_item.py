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

from notion_python_sdk.type.comment_get_list_response_results_item_created_by import CommentGetListResponseResultsItemCreatedBy
from notion_python_sdk.type.comment_get_list_response_results_item_parent import CommentGetListResponseResultsItemParent
from notion_python_sdk.type.comment_get_list_response_results_item_rich_text import CommentGetListResponseResultsItemRichText

class RequiredCommentGetListResponseResultsItem(TypedDict):
    pass

class OptionalCommentGetListResponseResultsItem(TypedDict, total=False):
    object: str

    id: str

    parent: CommentGetListResponseResultsItemParent

    discussion_id: str

    created_time: str

    last_edited_time: str

    created_by: CommentGetListResponseResultsItemCreatedBy

    rich_text: CommentGetListResponseResultsItemRichText

class CommentGetListResponseResultsItem(RequiredCommentGetListResponseResultsItem, OptionalCommentGetListResponseResultsItem):
    pass