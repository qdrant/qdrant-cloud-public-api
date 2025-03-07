from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCollectionKeysRequest(_message.Message):
    __slots__ = ("account_id", "collection_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    collection_id: str
    def __init__(self, account_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...

class ListCollectionKeysResponse(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[ApiKey]
    def __init__(self, keys: _Optional[_Iterable[_Union[ApiKey, _Mapping]]] = ...) -> None: ...

class CreateCollectionKeyRequest(_message.Message):
    __slots__ = ("account_id", "collection_id", "api_key")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    collection_id: str
    api_key: ApiKey
    def __init__(self, account_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., api_key: _Optional[_Union[ApiKey, _Mapping]] = ...) -> None: ...

class CreateCollectionKeyResponse(_message.Message):
    __slots__ = ("api_key",)
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: ApiKey
    def __init__(self, api_key: _Optional[_Union[ApiKey, _Mapping]] = ...) -> None: ...

class DeleteCollectionKeyRequest(_message.Message):
    __slots__ = ("account_id", "collection_id", "key_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    collection_id: str
    key_id: str
    def __init__(self, account_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., key_id: _Optional[str] = ...) -> None: ...

class DeleteCollectionKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ApiKey(_message.Message):
    __slots__ = ("id", "name", "key", "postfix", "created_at", "created_by_email", "access", "exp", "account_id", "collection_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    POSTFIX_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    key: str
    postfix: str
    created_at: _timestamp_pb2.Timestamp
    created_by_email: str
    access: str
    exp: int
    account_id: str
    collection_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., key: _Optional[str] = ..., postfix: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by_email: _Optional[str] = ..., access: _Optional[str] = ..., exp: _Optional[int] = ..., account_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...
