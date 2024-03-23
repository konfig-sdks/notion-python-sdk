# coding: utf-8

"""
    Notion API

    Notion is a new tool that blends your everyday work apps into one. It's the all-in-one workspace for you and your team.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from notion_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from notion_python_sdk.api_response import AsyncGeneratorResponse
from notion_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from notion_python_sdk import schemas  # noqa: F401

from notion_python_sdk.model.block_append_children_request_children import BlockAppendChildrenRequestChildren as BlockAppendChildrenRequestChildrenSchema
from notion_python_sdk.model.block_append_children_response import BlockAppendChildrenResponse as BlockAppendChildrenResponseSchema
from notion_python_sdk.model.block_append_children_request import BlockAppendChildrenRequest as BlockAppendChildrenRequestSchema

from notion_python_sdk.type.block_append_children_request_children import BlockAppendChildrenRequestChildren
from notion_python_sdk.type.block_append_children_request import BlockAppendChildrenRequest
from notion_python_sdk.type.block_append_children_response import BlockAppendChildrenResponse

from ...api_client import Dictionary
from notion_python_sdk.pydantic.block_append_children_request_children import BlockAppendChildrenRequestChildren as BlockAppendChildrenRequestChildrenPydantic
from notion_python_sdk.pydantic.block_append_children_request import BlockAppendChildrenRequest as BlockAppendChildrenRequestPydantic
from notion_python_sdk.pydantic.block_append_children_response import BlockAppendChildrenResponse as BlockAppendChildrenResponsePydantic

from . import path

# Header params
NotionVersionSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'Notion-Version': typing.Union[NotionVersionSchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_notion_version = api_client.HeaderParameter(
    name="Notion-Version",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NotionVersionSchema,
    required=True,
)
# Path params
BlockIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'block_id': typing.Union[BlockIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_block_id = api_client.PathParameter(
    name="block_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=BlockIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = BlockAppendChildrenRequestSchema


request_body_block_append_children_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = BlockAppendChildrenResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: BlockAppendChildrenResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: BlockAppendChildrenResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _append_children_mapped_args(
        self,
        children: BlockAppendChildrenRequestChildren,
        block_id: str,
        notion_version: str,
        after: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if children is not None:
            _body["children"] = children
        if after is not None:
            _body["after"] = after
        args.body = _body
        if notion_version is not None:
            _header_params["Notion-Version"] = notion_version
        if block_id is not None:
            _path_params["block_id"] = block_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aappend_children_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Append block children
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_block_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_notion_version,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/blocks/{block_id}/children',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_block_append_children_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _append_children_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Append block children
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_block_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_notion_version,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/blocks/{block_id}/children',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_block_append_children_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class AppendChildrenRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aappend_children(
        self,
        children: BlockAppendChildrenRequestChildren,
        block_id: str,
        notion_version: str,
        after: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._append_children_mapped_args(
            children=children,
            block_id=block_id,
            notion_version=notion_version,
            after=after,
        )
        return await self._aappend_children_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def append_children(
        self,
        children: BlockAppendChildrenRequestChildren,
        block_id: str,
        notion_version: str,
        after: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._append_children_mapped_args(
            children=children,
            block_id=block_id,
            notion_version=notion_version,
            after=after,
        )
        return self._append_children_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class AppendChildren(BaseApi):

    async def aappend_children(
        self,
        children: BlockAppendChildrenRequestChildren,
        block_id: str,
        notion_version: str,
        after: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> BlockAppendChildrenResponsePydantic:
        raw_response = await self.raw.aappend_children(
            children=children,
            block_id=block_id,
            notion_version=notion_version,
            after=after,
            **kwargs,
        )
        if validate:
            return BlockAppendChildrenResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BlockAppendChildrenResponsePydantic, raw_response.body)
    
    
    def append_children(
        self,
        children: BlockAppendChildrenRequestChildren,
        block_id: str,
        notion_version: str,
        after: typing.Optional[str] = None,
        validate: bool = False,
    ) -> BlockAppendChildrenResponsePydantic:
        raw_response = self.raw.append_children(
            children=children,
            block_id=block_id,
            notion_version=notion_version,
            after=after,
        )
        if validate:
            return BlockAppendChildrenResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BlockAppendChildrenResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        children: BlockAppendChildrenRequestChildren,
        block_id: str,
        notion_version: str,
        after: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._append_children_mapped_args(
            children=children,
            block_id=block_id,
            notion_version=notion_version,
            after=after,
        )
        return await self._aappend_children_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        children: BlockAppendChildrenRequestChildren,
        block_id: str,
        notion_version: str,
        after: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._append_children_mapped_args(
            children=children,
            block_id=block_id,
            notion_version=notion_version,
            after=after,
        )
        return self._append_children_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

