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

from notion_python_sdk.type.database_get_database_response_properties_meals_relation import DatabaseGetDatabaseResponsePropertiesMealsRelation

class RequiredDatabaseGetDatabaseResponsePropertiesMeals(TypedDict):
    pass

class OptionalDatabaseGetDatabaseResponsePropertiesMeals(TypedDict, total=False):
    id: str

    name: str

    type: str

    relation: DatabaseGetDatabaseResponsePropertiesMealsRelation

class DatabaseGetDatabaseResponsePropertiesMeals(RequiredDatabaseGetDatabaseResponsePropertiesMeals, OptionalDatabaseGetDatabaseResponsePropertiesMeals):
    pass