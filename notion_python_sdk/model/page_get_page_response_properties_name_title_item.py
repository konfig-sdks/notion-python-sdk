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


class PageGetPageResponsePropertiesNameTitleItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
        
            @staticmethod
            def text() -> typing.Type['PageGetPageResponsePropertiesNameTitleItemText']:
                return PageGetPageResponsePropertiesNameTitleItemText
        
            @staticmethod
            def annotations() -> typing.Type['PageGetPageResponsePropertiesNameTitleItemAnnotations']:
                return PageGetPageResponsePropertiesNameTitleItemAnnotations
            plain_text = schemas.StrSchema
            href = schemas.AnyTypeSchema
            __annotations__ = {
                "type": type,
                "text": text,
                "annotations": annotations,
                "plain_text": plain_text,
                "href": href,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> 'PageGetPageResponsePropertiesNameTitleItemText': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annotations"]) -> 'PageGetPageResponsePropertiesNameTitleItemAnnotations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plain_text"]) -> MetaOapg.properties.plain_text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "text", "annotations", "plain_text", "href", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union['PageGetPageResponsePropertiesNameTitleItemText', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annotations"]) -> typing.Union['PageGetPageResponsePropertiesNameTitleItemAnnotations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plain_text"]) -> typing.Union[MetaOapg.properties.plain_text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> typing.Union[MetaOapg.properties.href, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "text", "annotations", "plain_text", "href", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        text: typing.Union['PageGetPageResponsePropertiesNameTitleItemText', schemas.Unset] = schemas.unset,
        annotations: typing.Union['PageGetPageResponsePropertiesNameTitleItemAnnotations', schemas.Unset] = schemas.unset,
        plain_text: typing.Union[MetaOapg.properties.plain_text, str, schemas.Unset] = schemas.unset,
        href: typing.Union[MetaOapg.properties.href, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PageGetPageResponsePropertiesNameTitleItem':
        return super().__new__(
            cls,
            *args,
            type=type,
            text=text,
            annotations=annotations,
            plain_text=plain_text,
            href=href,
            _configuration=_configuration,
            **kwargs,
        )

from notion_python_sdk.model.page_get_page_response_properties_name_title_item_annotations import PageGetPageResponsePropertiesNameTitleItemAnnotations
from notion_python_sdk.model.page_get_page_response_properties_name_title_item_text import PageGetPageResponsePropertiesNameTitleItemText
