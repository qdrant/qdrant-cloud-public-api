from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetQuotasRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class AccountQuota(_message.Message):
    __slots__ = ("account_id", "max_spaces", "max_collections_per_space", "platform_max_storage_bytes_per_space", "used_spaces", "used_storage_bytes")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_SPACES_FIELD_NUMBER: _ClassVar[int]
    MAX_COLLECTIONS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_MAX_STORAGE_BYTES_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    USED_SPACES_FIELD_NUMBER: _ClassVar[int]
    USED_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    max_spaces: int
    max_collections_per_space: int
    platform_max_storage_bytes_per_space: int
    used_spaces: int
    used_storage_bytes: int
    def __init__(self, account_id: _Optional[str] = ..., max_spaces: _Optional[int] = ..., max_collections_per_space: _Optional[int] = ..., platform_max_storage_bytes_per_space: _Optional[int] = ..., used_spaces: _Optional[int] = ..., used_storage_bytes: _Optional[int] = ...) -> None: ...

class GetQuotasResponse(_message.Message):
    __slots__ = ("quota",)
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    quota: AccountQuota
    def __init__(self, quota: _Optional[_Union[AccountQuota, _Mapping]] = ...) -> None: ...
