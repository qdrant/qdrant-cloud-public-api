import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
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

class SpaceStatePhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_STATE_PHASE_UNSPECIFIED: _ClassVar[SpaceStatePhase]
    SPACE_STATE_PHASE_PROCESSING: _ClassVar[SpaceStatePhase]
    SPACE_STATE_PHASE_READY: _ClassVar[SpaceStatePhase]
    SPACE_STATE_PHASE_DISABLED: _ClassVar[SpaceStatePhase]
    SPACE_STATE_PHASE_DELETING: _ClassVar[SpaceStatePhase]
SPACE_STATE_PHASE_UNSPECIFIED: SpaceStatePhase
SPACE_STATE_PHASE_PROCESSING: SpaceStatePhase
SPACE_STATE_PHASE_READY: SpaceStatePhase
SPACE_STATE_PHASE_DISABLED: SpaceStatePhase
SPACE_STATE_PHASE_DELETING: SpaceStatePhase

class ListSpacesRequest(_message.Message):
    __slots__ = ("account_id", "cloud_provider_id", "cloud_provider_region_id", "page_size", "page_token")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cloud_provider_id: str
    cloud_provider_region_id: str
    page_size: int
    page_token: str
    def __init__(self, account_id: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ..., cloud_provider_region_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("id", "created_at", "account_id", "name", "deleted_at", "cloud_provider_id", "cloud_provider_region_id", "labels", "cost_allocation_label", "configuration", "created_by", "last_updated_by", "deleted_by", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_REGION_ID_FIELD_NUMBER: _ClassVar[int]
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
    cloud_provider_id: str
    cloud_provider_region_id: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    cost_allocation_label: str
    configuration: SpaceConfiguration
    created_by: _common_pb2.Caller
    last_updated_by: _common_pb2.Caller
    deleted_by: _common_pb2.Caller
    state: SpaceState
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., name: _Optional[str] = ..., deleted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cloud_provider_id: _Optional[str] = ..., cloud_provider_region_id: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ..., cost_allocation_label: _Optional[str] = ..., configuration: _Optional[_Union[SpaceConfiguration, _Mapping]] = ..., created_by: _Optional[_Union[_common_pb2.Caller, _Mapping]] = ..., last_updated_by: _Optional[_Union[_common_pb2.Caller, _Mapping]] = ..., deleted_by: _Optional[_Union[_common_pb2.Caller, _Mapping]] = ..., state: _Optional[_Union[SpaceState, _Mapping]] = ...) -> None: ...

class SpaceConfiguration(_message.Message):
    __slots__ = ("last_modified_at", "allowed_ip_source_ranges", "allowed_origins")
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_IP_SOURCE_RANGES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ORIGINS_FIELD_NUMBER: _ClassVar[int]
    last_modified_at: _timestamp_pb2.Timestamp
    allowed_ip_source_ranges: _containers.RepeatedScalarFieldContainer[str]
    allowed_origins: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., allowed_ip_source_ranges: _Optional[_Iterable[str]] = ..., allowed_origins: _Optional[_Iterable[str]] = ...) -> None: ...

class SpaceState(_message.Message):
    __slots__ = ("phase", "reason", "endpoint")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    phase: SpaceStatePhase
    reason: str
    endpoint: SpaceEndpoint
    def __init__(self, phase: _Optional[_Union[SpaceStatePhase, str]] = ..., reason: _Optional[str] = ..., endpoint: _Optional[_Union[SpaceEndpoint, _Mapping]] = ...) -> None: ...

class SpaceEndpoint(_message.Message):
    __slots__ = ("url", "rest_port", "grpc_port")
    URL_FIELD_NUMBER: _ClassVar[int]
    REST_PORT_FIELD_NUMBER: _ClassVar[int]
    GRPC_PORT_FIELD_NUMBER: _ClassVar[int]
    url: str
    rest_port: int
    grpc_port: int
    def __init__(self, url: _Optional[str] = ..., rest_port: _Optional[int] = ..., grpc_port: _Optional[int] = ...) -> None: ...
