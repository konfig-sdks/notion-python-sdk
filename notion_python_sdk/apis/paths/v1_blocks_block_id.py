from notion_python_sdk.paths.v1_blocks_block_id.get import ApiForget
from notion_python_sdk.paths.v1_blocks_block_id.delete import ApiFordelete
from notion_python_sdk.paths.v1_blocks_block_id.patch import ApiForpatch


class V1BlocksBlockId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
