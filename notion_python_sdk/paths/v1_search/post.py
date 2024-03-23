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

from notion_python_sdk.model.search_by_title400_response import SearchByTitle400Response as SearchByTitle400ResponseSchema
from notion_python_sdk.model.search_by_title_request_sort import SearchByTitleRequestSort as SearchByTitleRequestSortSchema
from notion_python_sdk.model.search_by_title_response import SearchByTitleResponse as SearchByTitleResponseSchema
from notion_python_sdk.model.search_by_title_request_filter import SearchByTitleRequestFilter as SearchByTitleRequestFilterSchema
from notion_python_sdk.model.search_by_title_request import SearchByTitleRequest as SearchByTitleRequestSchema
from notion_python_sdk.model.search_by_title429_response import SearchByTitle429Response as SearchByTitle429ResponseSchema

from notion_python_sdk.type.search_by_title_request import SearchByTitleRequest
from notion_python_sdk.type.search_by_title_request_filter import SearchByTitleRequestFilter
from notion_python_sdk.type.search_by_title429_response import SearchByTitle429Response
from notion_python_sdk.type.search_by_title400_response import SearchByTitle400Response
from notion_python_sdk.type.search_by_title_response import SearchByTitleResponse
from notion_python_sdk.type.search_by_title_request_sort import SearchByTitleRequestSort

from ...api_client import Dictionary
from notion_python_sdk.pydantic.search_by_title400_response import SearchByTitle400Response as SearchByTitle400ResponsePydantic
from notion_python_sdk.pydantic.search_by_title_request_sort import SearchByTitleRequestSort as SearchByTitleRequestSortPydantic
from notion_python_sdk.pydantic.search_by_title429_response import SearchByTitle429Response as SearchByTitle429ResponsePydantic
from notion_python_sdk.pydantic.search_by_title_request_filter import SearchByTitleRequestFilter as SearchByTitleRequestFilterPydantic
from notion_python_sdk.pydantic.search_by_title_response import SearchByTitleResponse as SearchByTitleResponsePydantic
from notion_python_sdk.pydantic.search_by_title_request import SearchByTitleRequest as SearchByTitleRequestPydantic

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
# body param
SchemaForRequestBodyApplicationJson = SearchByTitleRequestSchema


request_body_search_by_title_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = SearchByTitleResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SearchByTitleResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SearchByTitleResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = SearchByTitle400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: SearchByTitle400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: SearchByTitle400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor429ResponseBodyApplicationJson = SearchByTitle429ResponseSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: SearchByTitle429Response


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: SearchByTitle429Response


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '429': _response_for_429,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _by_title_mapped_args(
        self,
        notion_version: str,
        query: typing.Optional[str] = None,
        sort: typing.Optional[SearchByTitleRequestSort] = None,
        filter: typing.Optional[SearchByTitleRequestFilter] = None,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if query is not None:
            _body["query"] = query
        if sort is not None:
            _body["sort"] = sort
        if filter is not None:
            _body["filter"] = filter
        if start_cursor is not None:
            _body["start_cursor"] = start_cursor
        if page_size is not None:
            _body["page_size"] = page_size
        args.body = _body
        if notion_version is not None:
            _header_params["Notion-Version"] = notion_version
        args.header = _header_params
        return args

    async def _aby_title_oapg(
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
        Search by title
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
            path_template='/v1/search',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_search_by_title_request.serialize(body, content_type)
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


    def _by_title_oapg(
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
        Search by title
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
            path_template='/v1/search',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_search_by_title_request.serialize(body, content_type)
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


class ByTitleRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aby_title(
        self,
        notion_version: str,
        query: typing.Optional[str] = None,
        sort: typing.Optional[SearchByTitleRequestSort] = None,
        filter: typing.Optional[SearchByTitleRequestFilter] = None,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._by_title_mapped_args(
            notion_version=notion_version,
            query=query,
            sort=sort,
            filter=filter,
            start_cursor=start_cursor,
            page_size=page_size,
        )
        return await self._aby_title_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def by_title(
        self,
        notion_version: str,
        query: typing.Optional[str] = None,
        sort: typing.Optional[SearchByTitleRequestSort] = None,
        filter: typing.Optional[SearchByTitleRequestFilter] = None,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._by_title_mapped_args(
            notion_version=notion_version,
            query=query,
            sort=sort,
            filter=filter,
            start_cursor=start_cursor,
            page_size=page_size,
        )
        return self._by_title_oapg(
            body=args.body,
            header_params=args.header,
        )

class ByTitle(BaseApi):

    async def aby_title(
        self,
        notion_version: str,
        query: typing.Optional[str] = None,
        sort: typing.Optional[SearchByTitleRequestSort] = None,
        filter: typing.Optional[SearchByTitleRequestFilter] = None,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> SearchByTitleResponsePydantic:
        raw_response = await self.raw.aby_title(
            notion_version=notion_version,
            query=query,
            sort=sort,
            filter=filter,
            start_cursor=start_cursor,
            page_size=page_size,
            **kwargs,
        )
        if validate:
            return SearchByTitleResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SearchByTitleResponsePydantic, raw_response.body)
    
    
    def by_title(
        self,
        notion_version: str,
        query: typing.Optional[str] = None,
        sort: typing.Optional[SearchByTitleRequestSort] = None,
        filter: typing.Optional[SearchByTitleRequestFilter] = None,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
    ) -> SearchByTitleResponsePydantic:
        raw_response = self.raw.by_title(
            notion_version=notion_version,
            query=query,
            sort=sort,
            filter=filter,
            start_cursor=start_cursor,
            page_size=page_size,
        )
        if validate:
            return SearchByTitleResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SearchByTitleResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        notion_version: str,
        query: typing.Optional[str] = None,
        sort: typing.Optional[SearchByTitleRequestSort] = None,
        filter: typing.Optional[SearchByTitleRequestFilter] = None,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._by_title_mapped_args(
            notion_version=notion_version,
            query=query,
            sort=sort,
            filter=filter,
            start_cursor=start_cursor,
            page_size=page_size,
        )
        return await self._aby_title_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        notion_version: str,
        query: typing.Optional[str] = None,
        sort: typing.Optional[SearchByTitleRequestSort] = None,
        filter: typing.Optional[SearchByTitleRequestFilter] = None,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._by_title_mapped_args(
            notion_version=notion_version,
            query=query,
            sort=sort,
            filter=filter,
            start_cursor=start_cursor,
            page_size=page_size,
        )
        return self._by_title_oapg(
            body=args.body,
            header_params=args.header,
        )

