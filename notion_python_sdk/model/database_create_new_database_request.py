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


class DatabaseCreateNewDatabaseRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "parent",
            "properties",
        }
        
        class properties:
            parent = schemas.StrSchema
            properties = schemas.StrSchema
        
            @staticmethod
            def title() -> typing.Type['DatabaseCreateNewDatabaseRequestTitle']:
                return DatabaseCreateNewDatabaseRequestTitle
            __annotations__ = {
                "parent": parent,
                "properties": properties,
                "title": title,
            }
    
    parent: MetaOapg.properties.parent
    properties: MetaOapg.properties.properties
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> 'DatabaseCreateNewDatabaseRequestTitle': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["parent", "properties", "title", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union['DatabaseCreateNewDatabaseRequestTitle', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parent", "properties", "title", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        parent: typing.Union[MetaOapg.properties.parent, str, ],
        properties: typing.Union[MetaOapg.properties.properties, str, ],
        title: typing.Union['DatabaseCreateNewDatabaseRequestTitle', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DatabaseCreateNewDatabaseRequest':
        return super().__new__(
            cls,
            *args,
            parent=parent,
            properties=properties,
            title=title,
            _configuration=_configuration,
            **kwargs,
        )

from notion_python_sdk.model.database_create_new_database_request_title import DatabaseCreateNewDatabaseRequestTitle
