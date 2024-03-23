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

from notion_python_sdk.pydantic.comment_create_new_response_created_by import CommentCreateNewResponseCreatedBy
from notion_python_sdk.pydantic.comment_create_new_response_parent import CommentCreateNewResponseParent
from notion_python_sdk.pydantic.comment_create_new_response_rich_text import CommentCreateNewResponseRichText

class CommentCreateNewResponse(BaseModel):
    object: typing.Optional[str] = Field(None, alias='object')

    id: typing.Optional[str] = Field(None, alias='id')

    parent: typing.Optional[CommentCreateNewResponseParent] = Field(None, alias='parent')

    discussion_id: typing.Optional[str] = Field(None, alias='discussion_id')

    created_time: typing.Optional[str] = Field(None, alias='created_time')

    last_edited_time: typing.Optional[str] = Field(None, alias='last_edited_time')

    created_by: typing.Optional[CommentCreateNewResponseCreatedBy] = Field(None, alias='created_by')

    rich_text: typing.Optional[CommentCreateNewResponseRichText] = Field(None, alias='rich_text')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
