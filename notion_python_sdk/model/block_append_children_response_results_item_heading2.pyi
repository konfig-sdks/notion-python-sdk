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


class BlockAppendChildrenResponseResultsItemHeading2(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def rich_text() -> typing.Type['BlockAppendChildrenResponseResultsItemHeading2RichText']:
                return BlockAppendChildrenResponseResultsItemHeading2RichText
            color = schemas.StrSchema
            is_toggleable = schemas.BoolSchema
            __annotations__ = {
                "rich_text": rich_text,
                "color": color,
                "is_toggleable": is_toggleable,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rich_text"]) -> 'BlockAppendChildrenResponseResultsItemHeading2RichText': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_toggleable"]) -> MetaOapg.properties.is_toggleable: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["rich_text", "color", "is_toggleable", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rich_text"]) -> typing.Union['BlockAppendChildrenResponseResultsItemHeading2RichText', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_toggleable"]) -> typing.Union[MetaOapg.properties.is_toggleable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rich_text", "color", "is_toggleable", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        rich_text: typing.Union['BlockAppendChildrenResponseResultsItemHeading2RichText', schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        is_toggleable: typing.Union[MetaOapg.properties.is_toggleable, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BlockAppendChildrenResponseResultsItemHeading2':
        return super().__new__(
            cls,
            *args,
            rich_text=rich_text,
            color=color,
            is_toggleable=is_toggleable,
            _configuration=_configuration,
            **kwargs,
        )

from notion_python_sdk.model.block_append_children_response_results_item_heading2_rich_text import BlockAppendChildrenResponseResultsItemHeading2RichText
