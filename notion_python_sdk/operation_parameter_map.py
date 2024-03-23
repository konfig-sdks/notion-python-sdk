operation_parameter_map = {
    '/v1/blocks/{block_id}/children-PATCH': {
        'parameters': [
            {
                'name': 'children'
            },
            {
                'name': 'block_id'
            },
            {
                'name': 'Notion-Version'
            },
            {
                'name': 'after'
            },
        ]
    },
    '/v1/blocks/{block_id}/children-GET': {
        'parameters': [
            {
                'name': 'block_id'
            },
            {
                'name': 'Notion-Version'
            },
            {
                'name': 'start_cursor'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/blocks/{block_id}-GET': {
        'parameters': [
            {
                'name': 'block_id'
            },
            {
                'name': 'Notion-Version'
            },
        ]
    },
    '/v1/blocks/{block_id}-DELETE': {
        'parameters': [
            {
                'name': 'block_id'
            },
            {
                'name': 'Notion-Version'
            },
        ]
    },
    '/v1/blocks/{block_id}-PATCH': {
        'parameters': [
            {
                'name': 'block_id'
            },
            {
                'name': '{type}'
            },
            {
                'name': 'archived'
            },
            {
                'name': 'Notion-Version'
            },
        ]
    },
    '/v1/comments-POST': {
        'parameters': [
            {
                'name': 'rich_text'
            },
            {
                'name': 'Notion-Version'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'discussion_id'
            },
        ]
    },
    '/v1/comments-GET': {
        'parameters': [
            {
                'name': 'Notion-Version'
            },
            {
                'name': 'block_id'
            },
            {
                'name': 'start_cursor'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/databases-POST': {
        'parameters': [
            {
                'name': 'parent'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'Notion-Version'
            },
            {
                'name': 'title'
            },
        ]
    },
    '/v1/databases/{database_id}/query-POST': {
        'parameters': [
            {
                'name': 'database_id'
            },
            {
                'name': 'Notion-Version'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'sorts'
            },
            {
                'name': 'start_cursor'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'filter_properties'
            },
        ]
    },
    '/v1/databases/{database_id}-GET': {
        'parameters': [
            {
                'name': 'database_id'
            },
            {
                'name': 'Notion-Version'
            },
        ]
    },
    '/v1/databases/{database_id}-PATCH': {
        'parameters': [
            {
                'name': 'database_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'Notion-Version'
            },
        ]
    },
    '/v1/pages-POST': {
        'parameters': [
            {
                'name': 'parent'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'Notion-Version'
            },
            {
                'name': 'children'
            },
            {
                'name': 'icon'
            },
            {
                'name': 'cover'
            },
        ]
    },
    '/v1/pages/{page_id}-GET': {
        'parameters': [
            {
                'name': 'page_id'
            },
            {
                'name': 'Notion-Version'
            },
            {
                'name': 'filter_properties'
            },
        ]
    },
    '/v1/pages/{page_id}/properties/{property_id}-GET': {
        'parameters': [
            {
                'name': 'page_id'
            },
            {
                'name': 'property_id'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'start_cursor'
            },
            {
                'name': 'Notion-Version'
            },
        ]
    },
    '/v1/pages/{page_id}-PATCH': {
        'parameters': [
            {
                'name': 'page_id'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'archived'
            },
            {
                'name': 'icon'
            },
            {
                'name': 'cover'
            },
            {
                'name': 'Notion-Version'
            },
        ]
    },
    '/v1/search-POST': {
        'parameters': [
            {
                'name': 'Notion-Version'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'start_cursor'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/oauth/token-POST': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'grant_type'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'external_account'
            },
        ]
    },
    '/v1/users/me-GET': {
        'parameters': [
            {
                'name': 'Notion-Version'
            },
        ]
    },
    '/v1/users/{user_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'Notion-Version'
            },
        ]
    },
    '/v1/users-GET': {
        'parameters': [
            {
                'name': 'Notion-Version'
            },
            {
                'name': 'start_cursor'
            },
            {
                'name': 'page_size'
            },
        ]
    },
};