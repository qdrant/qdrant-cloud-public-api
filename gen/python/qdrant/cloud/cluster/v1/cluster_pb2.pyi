import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
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

class ClusterServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_SERVICE_TYPE_UNSPECIFIED: _ClassVar[ClusterServiceType]
    CLUSTER_SERVICE_TYPE_CLUSTER_IP: _ClassVar[ClusterServiceType]
    CLUSTER_SERVICE_TYPE_NODE_PORT: _ClassVar[ClusterServiceType]
    CLUSTER_SERVICE_TYPE_LOAD_BALANCER: _ClassVar[ClusterServiceType]

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

class AuditLogRotation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_LOG_ROTATION_UNSPECIFIED: _ClassVar[AuditLogRotation]
    AUDIT_LOG_ROTATION_DAILY: _ClassVar[AuditLogRotation]
    AUDIT_LOG_ROTATION_HOURLY: _ClassVar[AuditLogRotation]

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
    CLUSTER_PHASE_DELETING: _ClassVar[ClusterPhase]

class ClusterNodeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_NODE_STATE_UNSPECIFIED: _ClassVar[ClusterNodeState]
    CLUSTER_NODE_STATE_STARTING: _ClassVar[ClusterNodeState]
    CLUSTER_NODE_STATE_HEALTHY: _ClassVar[ClusterNodeState]
    CLUSTER_NODE_STATE_UNHEALTHY: _ClassVar[ClusterNodeState]
    CLUSTER_NODE_STATE_SUSPENDED: _ClassVar[ClusterNodeState]
    CLUSTER_NODE_STATE_RECOVERING: _ClassVar[ClusterNodeState]

class ClusterScalabilityStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_SCALABILITY_STATUS_UNSPECIFIED: _ClassVar[ClusterScalabilityStatus]
    CLUSTER_SCALABILITY_STATUS_NOT_SCALABLE: _ClassVar[ClusterScalabilityStatus]
    CLUSTER_SCALABILITY_STATUS_SCALABLE: _ClassVar[ClusterScalabilityStatus]
CLUSTER_SERVICE_TYPE_UNSPECIFIED: ClusterServiceType
CLUSTER_SERVICE_TYPE_CLUSTER_IP: ClusterServiceType
CLUSTER_SERVICE_TYPE_NODE_PORT: ClusterServiceType
CLUSTER_SERVICE_TYPE_LOAD_BALANCER: ClusterServiceType
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
AUDIT_LOG_ROTATION_UNSPECIFIED: AuditLogRotation
AUDIT_LOG_ROTATION_DAILY: AuditLogRotation
AUDIT_LOG_ROTATION_HOURLY: AuditLogRotation
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
CLUSTER_PHASE_DELETING: ClusterPhase
CLUSTER_NODE_STATE_UNSPECIFIED: ClusterNodeState
CLUSTER_NODE_STATE_STARTING: ClusterNodeState
CLUSTER_NODE_STATE_HEALTHY: ClusterNodeState
CLUSTER_NODE_STATE_UNHEALTHY: ClusterNodeState
CLUSTER_NODE_STATE_SUSPENDED: ClusterNodeState
CLUSTER_NODE_STATE_RECOVERING: ClusterNodeState
CLUSTER_SCALABILITY_STATUS_UNSPECIFIED: ClusterScalabilityStatus
CLUSTER_SCALABILITY_STATUS_NOT_SCALABLE: ClusterScalabilityStatus
CLUSTER_SCALABILITY_STATUS_SCALABLE: ClusterScalabilityStatus

class ListClustersRequest(_message.Message):
    __slots__ = ()
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

class ListClustersResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Cluster]
    total_size: int
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[Cluster, _Mapping]]] = ..., total_size: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetClusterRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class GetClusterResponse(_message.Message):
    __slots__ = ()
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...

class CreateClusterRequest(_message.Message):
    __slots__ = ()
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...

class CreateClusterResponse(_message.Message):
    __slots__ = ()
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ()
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...

class UpdateClusterResponse(_message.Message):
    __slots__ = ()
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    delete_backups: bool
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., delete_backups: _Optional[bool] = ...) -> None: ...

class DeleteClusterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestartClusterRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class RestartClusterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuspendClusterRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class SuspendClusterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnsuspendClusterRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class UnsuspendClusterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnableClusterJwtRbacRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class EnableClusterJwtRbacResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SuggestClusterNameRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class SuggestClusterNameResponse(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListQdrantReleasesRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class ListQdrantReleasesResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[QdrantRelease]
    def __init__(self, items: _Optional[_Iterable[_Union[QdrantRelease, _Mapping]]] = ...) -> None: ...

class GetQdrantReleaseRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    version: str
    def __init__(self, account_id: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class GetQdrantReleaseResponse(_message.Message):
    __slots__ = ()
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    release: QdrantRelease
    def __init__(self, release: _Optional[_Union[QdrantRelease, _Mapping]] = ...) -> None: ...

class Cluster(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    account_id: str
    name: str
    deleted_at: _timestamp_pb2.Timestamp
    cloud_provider_id: str
    cloud_provider_region_id: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    configuration: ClusterConfiguration
    state: ClusterState
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., name: _Optional[str] = ..., deleted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cloud_provider_id: _Optional[str] = ..., cloud_provider_region_id: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ..., configuration: _Optional[_Union[ClusterConfiguration, _Mapping]] = ..., state: _Optional[_Union[ClusterState, _Mapping]] = ...) -> None: ...

class ClusterConfiguration(_message.Message):
    __slots__ = ()
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
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    POD_LABELS_FIELD_NUMBER: _ClassVar[int]
    RESERVED_CPU_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_MEMORY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTART_POLICY_FIELD_NUMBER: _ClassVar[int]
    REBALANCE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_SPREAD_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STORAGE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
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
    service_type: ClusterServiceType
    service_annotations: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    pod_labels: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    reserved_cpu_percentage: int
    reserved_memory_percentage: int
    gpu_type: ClusterConfigurationGpuType
    restart_policy: ClusterConfigurationRestartPolicy
    rebalance_strategy: ClusterConfigurationRebalanceStrategy
    topology_spread_constraints: _containers.RepeatedCompositeFieldContainer[_common_pb2.TopologySpreadConstraint]
    cluster_storage_configuration: ClusterStorageConfiguration
    def __init__(self, last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., number_of_nodes: _Optional[int] = ..., version: _Optional[str] = ..., package_id: _Optional[str] = ..., additional_resources: _Optional[_Union[AdditionalResources, _Mapping]] = ..., database_configuration: _Optional[_Union[DatabaseConfiguration, _Mapping]] = ..., node_selector: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ..., tolerations: _Optional[_Iterable[_Union[Toleration, _Mapping]]] = ..., annotations: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ..., allowed_ip_source_ranges: _Optional[_Iterable[str]] = ..., service_type: _Optional[_Union[ClusterServiceType, str]] = ..., service_annotations: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ..., pod_labels: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ..., reserved_cpu_percentage: _Optional[int] = ..., reserved_memory_percentage: _Optional[int] = ..., gpu_type: _Optional[_Union[ClusterConfigurationGpuType, str]] = ..., restart_policy: _Optional[_Union[ClusterConfigurationRestartPolicy, str]] = ..., rebalance_strategy: _Optional[_Union[ClusterConfigurationRebalanceStrategy, str]] = ..., topology_spread_constraints: _Optional[_Iterable[_Union[_common_pb2.TopologySpreadConstraint, _Mapping]]] = ..., cluster_storage_configuration: _Optional[_Union[ClusterStorageConfiguration, _Mapping]] = ...) -> None: ...

class DatabaseConfiguration(_message.Message):
    __slots__ = ()
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_FIELD_NUMBER: _ClassVar[int]
    AUGIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    collection: DatabaseConfigurationCollection
    storage: DatabaseConfigurationStorage
    service: DatabaseConfigurationService
    log_level: DatabaseConfigurationLogLevel
    tls: DatabaseConfigurationTls
    inference: DatabaseConfigurationInference
    augit_logging: DatabaseConfigurationAuditLogging
    def __init__(self, collection: _Optional[_Union[DatabaseConfigurationCollection, _Mapping]] = ..., storage: _Optional[_Union[DatabaseConfigurationStorage, _Mapping]] = ..., service: _Optional[_Union[DatabaseConfigurationService, _Mapping]] = ..., log_level: _Optional[_Union[DatabaseConfigurationLogLevel, str]] = ..., tls: _Optional[_Union[DatabaseConfigurationTls, _Mapping]] = ..., inference: _Optional[_Union[DatabaseConfigurationInference, _Mapping]] = ..., augit_logging: _Optional[_Union[DatabaseConfigurationAuditLogging, _Mapping]] = ...) -> None: ...

class DatabaseConfigurationCollection(_message.Message):
    __slots__ = ()
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONSISTENCY_FACTOR_FIELD_NUMBER: _ClassVar[int]
    VECTORS_FIELD_NUMBER: _ClassVar[int]
    replication_factor: int
    write_consistency_factor: int
    vectors: DatabaseConfigurationCollectionVectors
    def __init__(self, replication_factor: _Optional[int] = ..., write_consistency_factor: _Optional[int] = ..., vectors: _Optional[_Union[DatabaseConfigurationCollectionVectors, _Mapping]] = ...) -> None: ...

class DatabaseConfigurationCollectionVectors(_message.Message):
    __slots__ = ()
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    on_disk: bool
    def __init__(self, on_disk: _Optional[bool] = ...) -> None: ...

class DatabaseConfigurationStorage(_message.Message):
    __slots__ = ()
    PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    performance: DatabaseConfigurationStoragePerformance
    def __init__(self, performance: _Optional[_Union[DatabaseConfigurationStoragePerformance, _Mapping]] = ...) -> None: ...

class DatabaseConfigurationStoragePerformance(_message.Message):
    __slots__ = ()
    OPTIMIZER_CPU_BUDGET_FIELD_NUMBER: _ClassVar[int]
    ASYNC_SCORER_FIELD_NUMBER: _ClassVar[int]
    optimizer_cpu_budget: int
    async_scorer: bool
    def __init__(self, optimizer_cpu_budget: _Optional[int] = ..., async_scorer: _Optional[bool] = ...) -> None: ...

class DatabaseConfigurationService(_message.Message):
    __slots__ = ()
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_API_KEY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TLS_FIELD_NUMBER: _ClassVar[int]
    api_key: _common_pb2.SecretKeyRef
    read_only_api_key: _common_pb2.SecretKeyRef
    enable_tls: bool
    def __init__(self, api_key: _Optional[_Union[_common_pb2.SecretKeyRef, _Mapping]] = ..., read_only_api_key: _Optional[_Union[_common_pb2.SecretKeyRef, _Mapping]] = ..., enable_tls: _Optional[bool] = ...) -> None: ...

class DatabaseConfigurationTls(_message.Message):
    __slots__ = ()
    CERT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    cert: _common_pb2.SecretKeyRef
    key: _common_pb2.SecretKeyRef
    def __init__(self, cert: _Optional[_Union[_common_pb2.SecretKeyRef, _Mapping]] = ..., key: _Optional[_Union[_common_pb2.SecretKeyRef, _Mapping]] = ...) -> None: ...

class DatabaseConfigurationInference(_message.Message):
    __slots__ = ()
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: _Optional[bool] = ...) -> None: ...

class AdditionalResources(_message.Message):
    __slots__ = ()
    DISK_FIELD_NUMBER: _ClassVar[int]
    disk: int
    def __init__(self, disk: _Optional[int] = ...) -> None: ...

class DatabaseConfigurationAuditLogging(_message.Message):
    __slots__ = ()
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    MAX_LOG_FILES_FIELD_NUMBER: _ClassVar[int]
    TRUST_FORWARDED_HEADERS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    rotation: AuditLogRotation
    max_log_files: int
    trust_forwarded_headers: bool
    def __init__(self, enabled: _Optional[bool] = ..., rotation: _Optional[_Union[AuditLogRotation, str]] = ..., max_log_files: _Optional[int] = ..., trust_forwarded_headers: _Optional[bool] = ...) -> None: ...

class Toleration(_message.Message):
    __slots__ = ()
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

class ClusterStorageConfiguration(_message.Message):
    __slots__ = ()
    STORAGE_TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
    storage_tier_type: _common_pb2.StorageTierType
    def __init__(self, storage_tier_type: _Optional[_Union[_common_pb2.StorageTierType, str]] = ...) -> None: ...

class ClusterState(_message.Message):
    __slots__ = ()
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NODES_UP_FIELD_NUMBER: _ClassVar[int]
    RESTARTED_AT_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SCALABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    JWT_RBAC_FIELD_NUMBER: _ClassVar[int]
    version: str
    nodes_up: int
    restarted_at: _timestamp_pb2.Timestamp
    phase: ClusterPhase
    reason: str
    endpoint: ClusterEndpoint
    resources: ClusterNodeResourcesSummary
    scalability_info: ClusterScalabilityInfo
    nodes: _containers.RepeatedCompositeFieldContainer[ClusterNodeInfo]
    jwt_rbac: bool
    def __init__(self, version: _Optional[str] = ..., nodes_up: _Optional[int] = ..., restarted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., phase: _Optional[_Union[ClusterPhase, str]] = ..., reason: _Optional[str] = ..., endpoint: _Optional[_Union[ClusterEndpoint, _Mapping]] = ..., resources: _Optional[_Union[ClusterNodeResourcesSummary, _Mapping]] = ..., scalability_info: _Optional[_Union[ClusterScalabilityInfo, _Mapping]] = ..., nodes: _Optional[_Iterable[_Union[ClusterNodeInfo, _Mapping]]] = ..., jwt_rbac: _Optional[bool] = ...) -> None: ...

class ClusterNodeInfo(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    name: str
    started_at: _timestamp_pb2.Timestamp
    version: str
    endpoint: ClusterEndpoint
    state: ClusterNodeState
    availability_zone: str
    def __init__(self, name: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[str] = ..., endpoint: _Optional[_Union[ClusterEndpoint, _Mapping]] = ..., state: _Optional[_Union[ClusterNodeState, str]] = ..., availability_zone: _Optional[str] = ...) -> None: ...

class ClusterEndpoint(_message.Message):
    __slots__ = ()
    URL_FIELD_NUMBER: _ClassVar[int]
    REST_PORT_FIELD_NUMBER: _ClassVar[int]
    GRPC_PORT_FIELD_NUMBER: _ClassVar[int]
    url: str
    rest_port: int
    grpc_port: int
    def __init__(self, url: _Optional[str] = ..., rest_port: _Optional[int] = ..., grpc_port: _Optional[int] = ...) -> None: ...

class ClusterNodeResourcesSummary(_message.Message):
    __slots__ = ()
    DISK_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    GPU_FIELD_NUMBER: _ClassVar[int]
    disk: ClusterNodeResources
    ram: ClusterNodeResources
    cpu: ClusterNodeResources
    gpu: ClusterNodeResources
    def __init__(self, disk: _Optional[_Union[ClusterNodeResources, _Mapping]] = ..., ram: _Optional[_Union[ClusterNodeResources, _Mapping]] = ..., cpu: _Optional[_Union[ClusterNodeResources, _Mapping]] = ..., gpu: _Optional[_Union[ClusterNodeResources, _Mapping]] = ...) -> None: ...

class ClusterNodeResources(_message.Message):
    __slots__ = ()
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

class ClusterScalabilityInfo(_message.Message):
    __slots__ = ()
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    status: ClusterScalabilityStatus
    reason: str
    def __init__(self, status: _Optional[_Union[ClusterScalabilityStatus, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class QdrantRelease(_message.Message):
    __slots__ = ()
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
    def __init__(self, version: _Optional[str] = ..., default: _Optional[bool] = ..., release_notes_url: _Optional[str] = ..., remarks: _Optional[str] = ..., end_of_life: _Optional[bool] = ..., unavailable: _Optional[bool] = ...) -> None: ...

class CreateClusterFromBackupRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    backup_id: str
    cluster_name: str
    def __init__(self, account_id: _Optional[str] = ..., backup_id: _Optional[str] = ..., cluster_name: _Optional[str] = ...) -> None: ...

class CreateClusterFromBackupResponse(_message.Message):
    __slots__ = ()
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ...) -> None: ...
