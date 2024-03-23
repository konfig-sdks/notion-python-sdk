# coding: utf-8

"""
    Notion API

    Notion is a new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from notion_python_sdk.pydantic.database_get_database_response_properties_store_availability_multi_select import DatabaseGetDatabaseResponsePropertiesStoreAvailabilityMultiSelect

class DatabaseGetDatabaseResponsePropertiesStoreAvailability(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    type: typing.Optional[str] = Field(None, alias='type')

    multi_select: typing.Optional[DatabaseGetDatabaseResponsePropertiesStoreAvailabilityMultiSelect] = Field(None, alias='multi_select')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
