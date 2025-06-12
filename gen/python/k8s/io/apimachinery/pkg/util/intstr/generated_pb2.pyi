from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IntOrString(_message.Message):
    __slots__ = ("type", "intVal", "strVal")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INTVAL_FIELD_NUMBER: _ClassVar[int]
    STRVAL_FIELD_NUMBER: _ClassVar[int]
    type: int
    intVal: int
    strVal: str
    def __init__(self, type: _Optional[int] = ..., intVal: _Optional[int] = ..., strVal: _Optional[str] = ...) -> None: ...
