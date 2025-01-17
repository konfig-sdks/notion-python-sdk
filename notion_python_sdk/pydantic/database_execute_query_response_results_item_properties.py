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

from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_cost_of_next_trip import DatabaseExecuteQueryResponseResultsItemPropertiesCostOfNextTrip
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_description import DatabaseExecuteQueryResponseResultsItemPropertiesDescription
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_food_group import DatabaseExecuteQueryResponseResultsItemPropertiesFoodGroup
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_in_stock import DatabaseExecuteQueryResponseResultsItemPropertiesInStock
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_last_ordered import DatabaseExecuteQueryResponseResultsItemPropertiesLastOrdered
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_name import DatabaseExecuteQueryResponseResultsItemPropertiesName
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_number_of_meals import DatabaseExecuteQueryResponseResultsItemPropertiesNumberOfMeals
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_photo import DatabaseExecuteQueryResponseResultsItemPropertiesPhoto
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_price import DatabaseExecuteQueryResponseResultsItemPropertiesPrice
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_recipes import DatabaseExecuteQueryResponseResultsItemPropertiesRecipes
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_responsible_person import DatabaseExecuteQueryResponseResultsItemPropertiesResponsiblePerson
from notion_python_sdk.pydantic.database_execute_query_response_results_item_properties_store_availability import DatabaseExecuteQueryResponseResultsItemPropertiesStoreAvailability

class DatabaseExecuteQueryResponseResultsItemProperties(BaseModel):
    store availability_: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesStoreAvailability] = Field(None, alias='Store availability')

    food group_: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesFoodGroup] = Field(None, alias='Food group')

    price: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesPrice] = Field(None, alias='Price')

    responsible _person_: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesResponsiblePerson] = Field(None, alias='Responsible Person')

    last ordered_: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesLastOrdered] = Field(None, alias='Last ordered')

    cost of next trip_: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesCostOfNextTrip] = Field(None, alias='Cost of next trip')

    recipes: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesRecipes] = Field(None, alias='Recipes')

    description: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesDescription] = Field(None, alias='Description')

    in stock_: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesInStock] = Field(None, alias='In stock')

    number of meals_: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesNumberOfMeals] = Field(None, alias='Number of meals')

    photo: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesPhoto] = Field(None, alias='Photo')

    name: typing.Optional[DatabaseExecuteQueryResponseResultsItemPropertiesName] = Field(None, alias='Name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
