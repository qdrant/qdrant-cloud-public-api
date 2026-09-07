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
AGGREGATOR_UNSPECIFIED: Aggregator
AGGREGATOR_SUM: Aggregator
AGGREGATOR_AVG: Aggregator
AGGREGATOR_MAX: Aggregator
AGGREGATOR_MIN: Aggregator

class GetSpaceSummaryMetricsRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "collection_name")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    collection_name: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., collection_name: _Optional[str] = ...) -> None: ...

class GetSpaceSummaryMetricsResponse(_message.Message):
    __slots__ = ("collections",)
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedCompositeFieldContainer[SpaceCollectionMetrics]
    def __init__(self, collections: _Optional[_Iterable[_Union[SpaceCollectionMetrics, _Mapping]]] = ...) -> None: ...

class GetSpaceUsageMetricsRequest(_message.Message):
    __slots__ = ("account_id", "space_id", "since", "until", "aggregator", "collection_name")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATOR_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    aggregator: Aggregator
    collection_name: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., aggregator: _Optional[_Union[Aggregator, str]] = ..., collection_name: _Optional[str] = ...) -> None: ...

class GetSpaceUsageMetricsResponse(_message.Message):
    __slots__ = ("collections",)
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedCompositeFieldContainer[SpaceCollectionUsageMetrics]
    def __init__(self, collections: _Optional[_Iterable[_Union[SpaceCollectionUsageMetrics, _Mapping]]] = ...) -> None: ...

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
