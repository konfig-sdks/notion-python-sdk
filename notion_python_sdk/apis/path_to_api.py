import typing_extensions

from notion_python_sdk.paths import PathValues
from notion_python_sdk.apis.paths.v1_oauth_token import V1OauthToken
from notion_python_sdk.apis.paths.v1_blocks_block_id_children import V1BlocksBlockIdChildren
from notion_python_sdk.apis.paths.v1_blocks_block_id import V1BlocksBlockId
from notion_python_sdk.apis.paths.v1_pages import V1Pages
from notion_python_sdk.apis.paths.v1_pages_page_id import V1PagesPageId
from notion_python_sdk.apis.paths.v1_pages_page_id_properties_property_id import V1PagesPageIdPropertiesPropertyId
from notion_python_sdk.apis.paths.v1_databases import V1Databases
from notion_python_sdk.apis.paths.v1_databases_database_id_query import V1DatabasesDatabaseIdQuery
from notion_python_sdk.apis.paths.v1_databases_database_id import V1DatabasesDatabaseId
from notion_python_sdk.apis.paths.v1_users import V1Users
from notion_python_sdk.apis.paths.v1_users_user_id import V1UsersUserId
from notion_python_sdk.apis.paths.v1_users_me import V1UsersMe
from notion_python_sdk.apis.paths.v1_comments import V1Comments
from notion_python_sdk.apis.paths.v1_search import V1Search

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_OAUTH_TOKEN: V1OauthToken,
        PathValues.V1_BLOCKS_BLOCK_ID_CHILDREN: V1BlocksBlockIdChildren,
        PathValues.V1_BLOCKS_BLOCK_ID: V1BlocksBlockId,
        PathValues.V1_PAGES: V1Pages,
        PathValues.V1_PAGES_PAGE_ID: V1PagesPageId,
        PathValues.V1_PAGES_PAGE_ID_PROPERTIES_PROPERTY_ID: V1PagesPageIdPropertiesPropertyId,
        PathValues.V1_DATABASES: V1Databases,
        PathValues.V1_DATABASES_DATABASE_ID_QUERY: V1DatabasesDatabaseIdQuery,
        PathValues.V1_DATABASES_DATABASE_ID: V1DatabasesDatabaseId,
        PathValues.V1_USERS: V1Users,
        PathValues.V1_USERS_USER_ID: V1UsersUserId,
        PathValues.V1_USERS_ME: V1UsersMe,
        PathValues.V1_COMMENTS: V1Comments,
        PathValues.V1_SEARCH: V1Search,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_OAUTH_TOKEN: V1OauthToken,
        PathValues.V1_BLOCKS_BLOCK_ID_CHILDREN: V1BlocksBlockIdChildren,
        PathValues.V1_BLOCKS_BLOCK_ID: V1BlocksBlockId,
        PathValues.V1_PAGES: V1Pages,
        PathValues.V1_PAGES_PAGE_ID: V1PagesPageId,
        PathValues.V1_PAGES_PAGE_ID_PROPERTIES_PROPERTY_ID: V1PagesPageIdPropertiesPropertyId,
        PathValues.V1_DATABASES: V1Databases,
        PathValues.V1_DATABASES_DATABASE_ID_QUERY: V1DatabasesDatabaseIdQuery,
        PathValues.V1_DATABASES_DATABASE_ID: V1DatabasesDatabaseId,
        PathValues.V1_USERS: V1Users,
        PathValues.V1_USERS_USER_ID: V1UsersUserId,
        PathValues.V1_USERS_ME: V1UsersMe,
        PathValues.V1_COMMENTS: V1Comments,
        PathValues.V1_SEARCH: V1Search,
    }
)
