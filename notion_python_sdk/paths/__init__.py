# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from notion_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_OAUTH_TOKEN = "/v1/oauth/token"
    V1_BLOCKS_BLOCK_ID_CHILDREN = "/v1/blocks/{block_id}/children"
    V1_BLOCKS_BLOCK_ID = "/v1/blocks/{block_id}"
    V1_PAGES = "/v1/pages"
    V1_PAGES_PAGE_ID = "/v1/pages/{page_id}"
    V1_PAGES_PAGE_ID_PROPERTIES_PROPERTY_ID = "/v1/pages/{page_id}/properties/{property_id}"
    V1_DATABASES = "/v1/databases"
    V1_DATABASES_DATABASE_ID_QUERY = "/v1/databases/{database_id}/query"
    V1_DATABASES_DATABASE_ID = "/v1/databases/{database_id}"
    V1_USERS = "/v1/users"
    V1_USERS_USER_ID = "/v1/users/{user_id}"
    V1_USERS_ME = "/v1/users/me"
    V1_COMMENTS = "/v1/comments"
    V1_SEARCH = "/v1/search"
