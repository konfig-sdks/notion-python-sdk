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


class BlockGetChildrenResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            object = schemas.StrSchema
        
            @staticmethod
            def results() -> typing.Type['BlockGetChildrenResponseResults']:
                return BlockGetChildrenResponseResults
            next_cursor = schemas.AnyTypeSchema
            has_more = schemas.BoolSchema
            type = schemas.StrSchema
            block = schemas.DictSchema
            __annotations__ = {
                "object": object,
                "results": results,
                "next_cursor": next_cursor,
                "has_more": has_more,
                "type": type,
                "block": block,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["results"]) -> 'BlockGetChildrenResponseResults': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_cursor"]) -> MetaOapg.properties.next_cursor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_more"]) -> MetaOapg.properties.has_more: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block"]) -> MetaOapg.properties.block: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["object", "results", "next_cursor", "has_more", "type", "block", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["results"]) -> typing.Union['BlockGetChildrenResponseResults', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_cursor"]) -> typing.Union[MetaOapg.properties.next_cursor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_more"]) -> typing.Union[MetaOapg.properties.has_more, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block"]) -> typing.Union[MetaOapg.properties.block, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["object", "results", "next_cursor", "has_more", "type", "block", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
        results: typing.Union['BlockGetChildrenResponseResults', schemas.Unset] = schemas.unset,
        next_cursor: typing.Union[MetaOapg.properties.next_cursor, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        has_more: typing.Union[MetaOapg.properties.has_more, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        block: typing.Union[MetaOapg.properties.block, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BlockGetChildrenResponse':
        return super().__new__(
            cls,
            *args,
            object=object,
            results=results,
            next_cursor=next_cursor,
            has_more=has_more,
            type=type,
            block=block,
            _configuration=_configuration,
            **kwargs,
        )

from notion_python_sdk.model.block_get_children_response_results import BlockGetChildrenResponseResults
