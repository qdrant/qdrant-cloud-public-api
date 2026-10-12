from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
GRAPHQL_FIELD_NUMBER: _ClassVar[int]
graphql: _descriptor.FieldDescriptor
GRAPHQL_FIELD_FIELD_NUMBER: _ClassVar[int]
graphql_field: _descriptor.FieldDescriptor

class GraphqlMethodOptions(_message.Message):
    __slots__ = ("field", "response_path")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_PATH_FIELD_NUMBER: _ClassVar[int]
    field: str
    response_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, field: _Optional[str] = ..., response_path: _Optional[_Iterable[str]] = ...) -> None: ...

class GraphqlFieldOptions(_message.Message):
    __slots__ = ("arg_name",)
    ARG_NAME_FIELD_NUMBER: _ClassVar[int]
    arg_name: str
    def __init__(self, arg_name: _Optional[str] = ...) -> None: ...
