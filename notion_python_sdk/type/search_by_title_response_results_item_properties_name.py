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

from notion_python_sdk.type.search_by_title_response_results_item_properties_name_title import SearchByTitleResponseResultsItemPropertiesNameTitle

class RequiredSearchByTitleResponseResultsItemPropertiesName(TypedDict):
    pass

class OptionalSearchByTitleResponseResultsItemPropertiesName(TypedDict, total=False):
    title: SearchByTitleResponseResultsItemPropertiesNameTitle

    id: str

    type: str

class SearchByTitleResponseResultsItemPropertiesName(RequiredSearchByTitleResponseResultsItemPropertiesName, OptionalSearchByTitleResponseResultsItemPropertiesName):
    pass
