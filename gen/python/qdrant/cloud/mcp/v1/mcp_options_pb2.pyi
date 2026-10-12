from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
MCP_TOOL_FIELD_NUMBER: _ClassVar[int]
mcp_tool: _descriptor.FieldDescriptor

class McpToolOptions(_message.Message):
    __slots__ = ("name", "allow_mutation", "sensitive_response", "read_only_hint", "destructive_hint", "idempotent_hint")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MUTATION_FIELD_NUMBER: _ClassVar[int]
    SENSITIVE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_HINT_FIELD_NUMBER: _ClassVar[int]
    DESTRUCTIVE_HINT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_HINT_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_mutation: bool
    sensitive_response: bool
    read_only_hint: bool
    destructive_hint: bool
    idempotent_hint: bool
    def __init__(self, name: _Optional[str] = ..., allow_mutation: _Optional[bool] = ..., sensitive_response: _Optional[bool] = ..., read_only_hint: _Optional[bool] = ..., destructive_hint: _Optional[bool] = ..., idempotent_hint: _Optional[bool] = ...) -> None: ...
