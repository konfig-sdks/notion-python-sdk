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


class RequiredPageGetPageResponsePropertiesDescriptionRichTextItemAnnotations(TypedDict):
    pass

class OptionalPageGetPageResponsePropertiesDescriptionRichTextItemAnnotations(TypedDict, total=False):
    bold: bool

    italic: bool

    strikethrough: bool

    underline: bool

    code: bool

    color: str

class PageGetPageResponsePropertiesDescriptionRichTextItemAnnotations(RequiredPageGetPageResponsePropertiesDescriptionRichTextItemAnnotations, OptionalPageGetPageResponsePropertiesDescriptionRichTextItemAnnotations):
    pass
