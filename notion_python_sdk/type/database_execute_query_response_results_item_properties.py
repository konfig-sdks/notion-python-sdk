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

from notion_python_sdk.type.database_execute_query_response_results_item_properties_cost_of_next_trip import DatabaseExecuteQueryResponseResultsItemPropertiesCostOfNextTrip
from notion_python_sdk.type.database_execute_query_response_results_item_properties_description import DatabaseExecuteQueryResponseResultsItemPropertiesDescription
from notion_python_sdk.type.database_execute_query_response_results_item_properties_food_group import DatabaseExecuteQueryResponseResultsItemPropertiesFoodGroup
from notion_python_sdk.type.database_execute_query_response_results_item_properties_in_stock import DatabaseExecuteQueryResponseResultsItemPropertiesInStock
from notion_python_sdk.type.database_execute_query_response_results_item_properties_last_ordered import DatabaseExecuteQueryResponseResultsItemPropertiesLastOrdered
from notion_python_sdk.type.database_execute_query_response_results_item_properties_name import DatabaseExecuteQueryResponseResultsItemPropertiesName
from notion_python_sdk.type.database_execute_query_response_results_item_properties_number_of_meals import DatabaseExecuteQueryResponseResultsItemPropertiesNumberOfMeals
from notion_python_sdk.type.database_execute_query_response_results_item_properties_photo import DatabaseExecuteQueryResponseResultsItemPropertiesPhoto
from notion_python_sdk.type.database_execute_query_response_results_item_properties_price import DatabaseExecuteQueryResponseResultsItemPropertiesPrice
from notion_python_sdk.type.database_execute_query_response_results_item_properties_recipes import DatabaseExecuteQueryResponseResultsItemPropertiesRecipes
from notion_python_sdk.type.database_execute_query_response_results_item_properties_responsible_person import DatabaseExecuteQueryResponseResultsItemPropertiesResponsiblePerson
from notion_python_sdk.type.database_execute_query_response_results_item_properties_store_availability import DatabaseExecuteQueryResponseResultsItemPropertiesStoreAvailability

RequiredDatabaseExecuteQueryResponseResultsItemProperties = TypedDict("RequiredDatabaseExecuteQueryResponseResultsItemProperties", {
    })

OptionalDatabaseExecuteQueryResponseResultsItemProperties = TypedDict("OptionalDatabaseExecuteQueryResponseResultsItemProperties", {
    "Store availability": DatabaseExecuteQueryResponseResultsItemPropertiesStoreAvailability,

    "Food group": DatabaseExecuteQueryResponseResultsItemPropertiesFoodGroup,

    "Price": DatabaseExecuteQueryResponseResultsItemPropertiesPrice,

    "Responsible Person": DatabaseExecuteQueryResponseResultsItemPropertiesResponsiblePerson,

    "Last ordered": DatabaseExecuteQueryResponseResultsItemPropertiesLastOrdered,

    "Cost of next trip": DatabaseExecuteQueryResponseResultsItemPropertiesCostOfNextTrip,

    "Recipes": DatabaseExecuteQueryResponseResultsItemPropertiesRecipes,

    "Description": DatabaseExecuteQueryResponseResultsItemPropertiesDescription,

    "In stock": DatabaseExecuteQueryResponseResultsItemPropertiesInStock,

    "Number of meals": DatabaseExecuteQueryResponseResultsItemPropertiesNumberOfMeals,

    "Photo": DatabaseExecuteQueryResponseResultsItemPropertiesPhoto,

    "Name": DatabaseExecuteQueryResponseResultsItemPropertiesName,
    }, total=False)

class DatabaseExecuteQueryResponseResultsItemProperties(RequiredDatabaseExecuteQueryResponseResultsItemProperties, OptionalDatabaseExecuteQueryResponseResultsItemProperties):
    pass
