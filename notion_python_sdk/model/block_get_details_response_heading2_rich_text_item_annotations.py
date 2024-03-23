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


class BlockGetDetailsResponseHeading2RichTextItemAnnotations(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            bold = schemas.BoolSchema
            italic = schemas.BoolSchema
            strikethrough = schemas.BoolSchema
            underline = schemas.BoolSchema
            code = schemas.BoolSchema
            color = schemas.StrSchema
            __annotations__ = {
                "bold": bold,
                "italic": italic,
                "strikethrough": strikethrough,
                "underline": underline,
                "code": code,
                "color": color,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bold"]) -> MetaOapg.properties.bold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["italic"]) -> MetaOapg.properties.italic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["strikethrough"]) -> MetaOapg.properties.strikethrough: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["underline"]) -> MetaOapg.properties.underline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bold", "italic", "strikethrough", "underline", "code", "color", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bold"]) -> typing.Union[MetaOapg.properties.bold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["italic"]) -> typing.Union[MetaOapg.properties.italic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["strikethrough"]) -> typing.Union[MetaOapg.properties.strikethrough, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["underline"]) -> typing.Union[MetaOapg.properties.underline, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bold", "italic", "strikethrough", "underline", "code", "color", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bold: typing.Union[MetaOapg.properties.bold, bool, schemas.Unset] = schemas.unset,
        italic: typing.Union[MetaOapg.properties.italic, bool, schemas.Unset] = schemas.unset,
        strikethrough: typing.Union[MetaOapg.properties.strikethrough, bool, schemas.Unset] = schemas.unset,
        underline: typing.Union[MetaOapg.properties.underline, bool, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, bool, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BlockGetDetailsResponseHeading2RichTextItemAnnotations':
        return super().__new__(
            cls,
            *args,
            bold=bold,
            italic=italic,
            strikethrough=strikethrough,
            underline=underline,
            code=code,
            color=color,
            _configuration=_configuration,
            **kwargs,
        )
