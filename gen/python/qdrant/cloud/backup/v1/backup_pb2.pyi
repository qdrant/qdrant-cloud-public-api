from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListBackupsRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "schedule_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    schedule_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., schedule_id: _Optional[str] = ...) -> None: ...

class ListBackupsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Backup]
    def __init__(self, items: _Optional[_Iterable[_Union[Backup, _Mapping]]] = ...) -> None: ...

class CreateBackupRequest(_message.Message):
    __slots__ = ("backup",)
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    backup: Backup
    def __init__(self, backup: _Optional[_Union[Backup, _Mapping]] = ...) -> None: ...

class CreateBackupResponse(_message.Message):
    __slots__ = ("backup",)
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    backup: Backup
    def __init__(self, backup: _Optional[_Union[Backup, _Mapping]] = ...) -> None: ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ("account_id", "backup_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    backup_id: str
    def __init__(self, account_id: _Optional[str] = ..., backup_id: _Optional[str] = ...) -> None: ...

class DeleteBackupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestoreBackupRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "backup_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    backup_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., backup_id: _Optional[str] = ...) -> None: ...

class RestoreBackupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Backup(_message.Message):
    __slots__ = ("id", "created_at", "account_id", "cluster_id", "name", "schedule_id", "status", "deleted_at", "creation_duration")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    account_id: str
    cluster_id: str
    name: str
    schedule_id: str
    status: str
    deleted_at: _timestamp_pb2.Timestamp
    creation_duration: _duration_pb2.Duration
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., name: _Optional[str] = ..., schedule_id: _Optional[str] = ..., status: _Optional[str] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., creation_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
