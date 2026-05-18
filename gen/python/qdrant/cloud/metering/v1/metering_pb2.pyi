import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMonthlyMeteringsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListMonthlyMeteringsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[MonthlyMeteringSummary]
    def __init__(self, items: _Optional[_Iterable[_Union[MonthlyMeteringSummary, _Mapping]]] = ...) -> None: ...

class ListMeteringsRequest(_message.Message):
    __slots__ = ("account_id", "year", "month")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    year: int
    month: int
    def __init__(self, account_id: _Optional[str] = ..., year: _Optional[int] = ..., month: _Optional[int] = ...) -> None: ...

class ListMeteringsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[MeteringItem]
    def __init__(self, items: _Optional[_Iterable[_Union[MeteringItem, _Mapping]]] = ...) -> None: ...

class MonthlyMeteringSummary(_message.Message):
    __slots__ = ("year", "month", "amount_millicents", "currency")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MILLICENTS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: int
    amount_millicents: int
    currency: str
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., amount_millicents: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class MeteringItem(_message.Message):
    __slots__ = ("account_id", "cluster_id", "cluster_name", "start_time", "end_time", "billable_entity_id", "billable_entity_reference_name", "billable_entity_type", "price_per_hour", "usage_hours", "amount_millicents", "discount_amount_millicents", "discount_amount_percent", "currency", "cluster_labels")
    class ClusterLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    BILLABLE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    BILLABLE_ENTITY_REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    BILLABLE_ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    USAGE_HOURS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MILLICENTS_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNT_MILLICENTS_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LABELS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    cluster_name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    billable_entity_id: str
    billable_entity_reference_name: str
    billable_entity_type: str
    price_per_hour: int
    usage_hours: float
    amount_millicents: int
    discount_amount_millicents: int
    discount_amount_percent: float
    currency: str
    cluster_labels: _containers.ScalarMap[str, str]
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster_name: _Optional[str] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., billable_entity_id: _Optional[str] = ..., billable_entity_reference_name: _Optional[str] = ..., billable_entity_type: _Optional[str] = ..., price_per_hour: _Optional[int] = ..., usage_hours: _Optional[float] = ..., amount_millicents: _Optional[int] = ..., discount_amount_millicents: _Optional[int] = ..., discount_amount_percent: _Optional[float] = ..., currency: _Optional[str] = ..., cluster_labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetUsageBreakdownRequest(_message.Message):
    __slots__ = ("account_id", "start_time", "end_time")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, account_id: _Optional[str] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetUsageBreakdownResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[UsageBreakdownMonth]
    def __init__(self, items: _Optional[_Iterable[_Union[UsageBreakdownMonth, _Mapping]]] = ...) -> None: ...

class UsageBreakdownMonth(_message.Message):
    __slots__ = ("year", "month", "accounts")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: int
    accounts: _containers.RepeatedCompositeFieldContainer[UsageBreakdownAccount]
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., accounts: _Optional[_Iterable[_Union[UsageBreakdownAccount, _Mapping]]] = ...) -> None: ...

class UsageBreakdownAccount(_message.Message):
    __slots__ = ("account_id", "account_name", "clusters")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    account_name: str
    clusters: _containers.RepeatedCompositeFieldContainer[UsageBreakdownCluster]
    def __init__(self, account_id: _Optional[str] = ..., account_name: _Optional[str] = ..., clusters: _Optional[_Iterable[_Union[UsageBreakdownCluster, _Mapping]]] = ...) -> None: ...

class ClusterUsageConfig(_message.Message):
    __slots__ = ("cloud_provider", "region", "cpu_vcpu", "ram_gib", "disk_gib", "multi_az", "gpu_enabled", "pricing_tier", "node_count")
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CPU_VCPU_FIELD_NUMBER: _ClassVar[int]
    RAM_GIB_FIELD_NUMBER: _ClassVar[int]
    DISK_GIB_FIELD_NUMBER: _ClassVar[int]
    MULTI_AZ_FIELD_NUMBER: _ClassVar[int]
    GPU_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRICING_TIER_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    cloud_provider: str
    region: str
    cpu_vcpu: int
    ram_gib: int
    disk_gib: int
    multi_az: bool
    gpu_enabled: bool
    pricing_tier: str
    node_count: int
    def __init__(self, cloud_provider: _Optional[str] = ..., region: _Optional[str] = ..., cpu_vcpu: _Optional[int] = ..., ram_gib: _Optional[int] = ..., disk_gib: _Optional[int] = ..., multi_az: _Optional[bool] = ..., gpu_enabled: _Optional[bool] = ..., pricing_tier: _Optional[str] = ..., node_count: _Optional[int] = ...) -> None: ...

class ClusterExtraDiskConfig(_message.Message):
    __slots__ = ("cloud_provider", "region", "pricing_tier", "extra_disk_gib")
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PRICING_TIER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DISK_GIB_FIELD_NUMBER: _ClassVar[int]
    cloud_provider: str
    region: str
    pricing_tier: str
    extra_disk_gib: int
    def __init__(self, cloud_provider: _Optional[str] = ..., region: _Optional[str] = ..., pricing_tier: _Optional[str] = ..., extra_disk_gib: _Optional[int] = ...) -> None: ...

class ClusterStorageTierConfig(_message.Message):
    __slots__ = ("cloud_provider", "region", "storage_tier", "pricing_tier")
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TIER_FIELD_NUMBER: _ClassVar[int]
    PRICING_TIER_FIELD_NUMBER: _ClassVar[int]
    cloud_provider: str
    region: str
    storage_tier: str
    pricing_tier: str
    def __init__(self, cloud_provider: _Optional[str] = ..., region: _Optional[str] = ..., storage_tier: _Optional[str] = ..., pricing_tier: _Optional[str] = ...) -> None: ...

class BackupStorageConfig(_message.Message):
    __slots__ = ("cloud_provider", "region", "pricing_tier")
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PRICING_TIER_FIELD_NUMBER: _ClassVar[int]
    cloud_provider: str
    region: str
    pricing_tier: str
    def __init__(self, cloud_provider: _Optional[str] = ..., region: _Optional[str] = ..., pricing_tier: _Optional[str] = ...) -> None: ...

class InferenceConfig(_message.Message):
    __slots__ = ("cloud_provider", "region", "model_name", "pricing_tier")
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    PRICING_TIER_FIELD_NUMBER: _ClassVar[int]
    cloud_provider: str
    region: str
    model_name: str
    pricing_tier: str
    def __init__(self, cloud_provider: _Optional[str] = ..., region: _Optional[str] = ..., model_name: _Optional[str] = ..., pricing_tier: _Optional[str] = ...) -> None: ...

class UsageBreakdownCluster(_message.Message):
    __slots__ = ("cluster_id", "cluster_name", "cluster_labels", "start_time", "end_time", "amount_millicents", "currency", "billable_entity_type", "cluster_usage_config", "cluster_extra_disk_config", "cluster_storage_tier_config", "backup_storage_config", "inference_config", "quantity", "discount_amount_millicents", "discount_amount_percent")
    class ClusterLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LABELS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MILLICENTS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    BILLABLE_ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_USAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_EXTRA_DISK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STORAGE_TIER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_STORAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNT_MILLICENTS_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    cluster_name: str
    cluster_labels: _containers.ScalarMap[str, str]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    amount_millicents: int
    currency: str
    billable_entity_type: str
    cluster_usage_config: ClusterUsageConfig
    cluster_extra_disk_config: ClusterExtraDiskConfig
    cluster_storage_tier_config: ClusterStorageTierConfig
    backup_storage_config: BackupStorageConfig
    inference_config: InferenceConfig
    quantity: float
    discount_amount_millicents: int
    discount_amount_percent: float
    def __init__(self, cluster_id: _Optional[str] = ..., cluster_name: _Optional[str] = ..., cluster_labels: _Optional[_Mapping[str, str]] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., amount_millicents: _Optional[int] = ..., currency: _Optional[str] = ..., billable_entity_type: _Optional[str] = ..., cluster_usage_config: _Optional[_Union[ClusterUsageConfig, _Mapping]] = ..., cluster_extra_disk_config: _Optional[_Union[ClusterExtraDiskConfig, _Mapping]] = ..., cluster_storage_tier_config: _Optional[_Union[ClusterStorageTierConfig, _Mapping]] = ..., backup_storage_config: _Optional[_Union[BackupStorageConfig, _Mapping]] = ..., inference_config: _Optional[_Union[InferenceConfig, _Mapping]] = ..., quantity: _Optional[float] = ..., discount_amount_millicents: _Optional[int] = ..., discount_amount_percent: _Optional[float] = ...) -> None: ...
