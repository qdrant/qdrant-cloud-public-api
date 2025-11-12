from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTOR_TYPE_UNSPECIFIED: _ClassVar[ActorType]
    ACTOR_TYPE_USER: _ClassVar[ActorType]
    ACTOR_TYPE_MANAGEMENT_KEY: _ClassVar[ActorType]
    ACTOR_TYPE_SERVICE_ACCOUNT: _ClassVar[ActorType]
ACTOR_TYPE_UNSPECIFIED: ActorType
ACTOR_TYPE_USER: ActorType
ACTOR_TYPE_MANAGEMENT_KEY: ActorType
ACTOR_TYPE_SERVICE_ACCOUNT: ActorType
PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
permissions: _descriptor.FieldDescriptor
ACCOUNT_ID_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
account_id_expression: _descriptor.FieldDescriptor
REQUIRES_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
requires_authentication: _descriptor.FieldDescriptor
SUPPORTED_ACTOR_TYPES_FIELD_NUMBER: _ClassVar[int]
supported_actor_types: _descriptor.FieldDescriptor
REQUIRES_ALL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
requires_all_permissions: _descriptor.FieldDescriptor
MAX_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
max_message_size: _descriptor.FieldDescriptor
LOG_FIELDS_FIELD_NUMBER: _ClassVar[int]
log_fields: _descriptor.FieldDescriptor

class LogField(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_expression: str
    def __init__(self, name: _Optional[str] = ..., field_expression: _Optional[str] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ()
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    patch: int
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., patch: _Optional[int] = ...) -> None: ...

class SecretKeyRef(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    key: str
    def __init__(self, name: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class KeyValue(_message.Message):
    __slots__ = ()
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
