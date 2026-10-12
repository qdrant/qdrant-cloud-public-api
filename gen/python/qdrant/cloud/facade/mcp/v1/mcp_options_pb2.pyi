from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
MCP_TOOL_FIELD_NUMBER: _ClassVar[int]
mcp_tool: _descriptor.FieldDescriptor

class McpToolOptions(_message.Message):
    __slots__ = ("name", "allow_mutation")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MUTATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_mutation: bool
    def __init__(self, name: _Optional[str] = ..., allow_mutation: _Optional[bool] = ...) -> None: ...
