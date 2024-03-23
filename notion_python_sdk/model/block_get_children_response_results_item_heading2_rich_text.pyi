# coding: utf-8

"""
    Notion API

    Notion is a new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from notion_python_sdk import schemas  # noqa: F401


class BlockGetChildrenResponseResultsItemHeading2RichText(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['BlockGetChildrenResponseResultsItemHeading2RichTextItem']:
            return BlockGetChildrenResponseResultsItemHeading2RichTextItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['BlockGetChildrenResponseResultsItemHeading2RichTextItem'], typing.List['BlockGetChildrenResponseResultsItemHeading2RichTextItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BlockGetChildrenResponseResultsItemHeading2RichText':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'BlockGetChildrenResponseResultsItemHeading2RichTextItem':
        return super().__getitem__(i)

from notion_python_sdk.model.block_get_children_response_results_item_heading2_rich_text_item import BlockGetChildrenResponseResultsItemHeading2RichTextItem
