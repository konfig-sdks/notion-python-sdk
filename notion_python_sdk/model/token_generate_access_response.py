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


class TokenGenerateAccessResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            access_token = schemas.StrSchema
            bot_id = schemas.StrSchema
            duplicated_template_id = schemas.AnyTypeSchema
        
            @staticmethod
            def owner() -> typing.Type['TokenGenerateAccessResponseOwner']:
                return TokenGenerateAccessResponseOwner
            workspace_icon = schemas.StrSchema
            workspace_id = schemas.StrSchema
            workspace_name = schemas.StrSchema
            __annotations__ = {
                "access_token": access_token,
                "bot_id": bot_id,
                "duplicated_template_id": duplicated_template_id,
                "owner": owner,
                "workspace_icon": workspace_icon,
                "workspace_id": workspace_id,
                "workspace_name": workspace_name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_token"]) -> MetaOapg.properties.access_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bot_id"]) -> MetaOapg.properties.bot_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duplicated_template_id"]) -> MetaOapg.properties.duplicated_template_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> 'TokenGenerateAccessResponseOwner': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_icon"]) -> MetaOapg.properties.workspace_icon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_id"]) -> MetaOapg.properties.workspace_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_name"]) -> MetaOapg.properties.workspace_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["access_token", "bot_id", "duplicated_template_id", "owner", "workspace_icon", "workspace_id", "workspace_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_token"]) -> typing.Union[MetaOapg.properties.access_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bot_id"]) -> typing.Union[MetaOapg.properties.bot_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duplicated_template_id"]) -> typing.Union[MetaOapg.properties.duplicated_template_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union['TokenGenerateAccessResponseOwner', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_icon"]) -> typing.Union[MetaOapg.properties.workspace_icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_id"]) -> typing.Union[MetaOapg.properties.workspace_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_name"]) -> typing.Union[MetaOapg.properties.workspace_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["access_token", "bot_id", "duplicated_template_id", "owner", "workspace_icon", "workspace_id", "workspace_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        access_token: typing.Union[MetaOapg.properties.access_token, str, schemas.Unset] = schemas.unset,
        bot_id: typing.Union[MetaOapg.properties.bot_id, str, schemas.Unset] = schemas.unset,
        duplicated_template_id: typing.Union[MetaOapg.properties.duplicated_template_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        owner: typing.Union['TokenGenerateAccessResponseOwner', schemas.Unset] = schemas.unset,
        workspace_icon: typing.Union[MetaOapg.properties.workspace_icon, str, schemas.Unset] = schemas.unset,
        workspace_id: typing.Union[MetaOapg.properties.workspace_id, str, schemas.Unset] = schemas.unset,
        workspace_name: typing.Union[MetaOapg.properties.workspace_name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TokenGenerateAccessResponse':
        return super().__new__(
            cls,
            *args,
            access_token=access_token,
            bot_id=bot_id,
            duplicated_template_id=duplicated_template_id,
            owner=owner,
            workspace_icon=workspace_icon,
            workspace_id=workspace_id,
            workspace_name=workspace_name,
            _configuration=_configuration,
            **kwargs,
        )

from notion_python_sdk.model.token_generate_access_response_owner import TokenGenerateAccessResponseOwner
