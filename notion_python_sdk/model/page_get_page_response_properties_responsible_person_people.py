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


class PageGetPageResponsePropertiesResponsiblePersonPeople(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PageGetPageResponsePropertiesResponsiblePersonPeopleItem']:
            return PageGetPageResponsePropertiesResponsiblePersonPeopleItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PageGetPageResponsePropertiesResponsiblePersonPeopleItem'], typing.List['PageGetPageResponsePropertiesResponsiblePersonPeopleItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PageGetPageResponsePropertiesResponsiblePersonPeople':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PageGetPageResponsePropertiesResponsiblePersonPeopleItem':
        return super().__getitem__(i)

from notion_python_sdk.model.page_get_page_response_properties_responsible_person_people_item import PageGetPageResponsePropertiesResponsiblePersonPeopleItem