from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Quantity(_message.Message):
    __slots__ = ("string",)
    STRING_FIELD_NUMBER: _ClassVar[int]
    string: str
    def __init__(self, string: _Optional[str] = ...) -> None: ...

class QuantityValue(_message.Message):
    __slots__ = ("string",)
    STRING_FIELD_NUMBER: _ClassVar[int]
    string: str
    def __init__(self, string: _Optional[str] = ...) -> None: ...
