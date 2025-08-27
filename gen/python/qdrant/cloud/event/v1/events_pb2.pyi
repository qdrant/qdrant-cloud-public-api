import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_TYPE_UNSPECIFIED: _ClassVar[EventType]
    EVENT_TYPE_CREATED: _ClassVar[EventType]
    EVENT_TYPE_UPDATED: _ClassVar[EventType]
    EVENT_TYPE_DELETED: _ClassVar[EventType]
    EVENT_TYPE_ACTION: _ClassVar[EventType]
EVENT_TYPE_UNSPECIFIED: EventType
EVENT_TYPE_CREATED: EventType
EVENT_TYPE_UPDATED: EventType
EVENT_TYPE_DELETED: EventType
EVENT_TYPE_ACTION: EventType
EVENT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
event_options: _descriptor.FieldDescriptor

class EventOptions(_message.Message):
    __slots__ = ("event_type", "resource_type", "status_only", "resource_id_field", "resource_url_template", "action_type", "additional_context_fields")
    class AdditionalContextFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CONTEXT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    event_type: EventType
    resource_type: str
    status_only: bool
    resource_id_field: str
    resource_url_template: str
    action_type: str
    additional_context_fields: _containers.ScalarMap[str, str]
    def __init__(self, event_type: _Optional[_Union[EventType, str]] = ..., resource_type: _Optional[str] = ..., status_only: _Optional[bool] = ..., resource_id_field: _Optional[str] = ..., resource_url_template: _Optional[str] = ..., action_type: _Optional[str] = ..., additional_context_fields: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("id", "created_at", "actor_id", "actor_type", "account_id", "event_type", "resource_type", "status_only", "resource_id", "resource_url", "action_type", "additional_context")
    class AdditionalContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    actor_id: str
    actor_type: _common_pb2.ActorType
    account_id: str
    event_type: EventType
    resource_type: str
    status_only: bool
    resource_id: str
    resource_url: str
    action_type: str
    additional_context: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., actor_id: _Optional[str] = ..., actor_type: _Optional[_Union[_common_pb2.ActorType, str]] = ..., account_id: _Optional[str] = ..., event_type: _Optional[_Union[EventType, str]] = ..., resource_type: _Optional[str] = ..., status_only: _Optional[bool] = ..., resource_id: _Optional[str] = ..., resource_url: _Optional[str] = ..., action_type: _Optional[str] = ..., additional_context: _Optional[_Mapping[str, str]] = ...) -> None: ...
