from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CollectionApiKeyAccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLLECTION_API_KEY_ACCESS_TYPE_UNSPECIFIED: _ClassVar[CollectionApiKeyAccessType]
    COLLECTION_API_KEY_ACCESS_TYPE_READ_ONLY: _ClassVar[CollectionApiKeyAccessType]
    COLLECTION_API_KEY_ACCESS_TYPE_READ_WRITE: _ClassVar[CollectionApiKeyAccessType]
COLLECTION_API_KEY_ACCESS_TYPE_UNSPECIFIED: CollectionApiKeyAccessType
COLLECTION_API_KEY_ACCESS_TYPE_READ_ONLY: CollectionApiKeyAccessType
COLLECTION_API_KEY_ACCESS_TYPE_READ_WRITE: CollectionApiKeyAccessType

class ListCollectionApiKeysRequest(_message.Message):
    __slots__ = ("account_id", "collection_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    collection_id: str
    def __init__(self, account_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...

class ListCollectionApiKeysResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CollectionApiKey]
    def __init__(self, items: _Optional[_Iterable[_Union[CollectionApiKey, _Mapping]]] = ...) -> None: ...

class CreateCollectionApiKeyRequest(_message.Message):
    __slots__ = ("account_id", "collection_id", "collection_api_key")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_API_KEY_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    collection_id: str
    collection_api_key: CollectionApiKey
    def __init__(self, account_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., collection_api_key: _Optional[_Union[CollectionApiKey, _Mapping]] = ...) -> None: ...

class CreateCollectionApiKeyResponse(_message.Message):
    __slots__ = ("collection_api_key",)
    COLLECTION_API_KEY_FIELD_NUMBER: _ClassVar[int]
    collection_api_key: CollectionApiKey
    def __init__(self, collection_api_key: _Optional[_Union[CollectionApiKey, _Mapping]] = ...) -> None: ...

class DeleteCollectionApiKeyRequest(_message.Message):
    __slots__ = ("account_id", "collection_id", "collection_api_key_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    collection_id: str
    collection_api_key_id: str
    def __init__(self, account_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., collection_api_key_id: _Optional[str] = ...) -> None: ...

class DeleteCollectionApiKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CollectionApiKey(_message.Message):
    __slots__ = ("id", "account_id", "created_at", "collection_id", "name", "expires_at", "access_type", "created_by_email", "postfix", "key")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    POSTFIX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    created_at: _timestamp_pb2.Timestamp
    collection_id: str
    name: str
    expires_at: _timestamp_pb2.Timestamp
    access_type: CollectionApiKeyAccessType
    created_by_email: str
    postfix: str
    key: str
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., collection_id: _Optional[str] = ..., name: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., access_type: _Optional[_Union[CollectionApiKeyAccessType, str]] = ..., created_by_email: _Optional[str] = ..., postfix: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...
