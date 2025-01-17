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


class BlockGetDetailsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            object = schemas.StrSchema
            id = schemas.StrSchema
        
            @staticmethod
            def parent() -> typing.Type['BlockGetDetailsResponseParent']:
                return BlockGetDetailsResponseParent
            created_time = schemas.StrSchema
            last_edited_time = schemas.StrSchema
        
            @staticmethod
            def created_by() -> typing.Type['BlockGetDetailsResponseCreatedBy']:
                return BlockGetDetailsResponseCreatedBy
        
            @staticmethod
            def last_edited_by() -> typing.Type['BlockGetDetailsResponseLastEditedBy']:
                return BlockGetDetailsResponseLastEditedBy
            has_children = schemas.BoolSchema
            archived = schemas.BoolSchema
            type = schemas.StrSchema
        
            @staticmethod
            def heading_2() -> typing.Type['BlockGetDetailsResponseHeading2']:
                return BlockGetDetailsResponseHeading2
            __annotations__ = {
                "object": object,
                "id": id,
                "parent": parent,
                "created_time": created_time,
                "last_edited_time": last_edited_time,
                "created_by": created_by,
                "last_edited_by": last_edited_by,
                "has_children": has_children,
                "archived": archived,
                "type": type,
                "heading_2": heading_2,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> 'BlockGetDetailsResponseParent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_time"]) -> MetaOapg.properties.created_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_edited_time"]) -> MetaOapg.properties.last_edited_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> 'BlockGetDetailsResponseCreatedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_edited_by"]) -> 'BlockGetDetailsResponseLastEditedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_children"]) -> MetaOapg.properties.has_children: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heading_2"]) -> 'BlockGetDetailsResponseHeading2': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["object", "id", "parent", "created_time", "last_edited_time", "created_by", "last_edited_by", "has_children", "archived", "type", "heading_2", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union['BlockGetDetailsResponseParent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_time"]) -> typing.Union[MetaOapg.properties.created_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_edited_time"]) -> typing.Union[MetaOapg.properties.last_edited_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union['BlockGetDetailsResponseCreatedBy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_edited_by"]) -> typing.Union['BlockGetDetailsResponseLastEditedBy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_children"]) -> typing.Union[MetaOapg.properties.has_children, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heading_2"]) -> typing.Union['BlockGetDetailsResponseHeading2', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["object", "id", "parent", "created_time", "last_edited_time", "created_by", "last_edited_by", "has_children", "archived", "type", "heading_2", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        parent: typing.Union['BlockGetDetailsResponseParent', schemas.Unset] = schemas.unset,
        created_time: typing.Union[MetaOapg.properties.created_time, str, schemas.Unset] = schemas.unset,
        last_edited_time: typing.Union[MetaOapg.properties.last_edited_time, str, schemas.Unset] = schemas.unset,
        created_by: typing.Union['BlockGetDetailsResponseCreatedBy', schemas.Unset] = schemas.unset,
        last_edited_by: typing.Union['BlockGetDetailsResponseLastEditedBy', schemas.Unset] = schemas.unset,
        has_children: typing.Union[MetaOapg.properties.has_children, bool, schemas.Unset] = schemas.unset,
        archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        heading_2: typing.Union['BlockGetDetailsResponseHeading2', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BlockGetDetailsResponse':
        return super().__new__(
            cls,
            *args,
            object=object,
            id=id,
            parent=parent,
            created_time=created_time,
            last_edited_time=last_edited_time,
            created_by=created_by,
            last_edited_by=last_edited_by,
            has_children=has_children,
            archived=archived,
            type=type,
            heading_2=heading_2,
            _configuration=_configuration,
            **kwargs,
        )

from notion_python_sdk.model.block_get_details_response_created_by import BlockGetDetailsResponseCreatedBy
from notion_python_sdk.model.block_get_details_response_heading2 import BlockGetDetailsResponseHeading2
from notion_python_sdk.model.block_get_details_response_last_edited_by import BlockGetDetailsResponseLastEditedBy
from notion_python_sdk.model.block_get_details_response_parent import BlockGetDetailsResponseParent
