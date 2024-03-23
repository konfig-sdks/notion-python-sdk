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


class CommentCreateNewResponse(
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
            def parent() -> typing.Type['CommentCreateNewResponseParent']:
                return CommentCreateNewResponseParent
            discussion_id = schemas.StrSchema
            created_time = schemas.StrSchema
            last_edited_time = schemas.StrSchema
        
            @staticmethod
            def created_by() -> typing.Type['CommentCreateNewResponseCreatedBy']:
                return CommentCreateNewResponseCreatedBy
        
            @staticmethod
            def rich_text() -> typing.Type['CommentCreateNewResponseRichText']:
                return CommentCreateNewResponseRichText
            __annotations__ = {
                "object": object,
                "id": id,
                "parent": parent,
                "discussion_id": discussion_id,
                "created_time": created_time,
                "last_edited_time": last_edited_time,
                "created_by": created_by,
                "rich_text": rich_text,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> 'CommentCreateNewResponseParent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discussion_id"]) -> MetaOapg.properties.discussion_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_time"]) -> MetaOapg.properties.created_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_edited_time"]) -> MetaOapg.properties.last_edited_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> 'CommentCreateNewResponseCreatedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rich_text"]) -> 'CommentCreateNewResponseRichText': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["object", "id", "parent", "discussion_id", "created_time", "last_edited_time", "created_by", "rich_text", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union['CommentCreateNewResponseParent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discussion_id"]) -> typing.Union[MetaOapg.properties.discussion_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_time"]) -> typing.Union[MetaOapg.properties.created_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_edited_time"]) -> typing.Union[MetaOapg.properties.last_edited_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union['CommentCreateNewResponseCreatedBy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rich_text"]) -> typing.Union['CommentCreateNewResponseRichText', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["object", "id", "parent", "discussion_id", "created_time", "last_edited_time", "created_by", "rich_text", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        parent: typing.Union['CommentCreateNewResponseParent', schemas.Unset] = schemas.unset,
        discussion_id: typing.Union[MetaOapg.properties.discussion_id, str, schemas.Unset] = schemas.unset,
        created_time: typing.Union[MetaOapg.properties.created_time, str, schemas.Unset] = schemas.unset,
        last_edited_time: typing.Union[MetaOapg.properties.last_edited_time, str, schemas.Unset] = schemas.unset,
        created_by: typing.Union['CommentCreateNewResponseCreatedBy', schemas.Unset] = schemas.unset,
        rich_text: typing.Union['CommentCreateNewResponseRichText', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CommentCreateNewResponse':
        return super().__new__(
            cls,
            *args,
            object=object,
            id=id,
            parent=parent,
            discussion_id=discussion_id,
            created_time=created_time,
            last_edited_time=last_edited_time,
            created_by=created_by,
            rich_text=rich_text,
            _configuration=_configuration,
            **kwargs,
        )

from notion_python_sdk.model.comment_create_new_response_created_by import CommentCreateNewResponseCreatedBy
from notion_python_sdk.model.comment_create_new_response_parent import CommentCreateNewResponseParent
from notion_python_sdk.model.comment_create_new_response_rich_text import CommentCreateNewResponseRichText
