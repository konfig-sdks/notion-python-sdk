import typing_extensions

from notion_python_sdk.apis.tags import TagValues
from notion_python_sdk.apis.tags.block_api import BlockApi
from notion_python_sdk.apis.tags.page_api import PageApi
from notion_python_sdk.apis.tags.database_api import DatabaseApi
from notion_python_sdk.apis.tags.user_api import UserApi
from notion_python_sdk.apis.tags.comment_api import CommentApi
from notion_python_sdk.apis.tags.token_api import TokenApi
from notion_python_sdk.apis.tags.search_api import SearchApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BLOCK: BlockApi,
        TagValues.PAGE: PageApi,
        TagValues.DATABASE: DatabaseApi,
        TagValues.USER: UserApi,
        TagValues.COMMENT: CommentApi,
        TagValues.TOKEN: TokenApi,
        TagValues.SEARCH: SearchApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BLOCK: BlockApi,
        TagValues.PAGE: PageApi,
        TagValues.DATABASE: DatabaseApi,
        TagValues.USER: UserApi,
        TagValues.COMMENT: CommentApi,
        TagValues.TOKEN: TokenApi,
        TagValues.SEARCH: SearchApi,
    }
)
