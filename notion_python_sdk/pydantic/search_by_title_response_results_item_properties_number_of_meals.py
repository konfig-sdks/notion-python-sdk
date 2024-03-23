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

from notion_python_sdk.pydantic.search_by_title_response_results_item_properties_number_of_meals_rollup import SearchByTitleResponseResultsItemPropertiesNumberOfMealsRollup

class SearchByTitleResponseResultsItemPropertiesNumberOfMeals(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    type: typing.Optional[str] = Field(None, alias='type')

    rollup: typing.Optional[SearchByTitleResponseResultsItemPropertiesNumberOfMealsRollup] = Field(None, alias='rollup')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
