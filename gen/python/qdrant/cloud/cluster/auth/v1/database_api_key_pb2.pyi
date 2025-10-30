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

class ListDatabaseApiKeysRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class ListDatabaseApiKeysResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DatabaseApiKey]
    def __init__(self, items: _Optional[_Iterable[_Union[DatabaseApiKey, _Mapping]]] = ...) -> None: ...

class CreateDatabaseApiKeyRequest(_message.Message):
    __slots__ = ()
    DATABASE_API_KEY_FIELD_NUMBER: _ClassVar[int]
    database_api_key: DatabaseApiKey
    def __init__(self, database_api_key: _Optional[_Union[DatabaseApiKey, _Mapping]] = ...) -> None: ...

class CreateDatabaseApiKeyResponse(_message.Message):
    __slots__ = ()
    DATABASE_API_KEY_FIELD_NUMBER: _ClassVar[int]
    database_api_key: DatabaseApiKey
    def __init__(self, database_api_key: _Optional[_Union[DatabaseApiKey, _Mapping]] = ...) -> None: ...

class DeleteDatabaseApiKeyRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    database_api_key_id: str
    def __init__(self, account_id: _Optional[str] = ..., database_api_key_id: _Optional[str] = ...) -> None: ...

class DeleteDatabaseApiKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DatabaseApiKey(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IDS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    created_at: _timestamp_pb2.Timestamp
    cluster_ids: _containers.RepeatedScalarFieldContainer[str]
    prefix: str
    key: str
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cluster_ids: _Optional[_Iterable[str]] = ..., prefix: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...
