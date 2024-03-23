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


class RequiredCommentCreateNewRequest(TypedDict):
    # A [rich text object](ref:rich-text)
    rich_text: str

class OptionalCommentCreateNewRequest(TypedDict, total=False):
    # A [page parent](/reference/database#page-parent). Either this or a discussion_id is required (not both)
    parent: str

    # A UUID identifier for a discussion thread. Either this or a parent object is required (not both)
    discussion_id: str

class CommentCreateNewRequest(RequiredCommentCreateNewRequest, OptionalCommentCreateNewRequest):
    pass
