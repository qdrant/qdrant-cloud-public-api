from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterConfigurationGpuType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_CONFIGURATION_GPU_TYPE_UNSPECIFIED: _ClassVar[ClusterConfigurationGpuType]
    CLUSTER_CONFIGURATION_GPU_TYPE_NVIDIA: _ClassVar[ClusterConfigurationGpuType]
    CLUSTER_CONFIGURATION_GPU_TYPE_AMD: _ClassVar[ClusterConfigurationGpuType]

class ClusterConfigurationRestartPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_CONFIGURATION_RESTART_POLICY_UNSPECIFIED: _ClassVar[ClusterConfigurationRestartPolicy]
    CLUSTER_CONFIGURATION_RESTART_POLICY_ROLLING: _ClassVar[ClusterConfigurationRestartPolicy]
    CLUSTER_CONFIGURATION_RESTART_POLICY_PARALLEL: _ClassVar[ClusterConfigurationRestartPolicy]
    CLUSTER_CONFIGURATION_RESTART_POLICY_AUTOMATIC: _ClassVar[ClusterConfigurationRestartPolicy]

class ClusterConfigurationRebalanceStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_UNSPECIFIED: _ClassVar[ClusterConfigurationRebalanceStrategy]
    CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_BY_COUNT: _ClassVar[ClusterConfigurationRebalanceStrategy]
    CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_BY_SIZE: _ClassVar[ClusterConfigurationRebalanceStrategy]
    CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_BY_COUNT_AND_SIZE: _ClassVar[ClusterConfigurationRebalanceStrategy]

class DatabaseConfigurationLogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_CONFIGURATION_LOG_LEVEL_UNSPECIFIED: _ClassVar[DatabaseConfigurationLogLevel]
    DATABASE_CONFIGURATION_LOG_LEVEL_TRACE: _ClassVar[DatabaseConfigurationLogLevel]
    DATABASE_CONFIGURATION_LOG_LEVEL_DEBUG: _ClassVar[DatabaseConfigurationLogLevel]
    DATABASE_CONFIGURATION_LOG_LEVEL_INFO: _ClassVar[DatabaseConfigurationLogLevel]
    DATABASE_CONFIGURATION_LOG_LEVEL_WARN: _ClassVar[DatabaseConfigurationLogLevel]
    DATABASE_CONFIGURATION_LOG_LEVEL_ERROR: _ClassVar[DatabaseConfigurationLogLevel]
    DATABASE_CONFIGURATION_LOG_LEVEL_OFF: _ClassVar[DatabaseConfigurationLogLevel]

class TolerationOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOLERATION_OPERATOR_UNSPECIFIED: _ClassVar[TolerationOperator]
    TOLERATION_OPERATOR_EXISTS: _ClassVar[TolerationOperator]
    TOLERATION_OPERATOR_EQUAL: _ClassVar[TolerationOperator]

class TolerationEffect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOLERATION_EFFECT_UNSPECIFIED: _ClassVar[TolerationEffect]
    TOLERATION_EFFECT_NO_SCHEDULE: _ClassVar[TolerationEffect]
    TOLERATION_EFFECT_PREFER_NO_SCHEDULE: _ClassVar[TolerationEffect]
    TOLERATION_EFFECT_NO_EXECUTE: _ClassVar[TolerationEffect]

class ClusterPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_PHASE_UNSPECIFIED: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_CREATING: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_FAILED_TO_CREATE: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_UPDATING: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_FAILED_TO_UPDATE: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_SCALING: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_UPGRADING: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_SUSPENDING: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_SUSPENDED: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_FAILED_TO_SUSPEND: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_RESUMING: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_FAILED_TO_RESUME: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_HEALTHY: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_NOT_READY: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_RECOVERY_MODE: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_MANUAL_MAINTENANCE: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_FAILED_TO_SYNC: _ClassVar[ClusterPhase]
    CLUSTER_PHASE_NOT_FOUND: _ClassVar[ClusterPhase]
CLUSTER_CONFIGURATION_GPU_TYPE_UNSPECIFIED: ClusterConfigurationGpuType
CLUSTER_CONFIGURATION_GPU_TYPE_NVIDIA: ClusterConfigurationGpuType
CLUSTER_CONFIGURATION_GPU_TYPE_AMD: ClusterConfigurationGpuType
CLUSTER_CONFIGURATION_RESTART_POLICY_UNSPECIFIED: ClusterConfigurationRestartPolicy
CLUSTER_CONFIGURATION_RESTART_POLICY_ROLLING: ClusterConfigurationRestartPolicy
CLUSTER_CONFIGURATION_RESTART_POLICY_PARALLEL: ClusterConfigurationRestartPolicy
CLUSTER_CONFIGURATION_RESTART_POLICY_AUTOMATIC: ClusterConfigurationRestartPolicy
CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_UNSPECIFIED: ClusterConfigurationRebalanceStrategy
CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_BY_COUNT: ClusterConfigurationRebalanceStrategy
CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_BY_SIZE: ClusterConfigurationRebalanceStrategy
CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_BY_COUNT_AND_SIZE: ClusterConfigurationRebalanceStrategy
DATABASE_CONFIGURATION_LOG_LEVEL_UNSPECIFIED: DatabaseConfigurationLogLevel
DATABASE_CONFIGURATION_LOG_LEVEL_TRACE: DatabaseConfigurationLogLevel
DATABASE_CONFIGURATION_LOG_LEVEL_DEBUG: DatabaseConfigurationLogLevel
DATABASE_CONFIGURATION_LOG_LEVEL_INFO: DatabaseConfigurationLogLevel
DATABASE_CONFIGURATION_LOG_LEVEL_WARN: DatabaseConfigurationLogLevel
DATABASE_CONFIGURATION_LOG_LEVEL_ERROR: DatabaseConfigurationLogLevel
DATABASE_CONFIGURATION_LOG_LEVEL_OFF: DatabaseConfigurationLogLevel
TOLERATION_OPERATOR_UNSPECIFIED: TolerationOperator
TOLERATION_OPERATOR_EXISTS: TolerationOperator
TOLERATION_OPERATOR_EQUAL: TolerationOperator
TOLERATION_EFFECT_UNSPECIFIED: TolerationEffect
TOLERATION_EFFECT_NO_SCHEDULE: TolerationEffect
TOLERATION_EFFECT_PREFER_NO_SCHEDULE: TolerationEffect
TOLERATION_EFFECT_NO_EXECUTE: TolerationEffect
CLUSTER_PHASE_UNSPECIFIED: ClusterPhase
CLUSTER_PHASE_CREATING: ClusterPhase
CLUSTER_PHASE_FAILED_TO_CREATE: ClusterPhase
CLUSTER_PHASE_UPDATING: ClusterPhase
CLUSTER_PHASE_FAILED_TO_UPDATE: ClusterPhase
CLUSTER_PHASE_SCALING: ClusterPhase
CLUSTER_PHASE_UPGRADING: ClusterPhase
CLUSTER_PHASE_SUSPENDING: ClusterPhase
CLUSTER_PHASE_SUSPENDED: ClusterPhase
CLUSTER_PHASE_FAILED_TO_SUSPEND: ClusterPhase
CLUSTER_PHASE_RESUMING: ClusterPhase
CLUSTER_PHASE_FAILED_TO_RESUME: ClusterPhase
CLUSTER_PHASE_HEALTHY: ClusterPhase
CLUSTER_PHASE_NOT_READY: ClusterPhase
CLUSTER_PHASE_RECOVERY_MODE: ClusterPhase
CLUSTER_PHASE_MANUAL_MAINTENANCE: ClusterPhase
CLUSTER_PHASE_FAILED_TO_SYNC: ClusterPhase
CLUSTER_PHASE_NOT_FOUND: ClusterPhase

class ListClustersRequest(_message.Message):
    __slots__ = ("account_id", "cloud_provider_id", "cloud_provider_region_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cloud_provider_id: str
    cloud_provider_region_id: str
    def __init__(self, account_id: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ..., cloud_provider_region_id: _Optional[str] = ...) -> None: ...

class ListClustersResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Cluster]
    def __init__(self, items: _Optional[_Iterable[_Union[Cluster, _Mapping]]] = ...) -> None: ...

class GetClusterRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class GetClusterResponse(_message.Message):
    __slots__ = ("cluster",)
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...

class CreateClusterRequest(_message.Message):
    __slots__ = ("cluster",)
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...

class CreateClusterResponse(_message.Message):
    __slots__ = ("cluster",)
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ("cluster",)
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...

class UpdateClusterResponse(_message.Message):
    __slots__ = ("cluster",)
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id", "delete_backups")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    delete_backups: bool
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., delete_backups: bool = ...) -> None: ...

class DeleteClusterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestartClusterRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class RestartClusterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuspendClusterRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class SuspendClusterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuggestClusterNameRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class SuggestClusterNameResponse(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListQdrantReleasesRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class ListQdrantReleasesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[QdrantRelease]
    def __init__(self, items: _Optional[_Iterable[_Union[QdrantRelease, _Mapping]]] = ...) -> None: ...

class Cluster(_message.Message):
    __slots__ = ("id", "created_at", "account_id", "name", "deleted_at", "cloud_provider_id", "cloud_provider_region_id", "configuration", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    account_id: str
    name: str
    deleted_at: _timestamp_pb2.Timestamp
    cloud_provider_id: str
    cloud_provider_region_id: str
    configuration: ClusterConfiguration
    state: ClusterState
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., name: _Optional[str] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cloud_provider_id: _Optional[str] = ..., cloud_provider_region_id: _Optional[str] = ..., configuration: _Optional[_Union[ClusterConfiguration, _Mapping]] = ..., state: _Optional[_Union[ClusterState, _Mapping]] = ...) -> None: ...

class ClusterConfiguration(_message.Message):
    __slots__ = ("last_modified_at", "number_of_nodes", "version", "package_id", "additional_resources", "database_configuration", "node_selector", "tolerations", "annotations", "allowed_ip_source_ranges", "reserved_cpu_percentage", "reserved_memory_percentage", "gpu_type", "restart_policy", "rebalance_strategy")
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_NODES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    DATABASE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    TOLERATIONS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_IP_SOURCE_RANGES_FIELD_NUMBER: _ClassVar[int]
    RESERVED_CPU_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_MEMORY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTART_POLICY_FIELD_NUMBER: _ClassVar[int]
    REBALANCE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    last_modified_at: _timestamp_pb2.Timestamp
    number_of_nodes: int
    version: str
    package_id: str
    additional_resources: AdditionalResources
    database_configuration: DatabaseConfiguration
    node_selector: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    tolerations: _containers.RepeatedCompositeFieldContainer[Toleration]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    allowed_ip_source_ranges: _containers.RepeatedScalarFieldContainer[str]
    reserved_cpu_percentage: int
    reserved_memory_percentage: int
    gpu_type: ClusterConfigurationGpuType
    restart_policy: ClusterConfigurationRestartPolicy
    rebalance_strategy: ClusterConfigurationRebalanceStrategy
    def __init__(self, last_modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., number_of_nodes: _Optional[int] = ..., version: _Optional[str] = ..., package_id: _Optional[str] = ..., additional_resources: _Optional[_Union[AdditionalResources, _Mapping]] = ..., database_configuration: _Optional[_Union[DatabaseConfiguration, _Mapping]] = ..., node_selector: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ..., tolerations: _Optional[_Iterable[_Union[Toleration, _Mapping]]] = ..., annotations: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ..., allowed_ip_source_ranges: _Optional[_Iterable[str]] = ..., reserved_cpu_percentage: _Optional[int] = ..., reserved_memory_percentage: _Optional[int] = ..., gpu_type: _Optional[_Union[ClusterConfigurationGpuType, str]] = ..., restart_policy: _Optional[_Union[ClusterConfigurationRestartPolicy, str]] = ..., rebalance_strategy: _Optional[_Union[ClusterConfigurationRebalanceStrategy, str]] = ...) -> None: ...

class DatabaseConfiguration(_message.Message):
    __slots__ = ("collection", "storage", "service", "log_level", "tls", "inference")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_FIELD_NUMBER: _ClassVar[int]
    collection: DatabaseConfigurationCollection
    storage: DatabaseConfigurationStorage
    service: DatabaseConfigurationService
    log_level: DatabaseConfigurationLogLevel
    tls: DatabaseConfigurationTls
    inference: DatabaseConfigurationInference
    def __init__(self, collection: _Optional[_Union[DatabaseConfigurationCollection, _Mapping]] = ..., storage: _Optional[_Union[DatabaseConfigurationStorage, _Mapping]] = ..., service: _Optional[_Union[DatabaseConfigurationService, _Mapping]] = ..., log_level: _Optional[_Union[DatabaseConfigurationLogLevel, str]] = ..., tls: _Optional[_Union[DatabaseConfigurationTls, _Mapping]] = ..., inference: _Optional[_Union[DatabaseConfigurationInference, _Mapping]] = ...) -> None: ...

class DatabaseConfigurationCollection(_message.Message):
    __slots__ = ("replication_factor", "write_consistency_factor", "vectors")
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONSISTENCY_FACTOR_FIELD_NUMBER: _ClassVar[int]
    VECTORS_FIELD_NUMBER: _ClassVar[int]
    replication_factor: int
    write_consistency_factor: int
    vectors: DatabaseConfigurationCollectionVectors
    def __init__(self, replication_factor: _Optional[int] = ..., write_consistency_factor: _Optional[int] = ..., vectors: _Optional[_Union[DatabaseConfigurationCollectionVectors, _Mapping]] = ...) -> None: ...

class DatabaseConfigurationCollectionVectors(_message.Message):
    __slots__ = ("on_disk",)
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    on_disk: bool
    def __init__(self, on_disk: bool = ...) -> None: ...

class DatabaseConfigurationStorage(_message.Message):
    __slots__ = ("performance",)
    PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    performance: DatabaseConfigurationStoragePerformance
    def __init__(self, performance: _Optional[_Union[DatabaseConfigurationStoragePerformance, _Mapping]] = ...) -> None: ...

class DatabaseConfigurationStoragePerformance(_message.Message):
    __slots__ = ("optimizer_cpu_budget", "async_scorer")
    OPTIMIZER_CPU_BUDGET_FIELD_NUMBER: _ClassVar[int]
    ASYNC_SCORER_FIELD_NUMBER: _ClassVar[int]
    optimizer_cpu_budget: int
    async_scorer: bool
    def __init__(self, optimizer_cpu_budget: _Optional[int] = ..., async_scorer: bool = ...) -> None: ...

class DatabaseConfigurationService(_message.Message):
    __slots__ = ("api_key", "read_only_api_key", "jwt_rbac", "enable_tls")
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_API_KEY_FIELD_NUMBER: _ClassVar[int]
    JWT_RBAC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TLS_FIELD_NUMBER: _ClassVar[int]
    api_key: _common_pb2.SecretKeyRef
    read_only_api_key: _common_pb2.SecretKeyRef
    jwt_rbac: bool
    enable_tls: bool
    def __init__(self, api_key: _Optional[_Union[_common_pb2.SecretKeyRef, _Mapping]] = ..., read_only_api_key: _Optional[_Union[_common_pb2.SecretKeyRef, _Mapping]] = ..., jwt_rbac: bool = ..., enable_tls: bool = ...) -> None: ...

class DatabaseConfigurationTls(_message.Message):
    __slots__ = ("cert", "key")
    CERT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    cert: _common_pb2.SecretKeyRef
    key: _common_pb2.SecretKeyRef
    def __init__(self, cert: _Optional[_Union[_common_pb2.SecretKeyRef, _Mapping]] = ..., key: _Optional[_Union[_common_pb2.SecretKeyRef, _Mapping]] = ...) -> None: ...

class DatabaseConfigurationInference(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class AdditionalResources(_message.Message):
    __slots__ = ("disk",)
    DISK_FIELD_NUMBER: _ClassVar[int]
    disk: int
    def __init__(self, disk: _Optional[int] = ...) -> None: ...

class Toleration(_message.Message):
    __slots__ = ("key", "operator", "value", "effect", "toleration_seconds")
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    TOLERATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    key: str
    operator: TolerationOperator
    value: str
    effect: TolerationEffect
    toleration_seconds: int
    def __init__(self, key: _Optional[str] = ..., operator: _Optional[_Union[TolerationOperator, str]] = ..., value: _Optional[str] = ..., effect: _Optional[_Union[TolerationEffect, str]] = ..., toleration_seconds: _Optional[int] = ...) -> None: ...

class ClusterState(_message.Message):
    __slots__ = ("version", "nodes_up", "restarted_at", "phase", "reason", "endpoint", "resources")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NODES_UP_FIELD_NUMBER: _ClassVar[int]
    RESTARTED_AT_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    version: str
    nodes_up: int
    restarted_at: _timestamp_pb2.Timestamp
    phase: ClusterPhase
    reason: str
    endpoint: ClusterEndpoint
    resources: ClusterNodeResourcesSummary
    def __init__(self, version: _Optional[str] = ..., nodes_up: _Optional[int] = ..., restarted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., phase: _Optional[_Union[ClusterPhase, str]] = ..., reason: _Optional[str] = ..., endpoint: _Optional[_Union[ClusterEndpoint, _Mapping]] = ..., resources: _Optional[_Union[ClusterNodeResourcesSummary, _Mapping]] = ...) -> None: ...

class ClusterEndpoint(_message.Message):
    __slots__ = ("url", "rest_port", "grpc_port")
    URL_FIELD_NUMBER: _ClassVar[int]
    REST_PORT_FIELD_NUMBER: _ClassVar[int]
    GRPC_PORT_FIELD_NUMBER: _ClassVar[int]
    url: str
    rest_port: int
    grpc_port: int
    def __init__(self, url: _Optional[str] = ..., rest_port: _Optional[int] = ..., grpc_port: _Optional[int] = ...) -> None: ...

class ClusterNodeResourcesSummary(_message.Message):
    __slots__ = ("disk", "ram", "cpu")
    DISK_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    disk: ClusterNodeResources
    ram: ClusterNodeResources
    cpu: ClusterNodeResources
    def __init__(self, disk: _Optional[_Union[ClusterNodeResources, _Mapping]] = ..., ram: _Optional[_Union[ClusterNodeResources, _Mapping]] = ..., cpu: _Optional[_Union[ClusterNodeResources, _Mapping]] = ...) -> None: ...

class ClusterNodeResources(_message.Message):
    __slots__ = ("base", "complimentary", "additional", "reserved", "available")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COMPLIMENTARY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FIELD_NUMBER: _ClassVar[int]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    base: float
    complimentary: float
    additional: float
    reserved: float
    available: float
    def __init__(self, base: _Optional[float] = ..., complimentary: _Optional[float] = ..., additional: _Optional[float] = ..., reserved: _Optional[float] = ..., available: _Optional[float] = ...) -> None: ...

class QdrantRelease(_message.Message):
    __slots__ = ("version", "default", "release_notes_url", "remarks", "end_of_life", "unavailable")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NOTES_URL_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    END_OF_LIFE_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    version: str
    default: bool
    release_notes_url: str
    remarks: str
    end_of_life: bool
    unavailable: bool
    def __init__(self, version: _Optional[str] = ..., default: bool = ..., release_notes_url: _Optional[str] = ..., remarks: _Optional[str] = ..., end_of_life: bool = ..., unavailable: bool = ...) -> None: ...
