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


class PageGetPageResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            object = schemas.StrSchema
            id = schemas.StrSchema
            created_time = schemas.StrSchema
            last_edited_time = schemas.StrSchema
        
            @staticmethod
            def created_by() -> typing.Type['PageGetPageResponseCreatedBy']:
                return PageGetPageResponseCreatedBy
        
            @staticmethod
            def last_edited_by() -> typing.Type['PageGetPageResponseLastEditedBy']:
                return PageGetPageResponseLastEditedBy
        
            @staticmethod
            def cover() -> typing.Type['PageGetPageResponseCover']:
                return PageGetPageResponseCover
        
            @staticmethod
            def icon() -> typing.Type['PageGetPageResponseIcon']:
                return PageGetPageResponseIcon
        
            @staticmethod
            def parent() -> typing.Type['PageGetPageResponseParent']:
                return PageGetPageResponseParent
            archived = schemas.BoolSchema
        
            @staticmethod
            def properties() -> typing.Type['PageGetPageResponseProperties']:
                return PageGetPageResponseProperties
            url = schemas.StrSchema
            public_url = schemas.AnyTypeSchema
            __annotations__ = {
                "object": object,
                "id": id,
                "created_time": created_time,
                "last_edited_time": last_edited_time,
                "created_by": created_by,
                "last_edited_by": last_edited_by,
                "cover": cover,
                "icon": icon,
                "parent": parent,
                "archived": archived,
                "properties": properties,
                "url": url,
                "public_url": public_url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_time"]) -> MetaOapg.properties.created_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_edited_time"]) -> MetaOapg.properties.last_edited_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> 'PageGetPageResponseCreatedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_edited_by"]) -> 'PageGetPageResponseLastEditedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover"]) -> 'PageGetPageResponseCover': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon"]) -> 'PageGetPageResponseIcon': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> 'PageGetPageResponseParent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> 'PageGetPageResponseProperties': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public_url"]) -> MetaOapg.properties.public_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["object", "id", "created_time", "last_edited_time", "created_by", "last_edited_by", "cover", "icon", "parent", "archived", "properties", "url", "public_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_time"]) -> typing.Union[MetaOapg.properties.created_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_edited_time"]) -> typing.Union[MetaOapg.properties.last_edited_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union['PageGetPageResponseCreatedBy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_edited_by"]) -> typing.Union['PageGetPageResponseLastEditedBy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover"]) -> typing.Union['PageGetPageResponseCover', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union['PageGetPageResponseIcon', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union['PageGetPageResponseParent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> typing.Union['PageGetPageResponseProperties', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public_url"]) -> typing.Union[MetaOapg.properties.public_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["object", "id", "created_time", "last_edited_time", "created_by", "last_edited_by", "cover", "icon", "parent", "archived", "properties", "url", "public_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        created_time: typing.Union[MetaOapg.properties.created_time, str, schemas.Unset] = schemas.unset,
        last_edited_time: typing.Union[MetaOapg.properties.last_edited_time, str, schemas.Unset] = schemas.unset,
        created_by: typing.Union['PageGetPageResponseCreatedBy', schemas.Unset] = schemas.unset,
        last_edited_by: typing.Union['PageGetPageResponseLastEditedBy', schemas.Unset] = schemas.unset,
        cover: typing.Union['PageGetPageResponseCover', schemas.Unset] = schemas.unset,
        icon: typing.Union['PageGetPageResponseIcon', schemas.Unset] = schemas.unset,
        parent: typing.Union['PageGetPageResponseParent', schemas.Unset] = schemas.unset,
        archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
        properties: typing.Union['PageGetPageResponseProperties', schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        public_url: typing.Union[MetaOapg.properties.public_url, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PageGetPageResponse':
        return super().__new__(
            cls,
            *args,
            object=object,
            id=id,
            created_time=created_time,
            last_edited_time=last_edited_time,
            created_by=created_by,
            last_edited_by=last_edited_by,
            cover=cover,
            icon=icon,
            parent=parent,
            archived=archived,
            properties=properties,
            url=url,
            public_url=public_url,
            _configuration=_configuration,
            **kwargs,
        )

from notion_python_sdk.model.page_get_page_response_cover import PageGetPageResponseCover
from notion_python_sdk.model.page_get_page_response_created_by import PageGetPageResponseCreatedBy
from notion_python_sdk.model.page_get_page_response_icon import PageGetPageResponseIcon
from notion_python_sdk.model.page_get_page_response_last_edited_by import PageGetPageResponseLastEditedBy
from notion_python_sdk.model.page_get_page_response_parent import PageGetPageResponseParent
from notion_python_sdk.model.page_get_page_response_properties import PageGetPageResponseProperties