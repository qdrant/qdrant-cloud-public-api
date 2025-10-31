import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.event.v1 import events_pb2 as _events_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListManagementKeysRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListManagementKeysResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ManagementKey]
    def __init__(self, items: _Optional[_Iterable[_Union[ManagementKey, _Mapping]]] = ...) -> None: ...

class CreateManagementKeyRequest(_message.Message):
    __slots__ = ()
    MANAGEMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    management_key: ManagementKey
    def __init__(self, management_key: _Optional[_Union[ManagementKey, _Mapping]] = ...) -> None: ...

class CreateManagementKeyResponse(_message.Message):
    __slots__ = ()
    MANAGEMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    management_key: ManagementKey
    def __init__(self, management_key: _Optional[_Union[ManagementKey, _Mapping]] = ...) -> None: ...

class DeleteManagementKeyRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    management_key_id: str
    def __init__(self, account_id: _Optional[str] = ..., management_key_id: _Optional[str] = ...) -> None: ...

class DeleteManagementKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ManagementKey(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    created_at: _timestamp_pb2.Timestamp
    prefix: str
    key: str
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., prefix: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...
