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

from notion_python_sdk.model.comment_create_new403_response import CommentCreateNew403Response as CommentCreateNew403ResponseSchema
from notion_python_sdk.model.comment_create_new_response import CommentCreateNewResponse as CommentCreateNewResponseSchema
from notion_python_sdk.model.comment_create_new_request import CommentCreateNewRequest as CommentCreateNewRequestSchema

from notion_python_sdk.type.comment_create_new403_response import CommentCreateNew403Response
from notion_python_sdk.type.comment_create_new_response import CommentCreateNewResponse
from notion_python_sdk.type.comment_create_new_request import CommentCreateNewRequest

from ...api_client import Dictionary
from notion_python_sdk.pydantic.comment_create_new_request import CommentCreateNewRequest as CommentCreateNewRequestPydantic
from notion_python_sdk.pydantic.comment_create_new_response import CommentCreateNewResponse as CommentCreateNewResponsePydantic
from notion_python_sdk.pydantic.comment_create_new403_response import CommentCreateNew403Response as CommentCreateNew403ResponsePydantic

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
# body param
SchemaForRequestBodyApplicationJson = CommentCreateNewRequestSchema


request_body_comment_create_new_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = CommentCreateNewResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CommentCreateNewResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CommentCreateNewResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = CommentCreateNew403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: CommentCreateNew403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: CommentCreateNew403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_mapped_args(
        self,
        rich_text: str,
        notion_version: str,
        parent: typing.Optional[str] = None,
        discussion_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if parent is not None:
            _body["parent"] = parent
        if discussion_id is not None:
            _body["discussion_id"] = discussion_id
        if rich_text is not None:
            _body["rich_text"] = rich_text
        args.body = _body
        if notion_version is not None:
            _header_params["Notion-Version"] = notion_version
        args.header = _header_params
        return args

    async def _acreate_new_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
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
        Create comment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/comments',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_comment_create_new_request.serialize(body, content_type)
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


    def _create_new_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
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
        Create comment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/comments',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_comment_create_new_request.serialize(body, content_type)
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


class CreateNewRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new(
        self,
        rich_text: str,
        notion_version: str,
        parent: typing.Optional[str] = None,
        discussion_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_mapped_args(
            rich_text=rich_text,
            notion_version=notion_version,
            parent=parent,
            discussion_id=discussion_id,
        )
        return await self._acreate_new_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def create_new(
        self,
        rich_text: str,
        notion_version: str,
        parent: typing.Optional[str] = None,
        discussion_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_mapped_args(
            rich_text=rich_text,
            notion_version=notion_version,
            parent=parent,
            discussion_id=discussion_id,
        )
        return self._create_new_oapg(
            body=args.body,
            header_params=args.header,
        )

class CreateNew(BaseApi):

    async def acreate_new(
        self,
        rich_text: str,
        notion_version: str,
        parent: typing.Optional[str] = None,
        discussion_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CommentCreateNewResponsePydantic:
        raw_response = await self.raw.acreate_new(
            rich_text=rich_text,
            notion_version=notion_version,
            parent=parent,
            discussion_id=discussion_id,
            **kwargs,
        )
        if validate:
            return CommentCreateNewResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CommentCreateNewResponsePydantic, raw_response.body)
    
    
    def create_new(
        self,
        rich_text: str,
        notion_version: str,
        parent: typing.Optional[str] = None,
        discussion_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CommentCreateNewResponsePydantic:
        raw_response = self.raw.create_new(
            rich_text=rich_text,
            notion_version=notion_version,
            parent=parent,
            discussion_id=discussion_id,
        )
        if validate:
            return CommentCreateNewResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CommentCreateNewResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        rich_text: str,
        notion_version: str,
        parent: typing.Optional[str] = None,
        discussion_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_mapped_args(
            rich_text=rich_text,
            notion_version=notion_version,
            parent=parent,
            discussion_id=discussion_id,
        )
        return await self._acreate_new_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        rich_text: str,
        notion_version: str,
        parent: typing.Optional[str] = None,
        discussion_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_mapped_args(
            rich_text=rich_text,
            notion_version=notion_version,
            parent=parent,
            discussion_id=discussion_id,
        )
        return self._create_new_oapg(
            body=args.body,
            header_params=args.header,
        )
