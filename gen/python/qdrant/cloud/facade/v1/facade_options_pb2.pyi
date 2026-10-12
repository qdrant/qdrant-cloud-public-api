from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
FACADE_FIELD_NUMBER: _ClassVar[int]
facade: _descriptor.FieldDescriptor
FACADE_FIELD_FIELD_NUMBER: _ClassVar[int]
facade_field: _descriptor.FieldDescriptor

class FacadeMethodOptions(_message.Message):
    __slots__ = ("description", "title")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    description: str
    title: str
    def __init__(self, description: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class FacadeFieldOptions(_message.Message):
    __slots__ = ("hide", "description")
    HIDE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    hide: bool
    description: str
    def __init__(self, hide: _Optional[bool] = ..., description: _Optional[str] = ...) -> None: ...
