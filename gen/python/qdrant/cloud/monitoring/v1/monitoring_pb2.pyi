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

class ClusterAlertState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_ALERT_STATE_UNSPECIFIED: _ClassVar[ClusterAlertState]
    CLUSTER_ALERT_STATE_FIRING: _ClassVar[ClusterAlertState]
    CLUSTER_ALERT_STATE_RESOLVED: _ClassVar[ClusterAlertState]

class ClusterAlertType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_ALERT_TYPE_UNSPECIFIED: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_DISK_OVERUTILIZED: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_MEMORY_OVERUTILIZED: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_OOD: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_OOM: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_RECOVERY_MODE: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_QDRANT_CLUSTER_UNHEALTHY: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_TOO_MANY_COLLECTIONS: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_QDRANT_CLUSTER_CPU_THROTTLED: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_QDRANT_JWT_API_KEY_ABOUT_TO_EXPIRE: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_CLUSTER_VERSION_IS_NOT_COVERED_BY_SLA: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_CLUSTER_DISK_HOTSPOT: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_CLUSTER_MEMORY_HOTSPOT: _ClassVar[ClusterAlertType]
    CLUSTER_ALERT_TYPE_CLUSTER_CPU_HOTSPOT: _ClassVar[ClusterAlertType]

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEVERITY_UNSPECIFIED: _ClassVar[Severity]
    SEVERITY_INFO: _ClassVar[Severity]
    SEVERITY_WARNING: _ClassVar[Severity]
    SEVERITY_CRITICAL: _ClassVar[Severity]
AGGREGATOR_UNSPECIFIED: Aggregator
AGGREGATOR_SUM: Aggregator
AGGREGATOR_AVG: Aggregator
AGGREGATOR_MAX: Aggregator
AGGREGATOR_MIN: Aggregator
INFERENCE_METRICS_INTERVAL_UNSPECIFIED: InferenceMetricsInterval
INFERENCE_METRICS_INTERVAL_DAY: InferenceMetricsInterval
INFERENCE_METRICS_INTERVAL_WEEK: InferenceMetricsInterval
INFERENCE_METRICS_INTERVAL_MONTH: InferenceMetricsInterval
CLUSTER_ALERT_STATE_UNSPECIFIED: ClusterAlertState
CLUSTER_ALERT_STATE_FIRING: ClusterAlertState
CLUSTER_ALERT_STATE_RESOLVED: ClusterAlertState
CLUSTER_ALERT_TYPE_UNSPECIFIED: ClusterAlertType
CLUSTER_ALERT_TYPE_DISK_OVERUTILIZED: ClusterAlertType
CLUSTER_ALERT_TYPE_MEMORY_OVERUTILIZED: ClusterAlertType
CLUSTER_ALERT_TYPE_OOD: ClusterAlertType
CLUSTER_ALERT_TYPE_OOM: ClusterAlertType
CLUSTER_ALERT_TYPE_RECOVERY_MODE: ClusterAlertType
CLUSTER_ALERT_TYPE_QDRANT_CLUSTER_UNHEALTHY: ClusterAlertType
CLUSTER_ALERT_TYPE_TOO_MANY_COLLECTIONS: ClusterAlertType
CLUSTER_ALERT_TYPE_QDRANT_CLUSTER_CPU_THROTTLED: ClusterAlertType
CLUSTER_ALERT_TYPE_QDRANT_JWT_API_KEY_ABOUT_TO_EXPIRE: ClusterAlertType
CLUSTER_ALERT_TYPE_CLUSTER_VERSION_IS_NOT_COVERED_BY_SLA: ClusterAlertType
CLUSTER_ALERT_TYPE_CLUSTER_DISK_HOTSPOT: ClusterAlertType
CLUSTER_ALERT_TYPE_CLUSTER_MEMORY_HOTSPOT: ClusterAlertType
CLUSTER_ALERT_TYPE_CLUSTER_CPU_HOTSPOT: ClusterAlertType
SEVERITY_UNSPECIFIED: Severity
SEVERITY_INFO: Severity
SEVERITY_WARNING: Severity
SEVERITY_CRITICAL: Severity

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
    __slots__ = ("cpu", "ram", "ram_cache", "ram_rss", "ram_qdrant_rss", "disk", "rps", "latency", "nodes", "gpu", "gpu_ram")
    CPU_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    RAM_CACHE_FIELD_NUMBER: _ClassVar[int]
    RAM_RSS_FIELD_NUMBER: _ClassVar[int]
    RAM_QDRANT_RSS_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    RPS_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    GPU_FIELD_NUMBER: _ClassVar[int]
    GPU_RAM_FIELD_NUMBER: _ClassVar[int]
    cpu: _containers.RepeatedCompositeFieldContainer[Metric]
    ram: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_cache: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_rss: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_qdrant_rss: _containers.RepeatedCompositeFieldContainer[Metric]
    disk: _containers.RepeatedCompositeFieldContainer[Metric]
    rps: _containers.RepeatedCompositeFieldContainer[Metric]
    latency: _containers.RepeatedCompositeFieldContainer[Metric]
    nodes: _containers.RepeatedCompositeFieldContainer[ClusterNodeUsageMetrics]
    gpu: _containers.RepeatedCompositeFieldContainer[Metric]
    gpu_ram: _containers.RepeatedCompositeFieldContainer[Metric]
    def __init__(self, cpu: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_cache: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_rss: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_qdrant_rss: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., disk: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., rps: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., latency: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., nodes: _Optional[_Iterable[_Union[ClusterNodeUsageMetrics, _Mapping]]] = ..., gpu: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., gpu_ram: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ...) -> None: ...

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

class GetClusterEventsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[LogEntry]
    def __init__(self, items: _Optional[_Iterable[_Union[LogEntry, _Mapping]]] = ...) -> None: ...

class GetClusterInferenceMetricsRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "since", "until", "interval", "inference_model_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    interval: InferenceMetricsInterval
    inference_model_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., interval: _Optional[_Union[InferenceMetricsInterval, str]] = ..., inference_model_id: _Optional[str] = ...) -> None: ...

class GetClusterInferenceMetricsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[ClusterInferenceModelMetrics]
    def __init__(self, models: _Optional[_Iterable[_Union[ClusterInferenceModelMetrics, _Mapping]]] = ...) -> None: ...

class ClusterInferenceModelMetrics(_message.Message):
    __slots__ = ("inference_model_id", "values")
    INFERENCE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    inference_model_id: str
    values: _containers.RepeatedCompositeFieldContainer[Metric]
    def __init__(self, inference_model_id: _Optional[str] = ..., values: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ...) -> None: ...

class ClusterNodeMetrics(_message.Message):
    __slots__ = ("node_id", "cpu", "ram", "ram_cache", "ram_rss", "ram_qdrant_rss", "disk", "gpu", "gpu_ram")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    RAM_CACHE_FIELD_NUMBER: _ClassVar[int]
    RAM_RSS_FIELD_NUMBER: _ClassVar[int]
    RAM_QDRANT_RSS_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    GPU_FIELD_NUMBER: _ClassVar[int]
    GPU_RAM_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    cpu: ClusterMetricOverview
    ram: ClusterMetricOverview
    ram_cache: ClusterMetricOverview
    ram_rss: ClusterMetricOverview
    ram_qdrant_rss: ClusterMetricOverview
    disk: ClusterMetricOverview
    gpu: ClusterMetricOverview
    gpu_ram: ClusterMetricOverview
    def __init__(self, node_id: _Optional[str] = ..., cpu: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., ram: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., ram_cache: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., ram_rss: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., ram_qdrant_rss: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., disk: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., gpu: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ..., gpu_ram: _Optional[_Union[ClusterMetricOverview, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("node_id", "cpu", "ram", "ram_cache", "ram_rss", "ram_qdrant_rss", "disk", "gpu", "gpu_ram")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    RAM_CACHE_FIELD_NUMBER: _ClassVar[int]
    RAM_RSS_FIELD_NUMBER: _ClassVar[int]
    RAM_QDRANT_RSS_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    GPU_FIELD_NUMBER: _ClassVar[int]
    GPU_RAM_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    cpu: _containers.RepeatedCompositeFieldContainer[Metric]
    ram: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_cache: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_rss: _containers.RepeatedCompositeFieldContainer[Metric]
    ram_qdrant_rss: _containers.RepeatedCompositeFieldContainer[Metric]
    disk: _containers.RepeatedCompositeFieldContainer[Metric]
    gpu: _containers.RepeatedCompositeFieldContainer[Metric]
    gpu_ram: _containers.RepeatedCompositeFieldContainer[Metric]
    def __init__(self, node_id: _Optional[str] = ..., cpu: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_cache: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_rss: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., ram_qdrant_rss: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., disk: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., gpu: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., gpu_ram: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ...) -> None: ...

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

class ListClusterAlertsRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "state")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    state: ClusterAlertState
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., state: _Optional[_Union[ClusterAlertState, str]] = ...) -> None: ...

class ListClusterAlertsResponse(_message.Message):
    __slots__ = ("alerts",)
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    alerts: _containers.RepeatedCompositeFieldContainer[ClusterAlert]
    def __init__(self, alerts: _Optional[_Iterable[_Union[ClusterAlert, _Mapping]]] = ...) -> None: ...

class ClusterAlert(_message.Message):
    __slots__ = ("id", "type", "severity", "title", "description", "last_firing_at", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAST_FIRING_AT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: ClusterAlertType
    severity: Severity
    title: str
    description: str
    last_firing_at: _timestamp_pb2.Timestamp
    state: ClusterAlertState
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[ClusterAlertType, str]] = ..., severity: _Optional[_Union[Severity, str]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., last_firing_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[ClusterAlertState, str]] = ...) -> None: ...
