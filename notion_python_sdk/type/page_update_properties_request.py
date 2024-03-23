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


class RequiredPageUpdatePropertiesRequest(TypedDict):
    pass

class OptionalPageUpdatePropertiesRequest(TypedDict, total=False):
    # The property values to update for the page. The keys are the names or IDs of the property and the values are property values. If a page property ID is not included, then it is not changed.
    properties: str

    # Whether the page is archived (deleted). Set to true to archive a page. Set to false to un-archive (restore) a page.
    archived: bool

    # A page icon for the page. Supported types are [external file object](https://developers.notion.com/reference/file-object) or [emoji object](https://developers.notion.com/reference/emoji-object).
    icon: str

    # A cover image for the page. Only [external file objects](https://developers.notion.com/reference/file-object) are supported.
    cover: str

class PageUpdatePropertiesRequest(RequiredPageUpdatePropertiesRequest, OptionalPageUpdatePropertiesRequest):
    pass