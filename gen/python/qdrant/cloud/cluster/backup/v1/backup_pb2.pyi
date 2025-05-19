from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKUP_STATUS_UNSPECIFIED: _ClassVar[BackupStatus]
    BACKUP_STATUS_RUNNING: _ClassVar[BackupStatus]
    BACKUP_STATUS_SKIPPED: _ClassVar[BackupStatus]
    BACKUP_STATUS_FAILED: _ClassVar[BackupStatus]
    BACKUP_STATUS_SUCCEEDED: _ClassVar[BackupStatus]
    BACKUP_STATUS_FAILED_TO_SYNC: _ClassVar[BackupStatus]
    BACKUP_STATUS_NOT_FOUND: _ClassVar[BackupStatus]
    BACKUP_STATUS_UNKNOWN: _ClassVar[BackupStatus]

class BackupScheduleStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKUP_SCHEDULE_STATUS_UNSPECIFIED: _ClassVar[BackupScheduleStatus]
    BACKUP_SCHEDULE_STATUS_ACTIVE: _ClassVar[BackupScheduleStatus]
    BACKUP_SCHEDULE_STATUS_FAILED_TO_SYNC: _ClassVar[BackupScheduleStatus]
    BACKUP_SCHEDULE_STATUS_NOT_FOUND: _ClassVar[BackupScheduleStatus]
    BACKUP_SCHEDULE_STATUS_UNKNOWN: _ClassVar[BackupScheduleStatus]

class BackupRestoreStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKUP_RESTORE_STATUS_UNSPECIFIED: _ClassVar[BackupRestoreStatus]
    BACKUP_RESTORE_STATUS_RUNNING: _ClassVar[BackupRestoreStatus]
    BACKUP_RESTORE_STATUS_FAILED: _ClassVar[BackupRestoreStatus]
    BACKUP_RESTORE_STATUS_SUCCEEDED: _ClassVar[BackupRestoreStatus]
    BACKUP_RESTORE_STATUS_FAILED_TO_SYNC: _ClassVar[BackupRestoreStatus]
    BACKUP_RESTORE_STATUS_NOT_FOUND: _ClassVar[BackupRestoreStatus]
    BACKUP_RESTORE_STATUS_UNKNOWN: _ClassVar[BackupRestoreStatus]
BACKUP_STATUS_UNSPECIFIED: BackupStatus
BACKUP_STATUS_RUNNING: BackupStatus
BACKUP_STATUS_SKIPPED: BackupStatus
BACKUP_STATUS_FAILED: BackupStatus
BACKUP_STATUS_SUCCEEDED: BackupStatus
BACKUP_STATUS_FAILED_TO_SYNC: BackupStatus
BACKUP_STATUS_NOT_FOUND: BackupStatus
BACKUP_STATUS_UNKNOWN: BackupStatus
BACKUP_SCHEDULE_STATUS_UNSPECIFIED: BackupScheduleStatus
BACKUP_SCHEDULE_STATUS_ACTIVE: BackupScheduleStatus
BACKUP_SCHEDULE_STATUS_FAILED_TO_SYNC: BackupScheduleStatus
BACKUP_SCHEDULE_STATUS_NOT_FOUND: BackupScheduleStatus
BACKUP_SCHEDULE_STATUS_UNKNOWN: BackupScheduleStatus
BACKUP_RESTORE_STATUS_UNSPECIFIED: BackupRestoreStatus
BACKUP_RESTORE_STATUS_RUNNING: BackupRestoreStatus
BACKUP_RESTORE_STATUS_FAILED: BackupRestoreStatus
BACKUP_RESTORE_STATUS_SUCCEEDED: BackupRestoreStatus
BACKUP_RESTORE_STATUS_FAILED_TO_SYNC: BackupRestoreStatus
BACKUP_RESTORE_STATUS_NOT_FOUND: BackupRestoreStatus
BACKUP_RESTORE_STATUS_UNKNOWN: BackupRestoreStatus

class ListBackupsRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "backup_schedule_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    backup_schedule_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., backup_schedule_id: _Optional[str] = ...) -> None: ...

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

class ListBackupRestoresRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListBackupRestoresResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[BackupRestore]
    def __init__(self, items: _Optional[_Iterable[_Union[BackupRestore, _Mapping]]] = ...) -> None: ...

class RestoreBackupRequest(_message.Message):
    __slots__ = ("account_id", "backup_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    backup_id: str
    def __init__(self, account_id: _Optional[str] = ..., backup_id: _Optional[str] = ...) -> None: ...

class RestoreBackupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListBackupSchedulesRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class ListBackupSchedulesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[BackupSchedule]
    def __init__(self, items: _Optional[_Iterable[_Union[BackupSchedule, _Mapping]]] = ...) -> None: ...

class GetBackupScheduleRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "backup_schedule_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    backup_schedule_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., backup_schedule_id: _Optional[str] = ...) -> None: ...

class GetBackupScheduleResponse(_message.Message):
    __slots__ = ("backup_schedule",)
    BACKUP_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    backup_schedule: BackupSchedule
    def __init__(self, backup_schedule: _Optional[_Union[BackupSchedule, _Mapping]] = ...) -> None: ...

class CreateBackupScheduleRequest(_message.Message):
    __slots__ = ("backup_schedule",)
    BACKUP_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    backup_schedule: BackupSchedule
    def __init__(self, backup_schedule: _Optional[_Union[BackupSchedule, _Mapping]] = ...) -> None: ...

class CreateBackupScheduleResponse(_message.Message):
    __slots__ = ("backup_schedule",)
    BACKUP_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    backup_schedule: BackupSchedule
    def __init__(self, backup_schedule: _Optional[_Union[BackupSchedule, _Mapping]] = ...) -> None: ...

class UpdateBackupScheduleRequest(_message.Message):
    __slots__ = ("backup_schedule",)
    BACKUP_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    backup_schedule: BackupSchedule
    def __init__(self, backup_schedule: _Optional[_Union[BackupSchedule, _Mapping]] = ...) -> None: ...

class UpdateBackupScheduleResponse(_message.Message):
    __slots__ = ("backup_schedule",)
    BACKUP_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    backup_schedule: BackupSchedule
    def __init__(self, backup_schedule: _Optional[_Union[BackupSchedule, _Mapping]] = ...) -> None: ...

class DeleteBackupScheduleRequest(_message.Message):
    __slots__ = ("account_id", "backup_schedule_id", "delete_backups")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    backup_schedule_id: str
    delete_backups: bool
    def __init__(self, account_id: _Optional[str] = ..., backup_schedule_id: _Optional[str] = ..., delete_backups: bool = ...) -> None: ...

class DeleteBackupScheduleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Backup(_message.Message):
    __slots__ = ("id", "created_at", "account_id", "cluster_id", "name", "status", "deleted_at", "backup_duration")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    account_id: str
    cluster_id: str
    name: str
    status: BackupStatus
    deleted_at: _timestamp_pb2.Timestamp
    backup_duration: _duration_pb2.Duration
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[BackupStatus, str]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., backup_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class BackupSchedule(_message.Message):
    __slots__ = ("id", "created_at", "account_id", "cluster_id", "schedule", "retention_period", "deleted_at", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    account_id: str
    cluster_id: str
    schedule: str
    retention_period: _duration_pb2.Duration
    deleted_at: _timestamp_pb2.Timestamp
    status: BackupScheduleStatus
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., schedule: _Optional[str] = ..., retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[BackupScheduleStatus, str]] = ...) -> None: ...

class BackupRestore(_message.Message):
    __slots__ = ("id", "created_at", "account_id", "cluster_id", "backup_id", "status", "deleted_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    account_id: str
    cluster_id: str
    backup_id: str
    status: BackupRestoreStatus
    deleted_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., backup_id: _Optional[str] = ..., status: _Optional[_Union[BackupRestoreStatus, str]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
