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


class SearchByTitleRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            query = schemas.StrSchema
        
            @staticmethod
            def sort() -> typing.Type['SearchByTitleRequestSort']:
                return SearchByTitleRequestSort
        
            @staticmethod
            def filter() -> typing.Type['SearchByTitleRequestFilter']:
                return SearchByTitleRequestFilter
            start_cursor = schemas.StrSchema
            page_size = schemas.Int32Schema
            __annotations__ = {
                "query": query,
                "sort": sort,
                "filter": filter,
                "start_cursor": start_cursor,
                "page_size": page_size,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> 'SearchByTitleRequestSort': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter"]) -> 'SearchByTitleRequestFilter': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_cursor"]) -> MetaOapg.properties.start_cursor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page_size"]) -> MetaOapg.properties.page_size: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["query", "sort", "filter", "start_cursor", "page_size", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> typing.Union['SearchByTitleRequestSort', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter"]) -> typing.Union['SearchByTitleRequestFilter', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_cursor"]) -> typing.Union[MetaOapg.properties.start_cursor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page_size"]) -> typing.Union[MetaOapg.properties.page_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["query", "sort", "filter", "start_cursor", "page_size", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        query: typing.Union[MetaOapg.properties.query, str, schemas.Unset] = schemas.unset,
        sort: typing.Union['SearchByTitleRequestSort', schemas.Unset] = schemas.unset,
        filter: typing.Union['SearchByTitleRequestFilter', schemas.Unset] = schemas.unset,
        start_cursor: typing.Union[MetaOapg.properties.start_cursor, str, schemas.Unset] = schemas.unset,
        page_size: typing.Union[MetaOapg.properties.page_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SearchByTitleRequest':
        return super().__new__(
            cls,
            *args,
            query=query,
            sort=sort,
            filter=filter,
            start_cursor=start_cursor,
            page_size=page_size,
            _configuration=_configuration,
            **kwargs,
        )

from notion_python_sdk.model.search_by_title_request_filter import SearchByTitleRequestFilter
from notion_python_sdk.model.search_by_title_request_sort import SearchByTitleRequestSort
