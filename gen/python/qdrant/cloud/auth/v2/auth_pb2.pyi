from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListManagementKeysRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListManagementKeysResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ManagementKey]
    def __init__(self, items: _Optional[_Iterable[_Union[ManagementKey, _Mapping]]] = ...) -> None: ...

class CreateManagementKeyRequest(_message.Message):
    __slots__ = ("management_key",)
    MANAGEMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    management_key: ManagementKey
    def __init__(self, management_key: _Optional[_Union[ManagementKey, _Mapping]] = ...) -> None: ...

class CreateManagementKeyResponse(_message.Message):
    __slots__ = ("management_key",)
    MANAGEMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    management_key: ManagementKey
    def __init__(self, management_key: _Optional[_Union[ManagementKey, _Mapping]] = ...) -> None: ...

class DeleteManagementKeyRequest(_message.Message):
    __slots__ = ("account_id", "management_key_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    management_key_id: str
    def __init__(self, account_id: _Optional[str] = ..., management_key_id: _Optional[str] = ...) -> None: ...

class DeleteManagementKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListApiKeysRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListApiKeysResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ApiKey]
    def __init__(self, items: _Optional[_Iterable[_Union[ApiKey, _Mapping]]] = ...) -> None: ...

class CreateApiKeyRequest(_message.Message):
    __slots__ = ("api_key",)
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: ApiKey
    def __init__(self, api_key: _Optional[_Union[ApiKey, _Mapping]] = ...) -> None: ...

class CreateApiKeyResponse(_message.Message):
    __slots__ = ("api_key",)
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: ApiKey
    def __init__(self, api_key: _Optional[_Union[ApiKey, _Mapping]] = ...) -> None: ...

class DeleteApiKeyRequest(_message.Message):
    __slots__ = ("account_id", "api_key_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    api_key_id: str
    def __init__(self, account_id: _Optional[str] = ..., api_key_id: _Optional[str] = ...) -> None: ...

class DeleteApiKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ManagementKey(_message.Message):
    __slots__ = ("id", "account_id", "created_at", "prefix", "key")
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
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., prefix: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class ApiKey(_message.Message):
    __slots__ = ("id", "account_id", "created_at", "cluster_ids", "prefix", "token")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IDS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    created_at: _timestamp_pb2.Timestamp
    cluster_ids: _containers.RepeatedScalarFieldContainer[str]
    prefix: str
    token: str
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cluster_ids: _Optional[_Iterable[str]] = ..., prefix: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...
