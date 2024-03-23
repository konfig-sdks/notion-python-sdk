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

from notion_python_sdk.pydantic.block_update_block_by_id_response_created_by import BlockUpdateBlockByIdResponseCreatedBy
from notion_python_sdk.pydantic.block_update_block_by_id_response_heading2 import BlockUpdateBlockByIdResponseHeading2
from notion_python_sdk.pydantic.block_update_block_by_id_response_last_edited_by import BlockUpdateBlockByIdResponseLastEditedBy
from notion_python_sdk.pydantic.block_update_block_by_id_response_parent import BlockUpdateBlockByIdResponseParent

class BlockUpdateBlockByIdResponse(BaseModel):
    object: typing.Optional[str] = Field(None, alias='object')

    id: typing.Optional[str] = Field(None, alias='id')

    parent: typing.Optional[BlockUpdateBlockByIdResponseParent] = Field(None, alias='parent')

    created_time: typing.Optional[str] = Field(None, alias='created_time')

    last_edited_time: typing.Optional[str] = Field(None, alias='last_edited_time')

    created_by: typing.Optional[BlockUpdateBlockByIdResponseCreatedBy] = Field(None, alias='created_by')

    last_edited_by: typing.Optional[BlockUpdateBlockByIdResponseLastEditedBy] = Field(None, alias='last_edited_by')

    has_children: typing.Optional[bool] = Field(None, alias='has_children')

    archived: typing.Optional[bool] = Field(None, alias='archived')

    type: typing.Optional[str] = Field(None, alias='type')

    heading_2: typing.Optional[BlockUpdateBlockByIdResponseHeading2] = Field(None, alias='heading_2')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
