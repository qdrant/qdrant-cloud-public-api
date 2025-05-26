from k8s.io.api.core.v1 import generated_pb2 as _generated_pb2
from k8s.io.api.networking.v1 import generated_pb2 as _generated_pb2_1
from k8s.io.api.policy.v1 import generated_pb2 as _generated_pb2_1_1
from qdrant.cloud.cluster.v1 import cluster_pb2 as _cluster_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OperatorConfiguration(_message.Message):
    __slots__ = ("log_level", "features")
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    log_level: str
    features: OperatorFeatures
    def __init__(self, log_level: _Optional[str] = ..., features: _Optional[_Union[OperatorFeatures, _Mapping]] = ...) -> None: ...

class OperatorFeatures(_message.Message):
    __slots__ = ("cluster_management", "backup_management")
    CLUSTER_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    cluster_management: OperatorClusterManagement
    backup_management: OperatorBackupManagement
    def __init__(self, cluster_management: _Optional[_Union[OperatorClusterManagement, _Mapping]] = ..., backup_management: _Optional[_Union[OperatorBackupManagement, _Mapping]] = ...) -> None: ...

class OperatorBackupManagement(_message.Message):
    __slots__ = ("enabled", "snapshots", "scheduled_snapshots", "restores")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    RESTORES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    snapshots: OperatorSnapshots
    scheduled_snapshots: OperatorScheduledSnapshots
    restores: OperatorRestores
    def __init__(self, enabled: bool = ..., snapshots: _Optional[_Union[OperatorSnapshots, _Mapping]] = ..., scheduled_snapshots: _Optional[_Union[OperatorScheduledSnapshots, _Mapping]] = ..., restores: _Optional[_Union[OperatorRestores, _Mapping]] = ...) -> None: ...

class OperatorSnapshots(_message.Message):
    __slots__ = ("enabled", "volume_snapshot_class", "retain_unsuccessful", "max_concurrent_reconciles")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_CLASS_FIELD_NUMBER: _ClassVar[int]
    RETAIN_UNSUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_RECONCILES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    volume_snapshot_class: str
    retain_unsuccessful: str
    max_concurrent_reconciles: int
    def __init__(self, enabled: bool = ..., volume_snapshot_class: _Optional[str] = ..., retain_unsuccessful: _Optional[str] = ..., max_concurrent_reconciles: _Optional[int] = ...) -> None: ...

class OperatorScheduledSnapshots(_message.Message):
    __slots__ = ("enable", "max_concurrent_reconciles")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_RECONCILES_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    max_concurrent_reconciles: int
    def __init__(self, enable: bool = ..., max_concurrent_reconciles: _Optional[int] = ...) -> None: ...

class OperatorRestores(_message.Message):
    __slots__ = ("enable", "max_concurrent_reconciles")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_RECONCILES_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    max_concurrent_reconciles: int
    def __init__(self, enable: bool = ..., max_concurrent_reconciles: _Optional[int] = ...) -> None: ...

class OperatorClusterManagement(_message.Message):
    __slots__ = ("enabled", "storage_class", "qdrant", "scheduling", "cluster_manager", "ingress", "telemetry_timeout", "max_concurrent_reconciles", "volume_expansion_mode")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    QDRANT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_MANAGER_FIELD_NUMBER: _ClassVar[int]
    INGRESS_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_RECONCILES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_EXPANSION_MODE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    storage_class: OperatorStorageClass
    qdrant: OperatorQdrant
    scheduling: OperatorScheduling
    cluster_manager: OperatorClusterManager
    ingress: OperatorIngress
    telemetry_timeout: str
    max_concurrent_reconciles: int
    volume_expansion_mode: str
    def __init__(self, enabled: bool = ..., storage_class: _Optional[_Union[OperatorStorageClass, _Mapping]] = ..., qdrant: _Optional[_Union[OperatorQdrant, _Mapping]] = ..., scheduling: _Optional[_Union[OperatorScheduling, _Mapping]] = ..., cluster_manager: _Optional[_Union[OperatorClusterManager, _Mapping]] = ..., ingress: _Optional[_Union[OperatorIngress, _Mapping]] = ..., telemetry_timeout: _Optional[str] = ..., max_concurrent_reconciles: _Optional[int] = ..., volume_expansion_mode: _Optional[str] = ...) -> None: ...

class OperatorScheduling(_message.Message):
    __slots__ = ("topology_spread_constraints", "pod_disruption_budget")
    TOPOLOGY_SPREAD_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    POD_DISRUPTION_BUDGET_FIELD_NUMBER: _ClassVar[int]
    topology_spread_constraints: _containers.RepeatedCompositeFieldContainer[_generated_pb2.TopologySpreadConstraint]
    pod_disruption_budget: _containers.RepeatedCompositeFieldContainer[_generated_pb2_1_1.PodDisruptionBudget]
    def __init__(self, topology_spread_constraints: _Optional[_Iterable[_Union[_generated_pb2.TopologySpreadConstraint, _Mapping]]] = ..., pod_disruption_budget: _Optional[_Iterable[_Union[_generated_pb2_1_1.PodDisruptionBudget, _Mapping]]] = ...) -> None: ...

class OperatorClusterManager(_message.Message):
    __slots__ = ("enable", "endpoint_address", "invocation_interval", "timeout", "manage_rules_overrides")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MANAGE_RULES_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    endpoint_address: str
    invocation_interval: str
    timeout: str
    manage_rules_overrides: OperatorClusterManagerOverrides
    def __init__(self, enable: bool = ..., endpoint_address: _Optional[str] = ..., invocation_interval: _Optional[str] = ..., timeout: _Optional[str] = ..., manage_rules_overrides: _Optional[_Union[OperatorClusterManagerOverrides, _Mapping]] = ...) -> None: ...

class OperatorIngress(_message.Message):
    __slots__ = ("enable", "provider", "kubernetes_ingress")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_INGRESS_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    provider: str
    kubernetes_ingress: OperatorKubernetesIngress
    def __init__(self, enable: bool = ..., provider: _Optional[str] = ..., kubernetes_ingress: _Optional[_Union[OperatorKubernetesIngress, _Mapping]] = ...) -> None: ...

class OperatorKubernetesIngress(_message.Message):
    __slots__ = ("ingress_class_name",)
    INGRESS_CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    ingress_class_name: str
    def __init__(self, ingress_class_name: _Optional[str] = ...) -> None: ...

class OperatorClusterManagerOverrides(_message.Message):
    __slots__ = ("dry_run", "max_transfers", "max_transfers_per_collection", "rebalance", "replicate")
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    MAX_TRANSFERS_FIELD_NUMBER: _ClassVar[int]
    MAX_TRANSFERS_PER_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    REBALANCE_FIELD_NUMBER: _ClassVar[int]
    REPLICATE_FIELD_NUMBER: _ClassVar[int]
    dry_run: bool
    max_transfers: int
    max_transfers_per_collection: int
    rebalance: str
    replicate: str
    def __init__(self, dry_run: bool = ..., max_transfers: _Optional[int] = ..., max_transfers_per_collection: _Optional[int] = ..., rebalance: _Optional[str] = ..., replicate: _Optional[str] = ...) -> None: ...

class OperatorStorageClass(_message.Message):
    __slots__ = ("database", "snapshot")
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    database: str
    snapshot: str
    def __init__(self, database: _Optional[str] = ..., snapshot: _Optional[str] = ...) -> None: ...

class OperatorQdrant(_message.Message):
    __slots__ = ("image", "storage", "log_level", "security_context", "network_policies")
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POLICIES_FIELD_NUMBER: _ClassVar[int]
    image: OperatorQdrantImage
    storage: OperatorQdrantStorage
    log_level: _cluster_pb2.DatabaseConfigurationLogLevel
    security_context: OperatorSecurityContext
    network_policies: OperatorNetworkPolicy
    def __init__(self, image: _Optional[_Union[OperatorQdrantImage, _Mapping]] = ..., storage: _Optional[_Union[OperatorQdrantStorage, _Mapping]] = ..., log_level: _Optional[_Union[_cluster_pb2.DatabaseConfigurationLogLevel, str]] = ..., security_context: _Optional[_Union[OperatorSecurityContext, _Mapping]] = ..., network_policies: _Optional[_Union[OperatorNetworkPolicy, _Mapping]] = ...) -> None: ...

class OperatorNetworkPolicy(_message.Message):
    __slots__ = ("enabled", "ingress", "egress")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    INGRESS_FIELD_NUMBER: _ClassVar[int]
    EGRESS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    ingress: _containers.RepeatedCompositeFieldContainer[_generated_pb2_1.NetworkPolicyIngressRule]
    egress: _containers.RepeatedCompositeFieldContainer[_generated_pb2_1.NetworkPolicyEgressRule]
    def __init__(self, enabled: bool = ..., ingress: _Optional[_Iterable[_Union[_generated_pb2_1.NetworkPolicyIngressRule, _Mapping]]] = ..., egress: _Optional[_Iterable[_Union[_generated_pb2_1.NetworkPolicyEgressRule, _Mapping]]] = ...) -> None: ...

class OperatorSecurityContext(_message.Message):
    __slots__ = ("enabled", "user", "fs_group", "group")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    FS_GROUP_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    user: str
    fs_group: str
    group: str
    def __init__(self, enabled: bool = ..., user: _Optional[str] = ..., fs_group: _Optional[str] = ..., group: _Optional[str] = ...) -> None: ...

class OperatorQdrantStorage(_message.Message):
    __slots__ = ("performance",)
    PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    performance: OperatorQdrantPerformance
    def __init__(self, performance: _Optional[_Union[OperatorQdrantPerformance, _Mapping]] = ...) -> None: ...

class OperatorQdrantPerformance(_message.Message):
    __slots__ = ("optimizer_cpu_budget", "async_scorer")
    OPTIMIZER_CPU_BUDGET_FIELD_NUMBER: _ClassVar[int]
    ASYNC_SCORER_FIELD_NUMBER: _ClassVar[int]
    optimizer_cpu_budget: int
    async_scorer: bool
    def __init__(self, optimizer_cpu_budget: _Optional[int] = ..., async_scorer: bool = ...) -> None: ...

class OperatorQdrantImage(_message.Message):
    __slots__ = ("repository", "pull_policy", "pull_secret_name")
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    PULL_POLICY_FIELD_NUMBER: _ClassVar[int]
    PULL_SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
    repository: str
    pull_policy: str
    pull_secret_name: str
    def __init__(self, repository: _Optional[str] = ..., pull_policy: _Optional[str] = ..., pull_secret_name: _Optional[str] = ...) -> None: ...
