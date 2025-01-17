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

from notion_python_sdk.pydantic.user_get_token_bot_user_response_bot import UserGetTokenBotUserResponseBot

class UserGetTokenBotUserResponse(BaseModel):
    object: typing.Optional[str] = Field(None, alias='object')

    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    avatar_url: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='avatar_url')

    type: typing.Optional[str] = Field(None, alias='type')

    bot: typing.Optional[UserGetTokenBotUserResponseBot] = Field(None, alias='bot')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
