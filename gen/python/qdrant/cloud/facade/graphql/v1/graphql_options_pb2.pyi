from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GRAPHQL_FIELD_NUMBER: _ClassVar[int]
graphql: _descriptor.FieldDescriptor
GRAPHQL_NESTED_FIELD_NUMBER: _ClassVar[int]
graphql_nested: _descriptor.FieldDescriptor
GRAPHQL_FIELD_FIELD_NUMBER: _ClassVar[int]
graphql_field: _descriptor.FieldDescriptor

class GraphqlMethodOptions(_message.Message):
    __slots__ = ("field", "response_path")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_PATH_FIELD_NUMBER: _ClassVar[int]
    field: str
    response_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, field: _Optional[str] = ..., response_path: _Optional[_Iterable[str]] = ...) -> None: ...

class GraphqlNestedOptions(_message.Message):
    __slots__ = ("parent_type", "field", "response_path", "inputs", "batch", "description")
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_PATH_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    parent_type: str
    field: str
    response_path: _containers.RepeatedScalarFieldContainer[str]
    inputs: _containers.RepeatedCompositeFieldContainer[GraphqlNestedInput]
    batch: bool
    description: str
    def __init__(self, parent_type: _Optional[str] = ..., field: _Optional[str] = ..., response_path: _Optional[_Iterable[str]] = ..., inputs: _Optional[_Iterable[_Union[GraphqlNestedInput, _Mapping]]] = ..., batch: _Optional[bool] = ..., description: _Optional[str] = ...) -> None: ...

class GraphqlNestedInput(_message.Message):
    __slots__ = ("proto_path", "parent_path")
    PROTO_PATH_FIELD_NUMBER: _ClassVar[int]
    PARENT_PATH_FIELD_NUMBER: _ClassVar[int]
    proto_path: str
    parent_path: str
    def __init__(self, proto_path: _Optional[str] = ..., parent_path: _Optional[str] = ...) -> None: ...

class GraphqlFieldOptions(_message.Message):
    __slots__ = ("arg_name",)
    ARG_NAME_FIELD_NUMBER: _ClassVar[int]
    arg_name: str
    def __init__(self, arg_name: _Optional[str] = ...) -> None: ...
