import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.event.v1 import events_pb2 as _events_pb2
from qdrant.cloud.facade.graphql.v1 import graphql_options_pb2 as _graphql_options_pb2
from qdrant.cloud.facade.mcp.v1 import mcp_options_pb2 as _mcp_options_pb2
from qdrant.cloud.facade.v1 import facade_options_pb2 as _facade_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LimitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIMIT_TYPE_UNSPECIFIED: _ClassVar[LimitType]
    LIMIT_TYPE_HARD: _ClassVar[LimitType]
    LIMIT_TYPE_SOFT: _ClassVar[LimitType]

class SpaceStatePhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_STATE_PHASE_UNSPECIFIED: _ClassVar[SpaceStatePhase]
    SPACE_STATE_PHASE_PROCESSING: _ClassVar[SpaceStatePhase]
    SPACE_STATE_PHASE_READY: _ClassVar[SpaceStatePhase]
    SPACE_STATE_PHASE_DISABLED: _ClassVar[SpaceStatePhase]
    SPACE_STATE_PHASE_DELETING: _ClassVar[SpaceStatePhase]

class SpaceAccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_ACCESS_MODE_UNSPECIFIED: _ClassVar[SpaceAccessMode]
    SPACE_ACCESS_MODE_FULL: _ClassVar[SpaceAccessMode]
    SPACE_ACCESS_MODE_WRITES_BLOCKED: _ClassVar[SpaceAccessMode]
    SPACE_ACCESS_MODE_BLOCKED: _ClassVar[SpaceAccessMode]

class LimitUsageLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIMIT_USAGE_LEVEL_UNSPECIFIED: _ClassVar[LimitUsageLevel]
    LIMIT_USAGE_LEVEL_UNLIMITED: _ClassVar[LimitUsageLevel]
    LIMIT_USAGE_LEVEL_OK: _ClassVar[LimitUsageLevel]
    LIMIT_USAGE_LEVEL_THRESHOLD_REACHED: _ClassVar[LimitUsageLevel]
    LIMIT_USAGE_LEVEL_LIMIT_REACHED: _ClassVar[LimitUsageLevel]
LIMIT_TYPE_UNSPECIFIED: LimitType
LIMIT_TYPE_HARD: LimitType
LIMIT_TYPE_SOFT: LimitType
SPACE_STATE_PHASE_UNSPECIFIED: SpaceStatePhase
SPACE_STATE_PHASE_PROCESSING: SpaceStatePhase
SPACE_STATE_PHASE_READY: SpaceStatePhase
SPACE_STATE_PHASE_DISABLED: SpaceStatePhase
SPACE_STATE_PHASE_DELETING: SpaceStatePhase
SPACE_ACCESS_MODE_UNSPECIFIED: SpaceAccessMode
SPACE_ACCESS_MODE_FULL: SpaceAccessMode
SPACE_ACCESS_MODE_WRITES_BLOCKED: SpaceAccessMode
SPACE_ACCESS_MODE_BLOCKED: SpaceAccessMode
LIMIT_USAGE_LEVEL_UNSPECIFIED: LimitUsageLevel
LIMIT_USAGE_LEVEL_UNLIMITED: LimitUsageLevel
LIMIT_USAGE_LEVEL_OK: LimitUsageLevel
LIMIT_USAGE_LEVEL_THRESHOLD_REACHED: LimitUsageLevel
LIMIT_USAGE_LEVEL_LIMIT_REACHED: LimitUsageLevel

class ListSpacesRequest(_message.Message):
    __slots__ = ("account_id", "cloud_region_id", "page_size", "page_token")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cloud_region_id: str
    page_size: int
    page_token: str
    def __init__(self, account_id: _Optional[str] = ..., cloud_region_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSpacesResponse(_message.Message):
    __slots__ = ("items", "total_size", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Space]
    total_size: int
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[Space, _Mapping]]] = ..., total_size: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSpaceRequest(_message.Message):
    __slots__ = ("account_id", "space_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...

class GetSpaceResponse(_message.Message):
    __slots__ = ("space",)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: Space
    def __init__(self, space: _Optional[_Union[Space, _Mapping]] = ...) -> None: ...

class CreateSpaceRequest(_message.Message):
    __slots__ = ("space",)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: Space
    def __init__(self, space: _Optional[_Union[Space, _Mapping]] = ...) -> None: ...

class CreateSpaceResponse(_message.Message):
    __slots__ = ("space",)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: Space
    def __init__(self, space: _Optional[_Union[Space, _Mapping]] = ...) -> None: ...

class CreateSpaceFromBackupRequest(_message.Message):
    __slots__ = ("account_id", "backup_id", "space_name")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    backup_id: str
    space_name: str
    def __init__(self, account_id: _Optional[str] = ..., backup_id: _Optional[str] = ..., space_name: _Optional[str] = ...) -> None: ...

class CreateSpaceFromBackupResponse(_message.Message):
    __slots__ = ("space",)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: Space
    def __init__(self, space: _Optional[_Union[Space, _Mapping]] = ...) -> None: ...

class UpdateSpaceRequest(_message.Message):
    __slots__ = ("space", "update_mask")
    SPACE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    space: Space
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, space: _Optional[_Union[Space, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSpaceResponse(_message.Message):
    __slots__ = ("space",)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: Space
    def __init__(self, space: _Optional[_Union[Space, _Mapping]] = ...) -> None: ...

class DeleteSpaceRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "delete_backups")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    delete_backups: bool
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., delete_backups: _Optional[bool] = ...) -> None: ...

class DeleteSpaceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuggestSpaceNameRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class SuggestSpaceNameResponse(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Space(_message.Message):
    __slots__ = ("id", "created_at", "account_id", "name", "deleted_at", "cloud_region_id", "labels", "cost_allocation_label", "configuration", "created_by", "last_updated_by", "deleted_by", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    COST_ALLOCATION_LABEL_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    account_id: str
    name: str
    deleted_at: _timestamp_pb2.Timestamp
    cloud_region_id: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    cost_allocation_label: str
    configuration: SpaceConfiguration
    created_by: _common_pb2.Caller
    last_updated_by: _common_pb2.Caller
    deleted_by: _common_pb2.Caller
    state: SpaceState
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., name: _Optional[str] = ..., deleted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cloud_region_id: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ..., cost_allocation_label: _Optional[str] = ..., configuration: _Optional[_Union[SpaceConfiguration, _Mapping]] = ..., created_by: _Optional[_Union[_common_pb2.Caller, _Mapping]] = ..., last_updated_by: _Optional[_Union[_common_pb2.Caller, _Mapping]] = ..., deleted_by: _Optional[_Union[_common_pb2.Caller, _Mapping]] = ..., state: _Optional[_Union[SpaceState, _Mapping]] = ...) -> None: ...

class SpaceConfiguration(_message.Message):
    __slots__ = ("last_modified_at", "allowed_ip_source_ranges", "allowed_origins", "max_collections_per_space", "collection_settings", "searcher_settings", "storage_limit", "monthly_spend_limit")
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_IP_SOURCE_RANGES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ORIGINS_FIELD_NUMBER: _ClassVar[int]
    MAX_COLLECTIONS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SEARCHER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SPEND_LIMIT_FIELD_NUMBER: _ClassVar[int]
    last_modified_at: _timestamp_pb2.Timestamp
    allowed_ip_source_ranges: _containers.RepeatedScalarFieldContainer[str]
    allowed_origins: _containers.RepeatedScalarFieldContainer[str]
    max_collections_per_space: int
    collection_settings: CollectionSettings
    searcher_settings: SearcherSettings
    storage_limit: StorageLimit
    monthly_spend_limit: SpendLimit
    def __init__(self, last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., allowed_ip_source_ranges: _Optional[_Iterable[str]] = ..., allowed_origins: _Optional[_Iterable[str]] = ..., max_collections_per_space: _Optional[int] = ..., collection_settings: _Optional[_Union[CollectionSettings, _Mapping]] = ..., searcher_settings: _Optional[_Union[SearcherSettings, _Mapping]] = ..., storage_limit: _Optional[_Union[StorageLimit, _Mapping]] = ..., monthly_spend_limit: _Optional[_Union[SpendLimit, _Mapping]] = ...) -> None: ...

class CollectionSettings(_message.Message):
    __slots__ = ("platform_max_size", "max_size", "max_indexed_size", "platform_max_indexed_size", "size_warning_threshold_percent")
    PLATFORM_MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_INDEXED_SIZE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_MAX_INDEXED_SIZE_FIELD_NUMBER: _ClassVar[int]
    SIZE_WARNING_THRESHOLD_PERCENT_FIELD_NUMBER: _ClassVar[int]
    platform_max_size: int
    max_size: int
    max_indexed_size: int
    platform_max_indexed_size: int
    size_warning_threshold_percent: int
    def __init__(self, platform_max_size: _Optional[int] = ..., max_size: _Optional[int] = ..., max_indexed_size: _Optional[int] = ..., platform_max_indexed_size: _Optional[int] = ..., size_warning_threshold_percent: _Optional[int] = ...) -> None: ...

class SearcherSettings(_message.Message):
    __slots__ = ("min_idle_timeout", "platform_max_workers", "max_workers")
    MIN_IDLE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_MAX_WORKERS_FIELD_NUMBER: _ClassVar[int]
    MAX_WORKERS_FIELD_NUMBER: _ClassVar[int]
    min_idle_timeout: _duration_pb2.Duration
    platform_max_workers: int
    max_workers: int
    def __init__(self, min_idle_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., platform_max_workers: _Optional[int] = ..., max_workers: _Optional[int] = ...) -> None: ...

class StorageLimit(_message.Message):
    __slots__ = ("max_size", "type", "alert_threshold_percent")
    MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ALERT_THRESHOLD_PERCENT_FIELD_NUMBER: _ClassVar[int]
    max_size: int
    type: LimitType
    alert_threshold_percent: int
    def __init__(self, max_size: _Optional[int] = ..., type: _Optional[_Union[LimitType, str]] = ..., alert_threshold_percent: _Optional[int] = ...) -> None: ...

class SpendLimit(_message.Message):
    __slots__ = ("max_amount_millicents", "type", "alert_threshold_percent", "currency")
    MAX_AMOUNT_MILLICENTS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ALERT_THRESHOLD_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    max_amount_millicents: int
    type: LimitType
    alert_threshold_percent: int
    currency: str
    def __init__(self, max_amount_millicents: _Optional[int] = ..., type: _Optional[_Union[LimitType, str]] = ..., alert_threshold_percent: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class SpaceState(_message.Message):
    __slots__ = ("phase", "reason", "endpoint", "limits")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    phase: SpaceStatePhase
    reason: str
    endpoint: SpaceEndpoint
    limits: SpaceLimitsStatus
    def __init__(self, phase: _Optional[_Union[SpaceStatePhase, str]] = ..., reason: _Optional[str] = ..., endpoint: _Optional[_Union[SpaceEndpoint, _Mapping]] = ..., limits: _Optional[_Union[SpaceLimitsStatus, _Mapping]] = ...) -> None: ...

class SpaceLimitsStatus(_message.Message):
    __slots__ = ("access_mode", "storage", "monthly_spend")
    ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SPEND_FIELD_NUMBER: _ClassVar[int]
    access_mode: SpaceAccessMode
    storage: StorageLimitStatus
    monthly_spend: SpendLimitStatus
    def __init__(self, access_mode: _Optional[_Union[SpaceAccessMode, str]] = ..., storage: _Optional[_Union[StorageLimitStatus, _Mapping]] = ..., monthly_spend: _Optional[_Union[SpendLimitStatus, _Mapping]] = ...) -> None: ...

class StorageLimitStatus(_message.Message):
    __slots__ = ("used_size", "level")
    USED_SIZE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    used_size: int
    level: LimitUsageLevel
    def __init__(self, used_size: _Optional[int] = ..., level: _Optional[_Union[LimitUsageLevel, str]] = ...) -> None: ...

class SpendLimitStatus(_message.Message):
    __slots__ = ("used_amount_millicents", "level", "period_start", "period_end", "currency")
    USED_AMOUNT_MILLICENTS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    used_amount_millicents: int
    level: LimitUsageLevel
    period_start: _timestamp_pb2.Timestamp
    period_end: _timestamp_pb2.Timestamp
    currency: str
    def __init__(self, used_amount_millicents: _Optional[int] = ..., level: _Optional[_Union[LimitUsageLevel, str]] = ..., period_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., currency: _Optional[str] = ...) -> None: ...

class SpaceEndpoint(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...
