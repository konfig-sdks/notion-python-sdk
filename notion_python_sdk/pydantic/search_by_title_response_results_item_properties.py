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

from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_cost_of_next_trip import SearchByTitleResponseResultsItemPropertiesCostOfNextTrip
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_description import SearchByTitleResponseResultsItemPropertiesDescription
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_food_group import SearchByTitleResponseResultsItemPropertiesFoodGroup
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_in_stock import SearchByTitleResponseResultsItemPropertiesInStock
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_last_ordered import SearchByTitleResponseResultsItemPropertiesLastOrdered
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_name import SearchByTitleResponseResultsItemPropertiesName
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_number_of_meals import SearchByTitleResponseResultsItemPropertiesNumberOfMeals
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_photo import SearchByTitleResponseResultsItemPropertiesPhoto
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_price import SearchByTitleResponseResultsItemPropertiesPrice
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_recipes import SearchByTitleResponseResultsItemPropertiesRecipes
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_responsible_person import SearchByTitleResponseResultsItemPropertiesResponsiblePerson
from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_store_availability import SearchByTitleResponseResultsItemPropertiesStoreAvailability

class SearchByTitleResponseResultsItemProperties(BaseModel):
    store availability_: typing.Optional[SearchByTitleResponseResultsItemPropertiesStoreAvailability] = Field(None, alias='Store availability')

    food group_: typing.Optional[SearchByTitleResponseResultsItemPropertiesFoodGroup] = Field(None, alias='Food group')

    price: typing.Optional[SearchByTitleResponseResultsItemPropertiesPrice] = Field(None, alias='Price')

    responsible _person_: typing.Optional[SearchByTitleResponseResultsItemPropertiesResponsiblePerson] = Field(None, alias='Responsible Person')

    last ordered_: typing.Optional[SearchByTitleResponseResultsItemPropertiesLastOrdered] = Field(None, alias='Last ordered')

    cost of next trip_: typing.Optional[SearchByTitleResponseResultsItemPropertiesCostOfNextTrip] = Field(None, alias='Cost of next trip')

    recipes: typing.Optional[SearchByTitleResponseResultsItemPropertiesRecipes] = Field(None, alias='Recipes')

    description: typing.Optional[SearchByTitleResponseResultsItemPropertiesDescription] = Field(None, alias='Description')

    in stock_: typing.Optional[SearchByTitleResponseResultsItemPropertiesInStock] = Field(None, alias='In stock')

    number of meals_: typing.Optional[SearchByTitleResponseResultsItemPropertiesNumberOfMeals] = Field(None, alias='Number of meals')

    photo: typing.Optional[SearchByTitleResponseResultsItemPropertiesPhoto] = Field(None, alias='Photo')

    name: typing.Optional[SearchByTitleResponseResultsItemPropertiesName] = Field(None, alias='Name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )