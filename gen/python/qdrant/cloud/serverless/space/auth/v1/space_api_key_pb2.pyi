import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.event.v1 import events_pb2 as _events_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceApiKeyStatePhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_API_KEY_STATE_PHASE_UNSPECIFIED: _ClassVar[SpaceApiKeyStatePhase]
    SPACE_API_KEY_STATE_PHASE_PROCESSING: _ClassVar[SpaceApiKeyStatePhase]
    SPACE_API_KEY_STATE_PHASE_READY: _ClassVar[SpaceApiKeyStatePhase]
    SPACE_API_KEY_STATE_PHASE_DISABLED: _ClassVar[SpaceApiKeyStatePhase]
    SPACE_API_KEY_STATE_PHASE_DELETING: _ClassVar[SpaceApiKeyStatePhase]

class GlobalAccessRuleAccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GLOBAL_ACCESS_RULE_ACCESS_TYPE_UNSPECIFIED: _ClassVar[GlobalAccessRuleAccessType]
    GLOBAL_ACCESS_RULE_ACCESS_TYPE_METRICS_READ_ONLY: _ClassVar[GlobalAccessRuleAccessType]
    GLOBAL_ACCESS_RULE_ACCESS_TYPE_READ_ONLY: _ClassVar[GlobalAccessRuleAccessType]
    GLOBAL_ACCESS_RULE_ACCESS_TYPE_MANAGE: _ClassVar[GlobalAccessRuleAccessType]

class CollectionAccessRuleAccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLLECTION_ACCESS_RULE_ACCESS_TYPE_UNSPECIFIED: _ClassVar[CollectionAccessRuleAccessType]
    COLLECTION_ACCESS_RULE_ACCESS_TYPE_READ_ONLY: _ClassVar[CollectionAccessRuleAccessType]
    COLLECTION_ACCESS_RULE_ACCESS_TYPE_READ_WRITE: _ClassVar[CollectionAccessRuleAccessType]
SPACE_API_KEY_STATE_PHASE_UNSPECIFIED: SpaceApiKeyStatePhase
SPACE_API_KEY_STATE_PHASE_PROCESSING: SpaceApiKeyStatePhase
SPACE_API_KEY_STATE_PHASE_READY: SpaceApiKeyStatePhase
SPACE_API_KEY_STATE_PHASE_DISABLED: SpaceApiKeyStatePhase
SPACE_API_KEY_STATE_PHASE_DELETING: SpaceApiKeyStatePhase
GLOBAL_ACCESS_RULE_ACCESS_TYPE_UNSPECIFIED: GlobalAccessRuleAccessType
GLOBAL_ACCESS_RULE_ACCESS_TYPE_METRICS_READ_ONLY: GlobalAccessRuleAccessType
GLOBAL_ACCESS_RULE_ACCESS_TYPE_READ_ONLY: GlobalAccessRuleAccessType
GLOBAL_ACCESS_RULE_ACCESS_TYPE_MANAGE: GlobalAccessRuleAccessType
COLLECTION_ACCESS_RULE_ACCESS_TYPE_UNSPECIFIED: CollectionAccessRuleAccessType
COLLECTION_ACCESS_RULE_ACCESS_TYPE_READ_ONLY: CollectionAccessRuleAccessType
COLLECTION_ACCESS_RULE_ACCESS_TYPE_READ_WRITE: CollectionAccessRuleAccessType

class ListSpaceApiKeysRequest(_message.Message):
    __slots__ = ("account_id", "space_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...

class ListSpaceApiKeysResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SpaceApiKey]
    def __init__(self, items: _Optional[_Iterable[_Union[SpaceApiKey, _Mapping]]] = ...) -> None: ...

class CreateSpaceApiKeyRequest(_message.Message):
    __slots__ = ("space_api_key",)
    SPACE_API_KEY_FIELD_NUMBER: _ClassVar[int]
    space_api_key: SpaceApiKey
    def __init__(self, space_api_key: _Optional[_Union[SpaceApiKey, _Mapping]] = ...) -> None: ...

class CreateSpaceApiKeyResponse(_message.Message):
    __slots__ = ("space_api_key",)
    SPACE_API_KEY_FIELD_NUMBER: _ClassVar[int]
    space_api_key: SpaceApiKey
    def __init__(self, space_api_key: _Optional[_Union[SpaceApiKey, _Mapping]] = ...) -> None: ...

class DeleteSpaceApiKeyRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "space_api_key_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    space_api_key_id: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., space_api_key_id: _Optional[str] = ...) -> None: ...

class DeleteSpaceApiKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceApiKey(_message.Message):
    __slots__ = ("id", "account_id", "created_at", "space_id", "name", "expires_at", "access_rules", "created_by", "deleted_by", "deleted_at", "postfix", "key", "state", "revoked_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RULES_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    POSTFIX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    created_at: _timestamp_pb2.Timestamp
    space_id: str
    name: str
    expires_at: _timestamp_pb2.Timestamp
    access_rules: _containers.RepeatedCompositeFieldContainer[AccessRule]
    created_by: _common_pb2.Caller
    deleted_by: _common_pb2.Caller
    deleted_at: _timestamp_pb2.Timestamp
    postfix: str
    key: str
    state: SpaceApiKeyState
    revoked_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., space_id: _Optional[str] = ..., name: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., access_rules: _Optional[_Iterable[_Union[AccessRule, _Mapping]]] = ..., created_by: _Optional[_Union[_common_pb2.Caller, _Mapping]] = ..., deleted_by: _Optional[_Union[_common_pb2.Caller, _Mapping]] = ..., deleted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., postfix: _Optional[str] = ..., key: _Optional[str] = ..., state: _Optional[_Union[SpaceApiKeyState, _Mapping]] = ..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SpaceApiKeyState(_message.Message):
    __slots__ = ("phase", "reason")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    phase: SpaceApiKeyStatePhase
    reason: str
    def __init__(self, phase: _Optional[_Union[SpaceApiKeyStatePhase, str]] = ..., reason: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("collection_name", "access_type")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    access_type: CollectionAccessRuleAccessType
    def __init__(self, collection_name: _Optional[str] = ..., access_type: _Optional[_Union[CollectionAccessRuleAccessType, str]] = ...) -> None: ...
