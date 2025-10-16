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

class GetClusterSummaryMetricsRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class GetClusterSummaryMetricsResponse(_message.Message):
    __slots__ = ("nodes",)
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[ClusterNodeMetrics]
    def __init__(self, nodes: _Optional[_Iterable[_Union[ClusterNodeMetrics, _Mapping]]] = ...) -> None: ...

class GetClusterUsageMetricsRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "since", "until", "aggregator")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATOR_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    aggregator: Aggregator
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., aggregator: _Optional[_Union[Aggregator, str]] = ...) -> None: ...

class GetClusterUsageMetricsResponse(_message.Message):
    __slots__ = ("cpu", "ram", "ram_cache", "ram_rss", "ram_qdrant_rss", "disk", "rps", "latency", "nodes")
    CPU_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    RAM_CACHE_FIELD_NUMBER: _ClassVar[int]
    RAM_RSS_FIELD_NUMBER: _ClassVar[int]
    RAM_QDRANT_RSS_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    RPS_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    cpu: _containers.RepeatedCompositeFieldContainer[Metric]
    ram: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_cache: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_rss: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_qdrant_rss: _containers.RepeatedCompositeFieldContainer[Metric]
    disk: _containers.RepeatedCompositeFieldContainer[Metric]
    rps: _containers.RepeatedCompositeFieldContainer[Metric]
    latency: _containers.RepeatedCompositeFieldContainer[Metric]
    nodes: _containers.RepeatedCompositeFieldContainer[ClusterNodeUsageMetrics]
    def __init__(self, cpu: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_cache: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_rss: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_qdrant_rss: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., disk: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., rps: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., latency: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., nodes: _Optional[_Iterable[_Union[ClusterNodeUsageMetrics, _Mapping]]] = ...) -> None: ...

class GetClusterLogsRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "since", "until")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetClusterLogsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[LogEntry]
    def __init__(self, items: _Optional[_Iterable[_Union[LogEntry, _Mapping]]] = ...) -> None: ...

class GetClusterEventsRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "since", "until")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ClusterNodeMetrics(_message.Message):
    __slots__ = ("node_id", "cpu", "ram", "ram_cache", "ram_rss", "ram_qdrant_rss", "disk")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    RAM_CACHE_FIELD_NUMBER: _ClassVar[int]
    RAM_RSS_FIELD_NUMBER: _ClassVar[int]
    RAM_QDRANT_RSS_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    cpu: ClusterMetricOverview
    ram: ClusterMetricOverview
    ram_cache: ClusterMetricOverview
    ram_rss: ClusterMetricOverview
    ram_qdrant_rss: ClusterMetricOverview
    disk: ClusterMetricOverview
    def __init__(self, node_id: _Optional[str] = ..., cpu: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., ram: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., ram_cache: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., ram_rss: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., ram_qdrant_rss: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., disk: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ...) -> None: ...

class ClusterMetricOverview(_message.Message):
    __slots__ = ("avg", "total")
    AVG_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    avg: _containers.RepeatedCompositeFieldContainer[IntervalAverage]
    total: ResourceValue
    def __init__(self, avg: _Optional[_Iterable[_Union[IntervalAverage, _Mapping]]] = ..., total: _Optional[_Union[ResourceValue, _Mapping]] = ...) -> None: ...

class IntervalAverage(_message.Message):
    __slots__ = ("interval", "value")
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    interval: _duration_pb2.Duration
    value: float
    def __init__(self, interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class ResourceValue(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: str
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[str] = ...) -> None: ...

class ClusterNodeUsageMetrics(_message.Message):
    __slots__ = ("node_id", "cpu", "ram", "ram_cache", "ram_rss", "ram_qdrant_rss", "disk")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    RAM_CACHE_FIELD_NUMBER: _ClassVar[int]
    RAM_RSS_FIELD_NUMBER: _ClassVar[int]
    RAM_QDRANT_RSS_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    cpu: _containers.RepeatedCompositeFieldContainer[Metric]
    ram: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_cache: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_rss: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_qdrant_rss: _containers.RepeatedCompositeFieldContainer[Metric]
    disk: _containers.RepeatedCompositeFieldContainer[Metric]
    def __init__(self, node_id: _Optional[str] = ..., cpu: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_cache: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_rss: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_qdrant_rss: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., disk: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ("timestamp", "value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    value: float
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class LogEntry(_message.Message):
    __slots__ = ("timestamp", "message")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    message: str
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class GetClusterEventsResponse(_message.Message):
    __slots__ = ("hybrid_cloud_id", "values")
    HYBRID_CLOUD_ID_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_id: str
    values: _containers.RepeatedCompositeFieldContainer[LogEntry]
    def __init__(self, hybrid_cloud_id: _Optional[str] = ..., values: _Optional[_Iterable[_Union[LogEntry, _Mapping]]] = ...) -> None: ...
