import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Aggregator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGGREGATOR_UNSPECIFIED: _ClassVar[Aggregator]
    AGGREGATOR_SUM: _ClassVar[Aggregator]
    AGGREGATOR_AVG: _ClassVar[Aggregator]
    AGGREGATOR_MAX: _ClassVar[Aggregator]
    AGGREGATOR_MIN: _ClassVar[Aggregator]

class InferenceMetricsInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFERENCE_METRICS_INTERVAL_UNSPECIFIED: _ClassVar[InferenceMetricsInterval]
    INFERENCE_METRICS_INTERVAL_DAY: _ClassVar[InferenceMetricsInterval]
    INFERENCE_METRICS_INTERVAL_WEEK: _ClassVar[InferenceMetricsInterval]
    INFERENCE_METRICS_INTERVAL_MONTH: _ClassVar[InferenceMetricsInterval]

class SpaceAlertState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_ALERT_STATE_UNSPECIFIED: _ClassVar[SpaceAlertState]
    SPACE_ALERT_STATE_FIRING: _ClassVar[SpaceAlertState]
    SPACE_ALERT_STATE_RESOLVED: _ClassVar[SpaceAlertState]

class SpaceAlertType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_ALERT_TYPE_UNSPECIFIED: _ClassVar[SpaceAlertType]
    SPACE_ALERT_TYPE_COLLECTION_STORAGE_OVERUTILIZED: _ClassVar[SpaceAlertType]
    SPACE_ALERT_TYPE_TOO_MANY_COLLECTIONS: _ClassVar[SpaceAlertType]
    SPACE_ALERT_TYPE_SPACE_API_KEY_ABOUT_TO_EXPIRE: _ClassVar[SpaceAlertType]
    SPACE_ALERT_TYPE_SPACE_UNHEALTHY: _ClassVar[SpaceAlertType]

class SpaceAlertSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_ALERT_SEVERITY_UNSPECIFIED: _ClassVar[SpaceAlertSeverity]
    SPACE_ALERT_SEVERITY_INFO: _ClassVar[SpaceAlertSeverity]
    SPACE_ALERT_SEVERITY_WARNING: _ClassVar[SpaceAlertSeverity]
    SPACE_ALERT_SEVERITY_CRITICAL: _ClassVar[SpaceAlertSeverity]
AGGREGATOR_UNSPECIFIED: Aggregator
AGGREGATOR_SUM: Aggregator
AGGREGATOR_AVG: Aggregator
AGGREGATOR_MAX: Aggregator
AGGREGATOR_MIN: Aggregator
INFERENCE_METRICS_INTERVAL_UNSPECIFIED: InferenceMetricsInterval
INFERENCE_METRICS_INTERVAL_DAY: InferenceMetricsInterval
INFERENCE_METRICS_INTERVAL_WEEK: InferenceMetricsInterval
INFERENCE_METRICS_INTERVAL_MONTH: InferenceMetricsInterval
SPACE_ALERT_STATE_UNSPECIFIED: SpaceAlertState
SPACE_ALERT_STATE_FIRING: SpaceAlertState
SPACE_ALERT_STATE_RESOLVED: SpaceAlertState
SPACE_ALERT_TYPE_UNSPECIFIED: SpaceAlertType
SPACE_ALERT_TYPE_COLLECTION_STORAGE_OVERUTILIZED: SpaceAlertType
SPACE_ALERT_TYPE_TOO_MANY_COLLECTIONS: SpaceAlertType
SPACE_ALERT_TYPE_SPACE_API_KEY_ABOUT_TO_EXPIRE: SpaceAlertType
SPACE_ALERT_TYPE_SPACE_UNHEALTHY: SpaceAlertType
SPACE_ALERT_SEVERITY_UNSPECIFIED: SpaceAlertSeverity
SPACE_ALERT_SEVERITY_INFO: SpaceAlertSeverity
SPACE_ALERT_SEVERITY_WARNING: SpaceAlertSeverity
SPACE_ALERT_SEVERITY_CRITICAL: SpaceAlertSeverity

class GetSpaceSummaryMetricsRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "collection_name", "collection_name_contains", "page_size", "page_token")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    collection_name: str
    collection_name_contains: str
    page_size: int
    page_token: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., collection_name: _Optional[str] = ..., collection_name_contains: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class GetSpaceSummaryMetricsResponse(_message.Message):
    __slots__ = ("items", "total_size", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SpaceCollectionMetrics]
    total_size: int
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[SpaceCollectionMetrics, _Mapping]]] = ..., total_size: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSpaceUsageMetricsRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "since", "until", "aggregator", "collection_name", "collection_name_contains", "page_size", "page_token")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATOR_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    aggregator: Aggregator
    collection_name: str
    collection_name_contains: str
    page_size: int
    page_token: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., aggregator: _Optional[_Union[Aggregator, str]] = ..., collection_name: _Optional[str] = ..., collection_name_contains: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class GetSpaceUsageMetricsResponse(_message.Message):
    __slots__ = ("items", "total_size", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SpaceCollectionUsageMetrics]
    total_size: int
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[SpaceCollectionUsageMetrics, _Mapping]]] = ..., total_size: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSpaceInferenceMetricsRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "since", "until", "interval", "inference_model_id", "collection_name", "collection_name_contains", "page_size", "page_token")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    interval: InferenceMetricsInterval
    inference_model_id: str
    collection_name: str
    collection_name_contains: str
    page_size: int
    page_token: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., interval: _Optional[_Union[InferenceMetricsInterval, str]] = ..., inference_model_id: _Optional[str] = ..., collection_name: _Optional[str] = ..., collection_name_contains: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class GetSpaceInferenceMetricsResponse(_message.Message):
    __slots__ = ("items", "total_size", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SpaceCollectionInferenceMetrics]
    total_size: int
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[SpaceCollectionInferenceMetrics, _Mapping]]] = ..., total_size: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SpaceCollectionInferenceMetrics(_message.Message):
    __slots__ = ("collection_name", "models")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    models: _containers.RepeatedCompositeFieldContainer[SpaceInferenceModelMetrics]
    def __init__(self, collection_name: _Optional[str] = ..., models: _Optional[_Iterable[_Union[SpaceInferenceModelMetrics, _Mapping]]] = ...) -> None: ...

class SpaceInferenceModelMetrics(_message.Message):
    __slots__ = ("inference_model_id", "values")
    INFERENCE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    inference_model_id: str
    values: _containers.RepeatedCompositeFieldContainer[Metric]
    def __init__(self, inference_model_id: _Optional[str] = ..., values: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ...) -> None: ...

class ListSpaceAlertsRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "state", "collection_name", "collection_name_contains", "space_global_only", "page_size", "page_token")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    SPACE_GLOBAL_ONLY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    state: SpaceAlertState
    collection_name: str
    collection_name_contains: str
    space_global_only: bool
    page_size: int
    page_token: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., state: _Optional[_Union[SpaceAlertState, str]] = ..., collection_name: _Optional[str] = ..., collection_name_contains: _Optional[str] = ..., space_global_only: _Optional[bool] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSpaceAlertsResponse(_message.Message):
    __slots__ = ("items", "total_size", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SpaceAlert]
    total_size: int
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[SpaceAlert, _Mapping]]] = ..., total_size: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SpaceAlert(_message.Message):
    __slots__ = ("id", "type", "severity", "title", "description", "last_firing_at", "state", "collection_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAST_FIRING_AT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: SpaceAlertType
    severity: SpaceAlertSeverity
    title: str
    description: str
    last_firing_at: _timestamp_pb2.Timestamp
    state: SpaceAlertState
    collection_name: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[SpaceAlertType, str]] = ..., severity: _Optional[_Union[SpaceAlertSeverity, str]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., last_firing_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[SpaceAlertState, str]] = ..., collection_name: _Optional[str] = ...) -> None: ...

class SpaceCollectionMetrics(_message.Message):
    __slots__ = ("collection_name", "search_requests", "write_requests", "search_latency", "vector_count", "used_storage_bytes")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    WRITE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LATENCY_FIELD_NUMBER: _ClassVar[int]
    VECTOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    USED_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    search_requests: SpaceMetricOverview
    write_requests: SpaceMetricOverview
    search_latency: SpaceMetricOverview
    vector_count: int
    used_storage_bytes: int
    def __init__(self, collection_name: _Optional[str] = ..., search_requests: _Optional[_Union[SpaceMetricOverview, _Mapping]] = ..., write_requests: _Optional[_Union[SpaceMetricOverview, _Mapping]] = ..., search_latency: _Optional[_Union[SpaceMetricOverview, _Mapping]] = ..., vector_count: _Optional[int] = ..., used_storage_bytes: _Optional[int] = ...) -> None: ...

class SpaceMetricOverview(_message.Message):
    __slots__ = ("avg",)
    AVG_FIELD_NUMBER: _ClassVar[int]
    avg: _containers.RepeatedCompositeFieldContainer[IntervalAverage]
    def __init__(self, avg: _Optional[_Iterable[_Union[IntervalAverage, _Mapping]]] = ...) -> None: ...

class IntervalAverage(_message.Message):
    __slots__ = ("interval", "value")
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    interval: _duration_pb2.Duration
    value: float
    def __init__(self, interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class SpaceCollectionUsageMetrics(_message.Message):
    __slots__ = ("collection_name", "search_requests", "write_requests", "search_latency", "vector_count", "used_storage_bytes")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    WRITE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LATENCY_FIELD_NUMBER: _ClassVar[int]
    VECTOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    USED_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    search_requests: _containers.RepeatedCompositeFieldContainer[Metric]
    write_requests: _containers.RepeatedCompositeFieldContainer[Metric]
    search_latency: _containers.RepeatedCompositeFieldContainer[Metric]
    vector_count: _containers.RepeatedCompositeFieldContainer[Metric]
    used_storage_bytes: _containers.RepeatedCompositeFieldContainer[Metric]
    def __init__(self, collection_name: _Optional[str] = ..., search_requests: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., write_requests: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., search_latency: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., vector_count: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., used_storage_bytes: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ("timestamp", "value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    value: float
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...
