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

from notion_python_sdk.type.database_get_database_response_properties1 import DatabaseGetDatabaseResponseProperties1
from notion_python_sdk.type.database_get_database_response_properties_description import DatabaseGetDatabaseResponsePropertiesDescription
from notion_python_sdk.type.database_get_database_response_properties_food_group import DatabaseGetDatabaseResponsePropertiesFoodGroup
from notion_python_sdk.type.database_get_database_response_properties_in_stock import DatabaseGetDatabaseResponsePropertiesInStock
from notion_python_sdk.type.database_get_database_response_properties_last_ordered import DatabaseGetDatabaseResponsePropertiesLastOrdered
from notion_python_sdk.type.database_get_database_response_properties_meals import DatabaseGetDatabaseResponsePropertiesMeals
from notion_python_sdk.type.database_get_database_response_properties_name import DatabaseGetDatabaseResponsePropertiesName
from notion_python_sdk.type.database_get_database_response_properties_number_of_meals import DatabaseGetDatabaseResponsePropertiesNumberOfMeals
from notion_python_sdk.type.database_get_database_response_properties_photo import DatabaseGetDatabaseResponsePropertiesPhoto
from notion_python_sdk.type.database_get_database_response_properties_price import DatabaseGetDatabaseResponsePropertiesPrice
from notion_python_sdk.type.database_get_database_response_properties_store_availability import DatabaseGetDatabaseResponsePropertiesStoreAvailability

RequiredDatabaseGetDatabaseResponseProperties = TypedDict("RequiredDatabaseGetDatabaseResponseProperties", {
    })

OptionalDatabaseGetDatabaseResponseProperties = TypedDict("OptionalDatabaseGetDatabaseResponseProperties", {
    "+1": DatabaseGetDatabaseResponseProperties1,

    "In stock": DatabaseGetDatabaseResponsePropertiesInStock,

    "Price": DatabaseGetDatabaseResponsePropertiesPrice,

    "Description": DatabaseGetDatabaseResponsePropertiesDescription,

    "Last ordered": DatabaseGetDatabaseResponsePropertiesLastOrdered,

    "Meals": DatabaseGetDatabaseResponsePropertiesMeals,

    "Number of meals": DatabaseGetDatabaseResponsePropertiesNumberOfMeals,

    "Store availability": DatabaseGetDatabaseResponsePropertiesStoreAvailability,

    "Photo": DatabaseGetDatabaseResponsePropertiesPhoto,

    "Food group": DatabaseGetDatabaseResponsePropertiesFoodGroup,

    "Name": DatabaseGetDatabaseResponsePropertiesName,
    }, total=False)

class DatabaseGetDatabaseResponseProperties(RequiredDatabaseGetDatabaseResponseProperties, OptionalDatabaseGetDatabaseResponseProperties):
    pass