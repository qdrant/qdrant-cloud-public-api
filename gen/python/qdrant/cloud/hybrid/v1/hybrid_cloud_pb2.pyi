from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.cluster.v1 import cluster_pb2 as _cluster_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HybridCloudEnvironmentStatusPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIVATE_REGION_STATUS_PHASE_READY: _ClassVar[HybridCloudEnvironmentStatusPhase]
    PRIVATE_REGION_STATUS_PHASE_NOT_READY: _ClassVar[HybridCloudEnvironmentStatusPhase]
    PRIVATE_REGION_STATUS_PHASE_FAILED_TO_SYNC: _ClassVar[HybridCloudEnvironmentStatusPhase]
    PRIVATE_REGION_STATUS_PHASE_UNKNOWN: _ClassVar[HybridCloudEnvironmentStatusPhase]

class HybridCloudEnvironmentComponentStatusPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_READY: _ClassVar[HybridCloudEnvironmentComponentStatusPhase]
    HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_NOT_READY: _ClassVar[HybridCloudEnvironmentComponentStatusPhase]
    HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_NOT_FOUND: _ClassVar[HybridCloudEnvironmentComponentStatusPhase]
    HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_UNKNOWN: _ClassVar[HybridCloudEnvironmentComponentStatusPhase]

class KubernetesDistribution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KUBERNETES_DISTRIBUTION_UNKNOWN: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_AWS: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_GCP: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_AZURE: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_DO: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_SCALEWAY: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_OPENSHIFT: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_LINODE: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_CIVO: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_OCI: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_OVHCLOUD: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_STACKIT: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_VULTR: _ClassVar[KubernetesDistribution]
    KUBERNETES_DISTRIBUTION_K3S: _ClassVar[KubernetesDistribution]
PRIVATE_REGION_STATUS_PHASE_READY: HybridCloudEnvironmentStatusPhase
PRIVATE_REGION_STATUS_PHASE_NOT_READY: HybridCloudEnvironmentStatusPhase
PRIVATE_REGION_STATUS_PHASE_FAILED_TO_SYNC: HybridCloudEnvironmentStatusPhase
PRIVATE_REGION_STATUS_PHASE_UNKNOWN: HybridCloudEnvironmentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_READY: HybridCloudEnvironmentComponentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_NOT_READY: HybridCloudEnvironmentComponentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_NOT_FOUND: HybridCloudEnvironmentComponentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_UNKNOWN: HybridCloudEnvironmentComponentStatusPhase
KUBERNETES_DISTRIBUTION_UNKNOWN: KubernetesDistribution
KUBERNETES_DISTRIBUTION_AWS: KubernetesDistribution
KUBERNETES_DISTRIBUTION_GCP: KubernetesDistribution
KUBERNETES_DISTRIBUTION_AZURE: KubernetesDistribution
KUBERNETES_DISTRIBUTION_DO: KubernetesDistribution
KUBERNETES_DISTRIBUTION_SCALEWAY: KubernetesDistribution
KUBERNETES_DISTRIBUTION_OPENSHIFT: KubernetesDistribution
KUBERNETES_DISTRIBUTION_LINODE: KubernetesDistribution
KUBERNETES_DISTRIBUTION_CIVO: KubernetesDistribution
KUBERNETES_DISTRIBUTION_OCI: KubernetesDistribution
KUBERNETES_DISTRIBUTION_OVHCLOUD: KubernetesDistribution
KUBERNETES_DISTRIBUTION_STACKIT: KubernetesDistribution
KUBERNETES_DISTRIBUTION_VULTR: KubernetesDistribution
KUBERNETES_DISTRIBUTION_K3S: KubernetesDistribution

class GetInitialInstallationCommandRequest(_message.Message):
    __slots__ = ("hybrid_cloud_environment_id", "account_id")
    HYBRID_CLOUD_ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment_id: str
    account_id: str
    def __init__(self, hybrid_cloud_environment_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetInitialInstallationCommandResponse(_message.Message):
    __slots__ = ("command", "access_key", "registry_username", "registry_password", "account_id", "region_id")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_USERNAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    command: str
    access_key: str
    registry_username: str
    registry_password: str
    account_id: str
    region_id: str
    def __init__(self, command: _Optional[str] = ..., access_key: _Optional[str] = ..., registry_username: _Optional[str] = ..., registry_password: _Optional[str] = ..., account_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class DeleteCloudEnvironmentRequest(_message.Message):
    __slots__ = ("hybrid_cloud_environment_id", "account_id")
    HYBRID_CLOUD_ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment_id: str
    account_id: str
    def __init__(self, hybrid_cloud_environment_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class DeleteCloudEnvironmentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateCloudEnvironmentRequest(_message.Message):
    __slots__ = ("hybrid_cloud_environment",)
    HYBRID_CLOUD_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment: HybridCloudEnvironment
    def __init__(self, hybrid_cloud_environment: _Optional[_Union[HybridCloudEnvironment, _Mapping]] = ...) -> None: ...

class UpdateCloudEnvironmentResponse(_message.Message):
    __slots__ = ("hybrid_cloud_environment",)
    HYBRID_CLOUD_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment: HybridCloudEnvironment
    def __init__(self, hybrid_cloud_environment: _Optional[_Union[HybridCloudEnvironment, _Mapping]] = ...) -> None: ...

class CreateCloudEnvironmentRequest(_message.Message):
    __slots__ = ("hybrid_cloud_environment",)
    HYBRID_CLOUD_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment: HybridCloudEnvironment
    def __init__(self, hybrid_cloud_environment: _Optional[_Union[HybridCloudEnvironment, _Mapping]] = ...) -> None: ...

class CreateCloudEnvironmentResponse(_message.Message):
    __slots__ = ("hybrid_cloud_environment",)
    HYBRID_CLOUD_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment: HybridCloudEnvironment
    def __init__(self, hybrid_cloud_environment: _Optional[_Union[HybridCloudEnvironment, _Mapping]] = ...) -> None: ...

class GetCloudEnvironmentRequest(_message.Message):
    __slots__ = ("hybrid_cloud_environment_id", "account_id")
    HYBRID_CLOUD_ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment_id: str
    account_id: str
    def __init__(self, hybrid_cloud_environment_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetCloudEnvironmentResponse(_message.Message):
    __slots__ = ("hybrid_cloud_environment",)
    HYBRID_CLOUD_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment: HybridCloudEnvironment
    def __init__(self, hybrid_cloud_environment: _Optional[_Union[HybridCloudEnvironment, _Mapping]] = ...) -> None: ...

class ListCloudEnvironmentsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListCloudEnvironmentsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[HybridCloudEnvironment]
    def __init__(self, items: _Optional[_Iterable[_Union[HybridCloudEnvironment, _Mapping]]] = ...) -> None: ...

class HybridCloudEnvironment(_message.Message):
    __slots__ = ("id", "created_at", "modified_at", "account_id", "name", "programmatic_access_key_id", "created_by", "configuration", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRAMMATIC_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    account_id: str
    name: str
    programmatic_access_key_id: str
    created_by: str
    configuration: HybridCloudEnvironmentConfiguration
    status: HybridCloudEnvironmentStatus
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., name: _Optional[str] = ..., programmatic_access_key_id: _Optional[str] = ..., created_by: _Optional[str] = ..., configuration: _Optional[_Union[HybridCloudEnvironmentConfiguration, _Mapping]] = ..., status: _Optional[_Union[HybridCloudEnvironmentStatus, _Mapping]] = ...) -> None: ...

class HybridCloudEnvironmentConfiguration(_message.Message):
    __slots__ = ("created_at", "version", "operator_config", "namespace", "http_proxy_url", "https_proxy_url", "no_proxy_config", "container_registry_url", "chart_repository_url", "registry_secret_name", "ca_certificates", "qdrant_kubernetes_api_version", "agent_version", "operator_version", "prometheus_version", "kubernetes_event_exporter_version", "qdrant_node_exporter_version", "qdrant_cluster_exporter_version", "qdrant_cluster_manager_version", "created_by", "log_level", "tolerations", "node_selector")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    HTTP_PROXY_URL_FIELD_NUMBER: _ClassVar[int]
    HTTPS_PROXY_URL_FIELD_NUMBER: _ClassVar[int]
    NO_PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_REGISTRY_URL_FIELD_NUMBER: _ClassVar[int]
    CHART_REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    QDRANT_KUBERNETES_API_VERSION_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROMETHEUS_VERSION_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_EVENT_EXPORTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    QDRANT_NODE_EXPORTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    QDRANT_CLUSTER_EXPORTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    QDRANT_CLUSTER_MANAGER_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TOLERATIONS_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    version: int
    operator_config: OperatorConfiguration
    namespace: str
    http_proxy_url: str
    https_proxy_url: str
    no_proxy_config: _containers.RepeatedScalarFieldContainer[str]
    container_registry_url: str
    chart_repository_url: str
    registry_secret_name: str
    ca_certificates: str
    qdrant_kubernetes_api_version: str
    agent_version: str
    operator_version: str
    prometheus_version: str
    kubernetes_event_exporter_version: str
    qdrant_node_exporter_version: str
    qdrant_cluster_exporter_version: str
    qdrant_cluster_manager_version: str
    created_by: str
    log_level: str
    tolerations: _containers.RepeatedCompositeFieldContainer[_cluster_pb2.Toleration]
    node_selector: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ..., operator_config: _Optional[_Union[OperatorConfiguration, _Mapping]] = ..., namespace: _Optional[str] = ..., http_proxy_url: _Optional[str] = ..., https_proxy_url: _Optional[str] = ..., no_proxy_config: _Optional[_Iterable[str]] = ..., container_registry_url: _Optional[str] = ..., chart_repository_url: _Optional[str] = ..., registry_secret_name: _Optional[str] = ..., ca_certificates: _Optional[str] = ..., qdrant_kubernetes_api_version: _Optional[str] = ..., agent_version: _Optional[str] = ..., operator_version: _Optional[str] = ..., prometheus_version: _Optional[str] = ..., kubernetes_event_exporter_version: _Optional[str] = ..., qdrant_node_exporter_version: _Optional[str] = ..., qdrant_cluster_exporter_version: _Optional[str] = ..., qdrant_cluster_manager_version: _Optional[str] = ..., created_by: _Optional[str] = ..., log_level: _Optional[str] = ..., tolerations: _Optional[_Iterable[_Union[_cluster_pb2.Toleration, _Mapping]]] = ..., node_selector: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ("enable", "snapshots", "scheduledSnapshots", "restores")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEDSNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    RESTORES_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    snapshots: OperatorSnapshots
    scheduledSnapshots: OperatorScheduledSnapshots
    restores: OperatorRestores
    def __init__(self, enable: bool = ..., snapshots: _Optional[_Union[OperatorSnapshots, _Mapping]] = ..., scheduledSnapshots: _Optional[_Union[OperatorScheduledSnapshots, _Mapping]] = ..., restores: _Optional[_Union[OperatorRestores, _Mapping]] = ...) -> None: ...

class OperatorSnapshots(_message.Message):
    __slots__ = ("enable", "volumeSnapshotClass", "retainUnsuccessful", "max_concurrent_reconciles")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    VOLUMESNAPSHOTCLASS_FIELD_NUMBER: _ClassVar[int]
    RETAINUNSUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_RECONCILES_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    volumeSnapshotClass: str
    retainUnsuccessful: str
    max_concurrent_reconciles: int
    def __init__(self, enable: bool = ..., volumeSnapshotClass: _Optional[str] = ..., retainUnsuccessful: _Optional[str] = ..., max_concurrent_reconciles: _Optional[int] = ...) -> None: ...

class OperatorScheduledSnapshots(_message.Message):
    __slots__ = ("enable", "remove_cron_jobs", "max_concurrent_reconciles")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_CRON_JOBS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_RECONCILES_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    remove_cron_jobs: bool
    max_concurrent_reconciles: int
    def __init__(self, enable: bool = ..., remove_cron_jobs: bool = ..., max_concurrent_reconciles: _Optional[int] = ...) -> None: ...

class OperatorRestores(_message.Message):
    __slots__ = ("enable", "max_concurrent_reconciles")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_RECONCILES_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    max_concurrent_reconciles: int
    def __init__(self, enable: bool = ..., max_concurrent_reconciles: _Optional[int] = ...) -> None: ...

class OperatorClusterManagement(_message.Message):
    __slots__ = ("enable", "storage_Class", "qdrant", "scheduling", "cluster_manager", "ingress", "telemetry_timeout", "max_concurrent_reconciles", "volume_expansion_mode")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    QDRANT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_MANAGER_FIELD_NUMBER: _ClassVar[int]
    INGRESS_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_RECONCILES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_EXPANSION_MODE_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    storage_Class: OperatorStorageClass
    qdrant: OperatorQdrant
    scheduling: OperatorScheduling
    cluster_manager: OperatorClusterManager
    ingress: OperatorIngress
    telemetry_timeout: str
    max_concurrent_reconciles: int
    volume_expansion_mode: str
    def __init__(self, enable: bool = ..., storage_Class: _Optional[_Union[OperatorStorageClass, _Mapping]] = ..., qdrant: _Optional[_Union[OperatorQdrant, _Mapping]] = ..., scheduling: _Optional[_Union[OperatorScheduling, _Mapping]] = ..., cluster_manager: _Optional[_Union[OperatorClusterManager, _Mapping]] = ..., ingress: _Optional[_Union[OperatorIngress, _Mapping]] = ..., telemetry_timeout: _Optional[str] = ..., max_concurrent_reconciles: _Optional[int] = ..., volume_expansion_mode: _Optional[str] = ...) -> None: ...

class OperatorScheduling(_message.Message):
    __slots__ = ("topology_spread_constraints", "pod_disruption_budget")
    TOPOLOGY_SPREAD_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    POD_DISRUPTION_BUDGET_FIELD_NUMBER: _ClassVar[int]
    topology_spread_constraints: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    pod_disruption_budget: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    def __init__(self, topology_spread_constraints: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ..., pod_disruption_budget: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ("enable", "provider", "kubernetesIngress")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    KUBERNETESINGRESS_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    provider: str
    kubernetesIngress: OperatorKubernetesIngress
    def __init__(self, enable: bool = ..., provider: _Optional[str] = ..., kubernetesIngress: _Optional[_Union[OperatorKubernetesIngress, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("enable", "database", "snapshot")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    database: str
    snapshot: str
    def __init__(self, enable: bool = ..., database: _Optional[str] = ..., snapshot: _Optional[str] = ...) -> None: ...

class OperatorQdrant(_message.Message):
    __slots__ = ("image", "storage", "log_level", "security_context", "network_policies")
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POLICIES_FIELD_NUMBER: _ClassVar[int]
    image: OperatorQdrantImage
    storage: OperatorQdrantStorage
    log_level: str
    security_context: OperatorSecurityContext
    network_policies: OperatorV2NetworkPolicy
    def __init__(self, image: _Optional[_Union[OperatorQdrantImage, _Mapping]] = ..., storage: _Optional[_Union[OperatorQdrantStorage, _Mapping]] = ..., log_level: _Optional[str] = ..., security_context: _Optional[_Union[OperatorSecurityContext, _Mapping]] = ..., network_policies: _Optional[_Union[OperatorV2NetworkPolicy, _Mapping]] = ...) -> None: ...

class OperatorV2NetworkPolicy(_message.Message):
    __slots__ = ("ingress", "egress")
    INGRESS_FIELD_NUMBER: _ClassVar[int]
    EGRESS_FIELD_NUMBER: _ClassVar[int]
    ingress: _containers.RepeatedCompositeFieldContainer[NetworkPolicyIngress]
    egress: _containers.RepeatedCompositeFieldContainer[NetworkPolicyEgress]
    def __init__(self, ingress: _Optional[_Iterable[_Union[NetworkPolicyIngress, _Mapping]]] = ..., egress: _Optional[_Iterable[_Union[NetworkPolicyEgress, _Mapping]]] = ...) -> None: ...

class NetworkPolicyEgress(_message.Message):
    __slots__ = ("to", "ports")
    TO_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    to: _containers.RepeatedCompositeFieldContainer[NetworkPolicyItem]
    ports: _containers.RepeatedCompositeFieldContainer[NetworkPolicyPort]
    def __init__(self, to: _Optional[_Iterable[_Union[NetworkPolicyItem, _Mapping]]] = ..., ports: _Optional[_Iterable[_Union[NetworkPolicyPort, _Mapping]]] = ...) -> None: ...

class NetworkPolicyIngress(_message.Message):
    __slots__ = ("ports",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    ports: _containers.RepeatedCompositeFieldContainer[NetworkPolicyPort]
    def __init__(self, ports: _Optional[_Iterable[_Union[NetworkPolicyPort, _Mapping]]] = ..., **kwargs) -> None: ...

class NetworkPolicyItem(_message.Message):
    __slots__ = ("namespace_selector", "pod_selector")
    NAMESPACE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    POD_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    namespace_selector: NetworkPolicyItemSelector
    pod_selector: NetworkPolicyItemSelector
    def __init__(self, namespace_selector: _Optional[_Union[NetworkPolicyItemSelector, _Mapping]] = ..., pod_selector: _Optional[_Union[NetworkPolicyItemSelector, _Mapping]] = ...) -> None: ...

class NetworkPolicyItemSelector(_message.Message):
    __slots__ = ("match_labels",)
    MATCH_LABELS_FIELD_NUMBER: _ClassVar[int]
    match_labels: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    def __init__(self, match_labels: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class NetworkPolicyPort(_message.Message):
    __slots__ = ("protocol", "port")
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    protocol: str
    port: int
    def __init__(self, protocol: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class OperatorSecurityContext(_message.Message):
    __slots__ = ("user", "fs_group", "group")
    USER_FIELD_NUMBER: _ClassVar[int]
    FS_GROUP_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    user: str
    fs_group: str
    group: str
    def __init__(self, user: _Optional[str] = ..., fs_group: _Optional[str] = ..., group: _Optional[str] = ...) -> None: ...

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

class HybridCloudEnvironmentStatus(_message.Message):
    __slots__ = ("modified_at", "schema_version", "phase", "k8s_version", "number_of_nodes", "capabilities", "helm_repositories", "helm_releases", "ready_for_cluster_creation", "k8s_distribution", "message", "storage_classes", "volume_snapshot_classes", "node_infos")
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    K8S_VERSION_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_NODES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    HELM_REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    HELM_RELEASES_FIELD_NUMBER: _ClassVar[int]
    READY_FOR_CLUSTER_CREATION_FIELD_NUMBER: _ClassVar[int]
    K8S_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASSES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    NODE_INFOS_FIELD_NUMBER: _ClassVar[int]
    modified_at: _timestamp_pb2.Timestamp
    schema_version: str
    phase: HybridCloudEnvironmentStatusPhase
    k8s_version: str
    number_of_nodes: int
    capabilities: HybridCloudEnvironmentCapabilities
    helm_repositories: _containers.RepeatedCompositeFieldContainer[HybridCloudEnvironmentComponentStatus]
    helm_releases: _containers.RepeatedCompositeFieldContainer[HybridCloudEnvironmentComponentStatus]
    ready_for_cluster_creation: bool
    k8s_distribution: KubernetesDistribution
    message: str
    storage_classes: _containers.RepeatedCompositeFieldContainer[HybridCloudEnvironmentStorageClass]
    volume_snapshot_classes: _containers.RepeatedCompositeFieldContainer[HybridCloudEnvironmentVolumeSnapshotClass]
    node_infos: _containers.RepeatedCompositeFieldContainer[HybridCloudEnvironmentNodeInfo]
    def __init__(self, modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., schema_version: _Optional[str] = ..., phase: _Optional[_Union[HybridCloudEnvironmentStatusPhase, str]] = ..., k8s_version: _Optional[str] = ..., number_of_nodes: _Optional[int] = ..., capabilities: _Optional[_Union[HybridCloudEnvironmentCapabilities, _Mapping]] = ..., helm_repositories: _Optional[_Iterable[_Union[HybridCloudEnvironmentComponentStatus, _Mapping]]] = ..., helm_releases: _Optional[_Iterable[_Union[HybridCloudEnvironmentComponentStatus, _Mapping]]] = ..., ready_for_cluster_creation: bool = ..., k8s_distribution: _Optional[_Union[KubernetesDistribution, str]] = ..., message: _Optional[str] = ..., storage_classes: _Optional[_Iterable[_Union[HybridCloudEnvironmentStorageClass, _Mapping]]] = ..., volume_snapshot_classes: _Optional[_Iterable[_Union[HybridCloudEnvironmentVolumeSnapshotClass, _Mapping]]] = ..., node_infos: _Optional[_Iterable[_Union[HybridCloudEnvironmentNodeInfo, _Mapping]]] = ...) -> None: ...

class HybridCloudEnvironmentCapabilities(_message.Message):
    __slots__ = ("volume_snapshot", "volume_expansion")
    VOLUME_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_EXPANSION_FIELD_NUMBER: _ClassVar[int]
    volume_snapshot: bool
    volume_expansion: bool
    def __init__(self, volume_snapshot: bool = ..., volume_expansion: bool = ...) -> None: ...

class HybridCloudEnvironmentComponentStatus(_message.Message):
    __slots__ = ("name", "namespace", "version", "phase", "message")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    version: str
    phase: HybridCloudEnvironmentComponentStatusPhase
    message: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., version: _Optional[str] = ..., phase: _Optional[_Union[HybridCloudEnvironmentComponentStatusPhase, str]] = ..., message: _Optional[str] = ...) -> None: ...

class HybridCloudEnvironmentStorageClass(_message.Message):
    __slots__ = ("name", "default", "provisioner", "allow_volume_expansion", "reclaim_policy", "parameters")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    PROVISIONER_FIELD_NUMBER: _ClassVar[int]
    ALLOW_VOLUME_EXPANSION_FIELD_NUMBER: _ClassVar[int]
    RECLAIM_POLICY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    default: bool
    provisioner: str
    allow_volume_expansion: bool
    reclaim_policy: str
    parameters: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    def __init__(self, name: _Optional[str] = ..., default: bool = ..., provisioner: _Optional[str] = ..., allow_volume_expansion: bool = ..., reclaim_policy: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class HybridCloudEnvironmentVolumeSnapshotClass(_message.Message):
    __slots__ = ("name", "driver")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    name: str
    driver: str
    def __init__(self, name: _Optional[str] = ..., driver: _Optional[str] = ...) -> None: ...

class HybridCloudEnvironmentNodeInfo(_message.Message):
    __slots__ = ("name", "region", "zone", "instance_type", "arch", "capacity", "allocatable")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCH_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ALLOCATABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    region: str
    zone: str
    instance_type: str
    arch: str
    capacity: HybridCloudEnvironmentNodeResourceInfo
    allocatable: HybridCloudEnvironmentNodeResourceInfo
    def __init__(self, name: _Optional[str] = ..., region: _Optional[str] = ..., zone: _Optional[str] = ..., instance_type: _Optional[str] = ..., arch: _Optional[str] = ..., capacity: _Optional[_Union[HybridCloudEnvironmentNodeResourceInfo, _Mapping]] = ..., allocatable: _Optional[_Union[HybridCloudEnvironmentNodeResourceInfo, _Mapping]] = ...) -> None: ...

class HybridCloudEnvironmentNodeResourceInfo(_message.Message):
    __slots__ = ("cpu", "memory", "pods", "ephemeral_storage")
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    PODS_FIELD_NUMBER: _ClassVar[int]
    EPHEMERAL_STORAGE_FIELD_NUMBER: _ClassVar[int]
    cpu: str
    memory: str
    pods: str
    ephemeral_storage: str
    def __init__(self, cpu: _Optional[str] = ..., memory: _Optional[str] = ..., pods: _Optional[str] = ..., ephemeral_storage: _Optional[str] = ...) -> None: ...
