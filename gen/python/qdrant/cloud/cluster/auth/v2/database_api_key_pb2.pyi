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

class GlobalAccessRuleAccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GLOBAL_ACCESS_RULE_ACCESS_TYPE_UNSPECIFIED: _ClassVar[GlobalAccessRuleAccessType]
    GLOBAL_ACCESS_RULE_ACCESS_TYPE_READ_ONLY: _ClassVar[GlobalAccessRuleAccessType]
    GLOBAL_ACCESS_RULE_ACCESS_TYPE_MANAGE: _ClassVar[GlobalAccessRuleAccessType]

class CollectionAccessRuleAccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLLECTION_ACCESS_RULE_ACCESS_TYPE_UNSPECIFIED: _ClassVar[CollectionAccessRuleAccessType]
    COLLECTION_ACCESS_RULE_ACCESS_TYPE_READ_ONLY: _ClassVar[CollectionAccessRuleAccessType]
    COLLECTION_ACCESS_RULE_ACCESS_TYPE_READ_WRITE: _ClassVar[CollectionAccessRuleAccessType]
GLOBAL_ACCESS_RULE_ACCESS_TYPE_UNSPECIFIED: GlobalAccessRuleAccessType
GLOBAL_ACCESS_RULE_ACCESS_TYPE_READ_ONLY: GlobalAccessRuleAccessType
GLOBAL_ACCESS_RULE_ACCESS_TYPE_MANAGE: GlobalAccessRuleAccessType
COLLECTION_ACCESS_RULE_ACCESS_TYPE_UNSPECIFIED: CollectionAccessRuleAccessType
COLLECTION_ACCESS_RULE_ACCESS_TYPE_READ_ONLY: CollectionAccessRuleAccessType
COLLECTION_ACCESS_RULE_ACCESS_TYPE_READ_WRITE: CollectionAccessRuleAccessType

class ListDatabaseApiKeysRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class ListDatabaseApiKeysResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DatabaseApiKey]
    def __init__(self, items: _Optional[_Iterable[_Union[DatabaseApiKey, _Mapping]]] = ...) -> None: ...

class CreateDatabaseApiKeyRequest(_message.Message):
    __slots__ = ("database_api_key",)
    DATABASE_API_KEY_FIELD_NUMBER: _ClassVar[int]
    database_api_key: DatabaseApiKey
    def __init__(self, database_api_key: _Optional[_Union[DatabaseApiKey, _Mapping]] = ...) -> None: ...

class CreateDatabaseApiKeyResponse(_message.Message):
    __slots__ = ("database_api_key",)
    DATABASE_API_KEY_FIELD_NUMBER: _ClassVar[int]
    database_api_key: DatabaseApiKey
    def __init__(self, database_api_key: _Optional[_Union[DatabaseApiKey, _Mapping]] = ...) -> None: ...

class DeleteDatabaseApiKeyRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "database_api_key_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    database_api_key_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., database_api_key_id: _Optional[str] = ...) -> None: ...

class DeleteDatabaseApiKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DatabaseApiKey(_message.Message):
    __slots__ = ("id", "account_id", "created_at", "cluster_id", "name", "expires_at", "access_rules", "created_by_email", "postfix", "key")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RULES_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    POSTFIX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    created_at: _timestamp_pb2.Timestamp
    cluster_id: str
    name: str
    expires_at: _timestamp_pb2.Timestamp
    access_rules: _containers.RepeatedCompositeFieldContainer[AccessRule]
    created_by_email: str
    postfix: str
    key: str
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cluster_id: _Optional[str] = ..., name: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., access_rules: _Optional[_Iterable[_Union[AccessRule, _Mapping]]] = ..., created_by_email: _Optional[str] = ..., postfix: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class AccessRule(_message.Message):
    __slots__ = ("global_access", "collection_access")
    GLOBAL_ACCESS_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ACCESS_FIELD_NUMBER: _ClassVar[int]
    global_access: GlobalAccessRule
    collection_access: CollectionAccessRule
    def __init__(self, global_access: _Optional[_Union[GlobalAccessRule, _Mapping]] = ..., collection_access: _Optional[_Union[CollectionAccessRule, _Mapping]] = ...) -> None: ...

class GlobalAccessRule(_message.Message):
    __slots__ = ("access_type",)
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_type: GlobalAccessRuleAccessType
    def __init__(self, access_type: _Optional[_Union[GlobalAccessRuleAccessType, str]] = ...) -> None: ...

class CollectionAccessRule(_message.Message):
    __slots__ = ("collection_name", "access_type", "payload")
    class PayloadEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    access_type: CollectionAccessRuleAccessType
    payload: _containers.ScalarMap[str, str]
    def __init__(self, collection_name: _Optional[str] = ..., access_type: _Optional[_Union[CollectionAccessRuleAccessType, str]] = ..., payload: _Optional[_Mapping[str, str]] = ...) -> None: ...
