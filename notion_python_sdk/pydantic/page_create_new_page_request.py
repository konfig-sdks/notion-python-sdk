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

from notion_python_sdk.pydantic.page_create_new_page_request_children import PageCreateNewPageRequestChildren

class PageCreateNewPageRequest(BaseModel):
    # The parent page or database where the new page is inserted, represented as a JSON object with a `page_id` or `database_id` key, and the corresponding ID.
    parent: str = Field(alias='parent')

    # The values of the page’s properties. If the `parent` is a database, then the schema must match the parent database’s properties. If the `parent` is a page, then the only valid object key is `title`.
    properties: str = Field(alias='properties')

    children: typing.Optional[PageCreateNewPageRequestChildren] = Field(None, alias='children')

    # The icon of the new page. Either an [emoji object](https://developers.notion.com/reference/emoji-object) or an [external file object](https://developers.notion.com/reference/file-object)..
    icon: typing.Optional[str] = Field(None, alias='icon')

    # The cover image of the new page, represented as a [file object](https://developers.notion.com/reference/file-object).
    cover: typing.Optional[str] = Field(None, alias='cover')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
