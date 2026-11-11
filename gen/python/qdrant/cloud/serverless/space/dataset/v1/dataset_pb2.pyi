import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.event.v1 import events_pb2 as _events_pb2
from qdrant.cloud.facade.mcp.v1 import mcp_options_pb2 as _mcp_options_pb2
from qdrant.cloud.facade.v1 import facade_options_pb2 as _facade_options_pb2
from qdrant.serverless import collections_pb2 as _collections_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SampleDatasetLoadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAMPLE_DATASET_LOAD_STATUS_UNSPECIFIED: _ClassVar[SampleDatasetLoadStatus]
    SAMPLE_DATASET_LOAD_STATUS_RUNNING: _ClassVar[SampleDatasetLoadStatus]
    SAMPLE_DATASET_LOAD_STATUS_FAILED: _ClassVar[SampleDatasetLoadStatus]
    SAMPLE_DATASET_LOAD_STATUS_SUCCEEDED: _ClassVar[SampleDatasetLoadStatus]
    SAMPLE_DATASET_LOAD_STATUS_FAILED_TO_SYNC: _ClassVar[SampleDatasetLoadStatus]
    SAMPLE_DATASET_LOAD_STATUS_NOT_FOUND: _ClassVar[SampleDatasetLoadStatus]
    SAMPLE_DATASET_LOAD_STATUS_SKIPPED: _ClassVar[SampleDatasetLoadStatus]
SAMPLE_DATASET_LOAD_STATUS_UNSPECIFIED: SampleDatasetLoadStatus
SAMPLE_DATASET_LOAD_STATUS_RUNNING: SampleDatasetLoadStatus
SAMPLE_DATASET_LOAD_STATUS_FAILED: SampleDatasetLoadStatus
SAMPLE_DATASET_LOAD_STATUS_SUCCEEDED: SampleDatasetLoadStatus
SAMPLE_DATASET_LOAD_STATUS_FAILED_TO_SYNC: SampleDatasetLoadStatus
SAMPLE_DATASET_LOAD_STATUS_NOT_FOUND: SampleDatasetLoadStatus
SAMPLE_DATASET_LOAD_STATUS_SKIPPED: SampleDatasetLoadStatus

class ListSampleDatasetsRequest(_message.Message):
    __slots__ = ("account_id", "space_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...

class ListSampleDatasetsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SampleDataset]
    def __init__(self, items: _Optional[_Iterable[_Union[SampleDataset, _Mapping]]] = ...) -> None: ...

class ListSampleDatasetLoadsRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "page_size", "page_token")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    page_size: int
    page_token: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSampleDatasetLoadsResponse(_message.Message):
    __slots__ = ("items", "total_size", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SampleDatasetLoad]
    total_size: int
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[SampleDatasetLoad, _Mapping]]] = ..., total_size: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSampleDatasetLoadRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "sample_dataset_load_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_DATASET_LOAD_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    sample_dataset_load_id: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., sample_dataset_load_id: _Optional[str] = ...) -> None: ...

class GetSampleDatasetLoadResponse(_message.Message):
    __slots__ = ("sample_dataset_load",)
    SAMPLE_DATASET_LOAD_FIELD_NUMBER: _ClassVar[int]
    sample_dataset_load: SampleDatasetLoad
    def __init__(self, sample_dataset_load: _Optional[_Union[SampleDatasetLoad, _Mapping]] = ...) -> None: ...

class LoadSampleDatasetRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "sample_dataset_id", "collection_name")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    sample_dataset_id: str
    collection_name: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., sample_dataset_id: _Optional[str] = ..., collection_name: _Optional[str] = ...) -> None: ...

class LoadSampleDatasetResponse(_message.Message):
    __slots__ = ("sample_dataset_load",)
    SAMPLE_DATASET_LOAD_FIELD_NUMBER: _ClassVar[int]
    sample_dataset_load: SampleDatasetLoad
    def __init__(self, sample_dataset_load: _Optional[_Union[SampleDatasetLoad, _Mapping]] = ...) -> None: ...

class SampleDataset(_message.Message):
    __slots__ = ("id", "name", "description", "collection_config", "point_count", "size_bytes", "indexed_size_bytes", "version", "vector_models")
    class VectorModelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    INDEXED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VECTOR_MODELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    collection_config: _collections_pb2.CollectionConfig
    point_count: int
    size_bytes: int
    indexed_size_bytes: int
    version: str
    vector_models: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., collection_config: _Optional[_Union[_collections_pb2.CollectionConfig, _Mapping]] = ..., point_count: _Optional[int] = ..., size_bytes: _Optional[int] = ..., indexed_size_bytes: _Optional[int] = ..., version: _Optional[str] = ..., vector_models: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SampleDatasetLoad(_message.Message):
    __slots__ = ("id", "created_at", "account_id", "space_id", "sample_dataset_id", "sample_dataset_version", "collection_name", "status", "reason", "deleted_at", "created_by", "stats")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_DATASET_VERSION_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    account_id: str
    space_id: str
    sample_dataset_id: str
    sample_dataset_version: str
    collection_name: str
    status: SampleDatasetLoadStatus
    reason: str
    deleted_at: _timestamp_pb2.Timestamp
    created_by: _common_pb2.Caller
    stats: SampleDatasetLoadStats
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., sample_dataset_id: _Optional[str] = ..., sample_dataset_version: _Optional[str] = ..., collection_name: _Optional[str] = ..., status: _Optional[_Union[SampleDatasetLoadStatus, str]] = ..., reason: _Optional[str] = ..., deleted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[_Union[_common_pb2.Caller, _Mapping]] = ..., stats: _Optional[_Union[SampleDatasetLoadStats, _Mapping]] = ...) -> None: ...

class SampleDatasetLoadStats(_message.Message):
    __slots__ = ("duration", "progress")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    progress: str
    def __init__(self, duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., progress: _Optional[str] = ...) -> None: ...
