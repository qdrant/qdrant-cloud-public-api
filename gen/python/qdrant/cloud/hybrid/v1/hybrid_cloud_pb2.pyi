from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.cluster.v1 import cluster_pb2 as _cluster_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.hybrid.v1 import operator_pb2 as _operator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HybridCloudEnvironmentStatusPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HYBRID_CLOUD_ENVIRONMENT_STATUS_PHASE_UNSPECIFIED: _ClassVar[HybridCloudEnvironmentStatusPhase]
    HYBRID_CLOUD_ENVIRONMENT_STATUS_PHASE_READY: _ClassVar[HybridCloudEnvironmentStatusPhase]
    HYBRID_CLOUD_ENVIRONMENT_STATUS_PHASE_NOT_READY: _ClassVar[HybridCloudEnvironmentStatusPhase]
    HYBRID_CLOUD_ENVIRONMENT_STATUS_PHASE_FAILED_TO_SYNC: _ClassVar[HybridCloudEnvironmentStatusPhase]

class HybridCloudEnvironmentComponentStatusPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_UNSPECIFIED: _ClassVar[HybridCloudEnvironmentComponentStatusPhase]
    HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_READY: _ClassVar[HybridCloudEnvironmentComponentStatusPhase]
    HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_NOT_READY: _ClassVar[HybridCloudEnvironmentComponentStatusPhase]
    HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_NOT_FOUND: _ClassVar[HybridCloudEnvironmentComponentStatusPhase]

class KubernetesDistribution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KUBERNETES_DISTRIBUTION_UNSPECIFIED: _ClassVar[KubernetesDistribution]
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
HYBRID_CLOUD_ENVIRONMENT_STATUS_PHASE_UNSPECIFIED: HybridCloudEnvironmentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_STATUS_PHASE_READY: HybridCloudEnvironmentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_STATUS_PHASE_NOT_READY: HybridCloudEnvironmentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_STATUS_PHASE_FAILED_TO_SYNC: HybridCloudEnvironmentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_UNSPECIFIED: HybridCloudEnvironmentComponentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_READY: HybridCloudEnvironmentComponentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_NOT_READY: HybridCloudEnvironmentComponentStatusPhase
HYBRID_CLOUD_ENVIRONMENT_COMPONENT_STATUS_PHASE_NOT_FOUND: HybridCloudEnvironmentComponentStatusPhase
KUBERNETES_DISTRIBUTION_UNSPECIFIED: KubernetesDistribution
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
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: str
    def __init__(self, command: _Optional[str] = ...) -> None: ...

class DeleteHybridCloudEnvironmentRequest(_message.Message):
    __slots__ = ("hybrid_cloud_environment_id", "account_id")
    HYBRID_CLOUD_ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment_id: str
    account_id: str
    def __init__(self, hybrid_cloud_environment_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class DeleteHybridCloudEnvironmentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateHybridCloudEnvironmentRequest(_message.Message):
    __slots__ = ("hybrid_cloud_environment",)
    HYBRID_CLOUD_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment: HybridCloudEnvironment
    def __init__(self, hybrid_cloud_environment: _Optional[_Union[HybridCloudEnvironment, _Mapping]] = ...) -> None: ...

class UpdateHybridCloudEnvironmentResponse(_message.Message):
    __slots__ = ("hybrid_cloud_environment",)
    HYBRID_CLOUD_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment: HybridCloudEnvironment
    def __init__(self, hybrid_cloud_environment: _Optional[_Union[HybridCloudEnvironment, _Mapping]] = ...) -> None: ...

class CreateHybridCloudEnvironmentRequest(_message.Message):
    __slots__ = ("hybrid_cloud_environment",)
    HYBRID_CLOUD_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment: HybridCloudEnvironment
    def __init__(self, hybrid_cloud_environment: _Optional[_Union[HybridCloudEnvironment, _Mapping]] = ...) -> None: ...

class CreateHybridCloudEnvironmentResponse(_message.Message):
    __slots__ = ("hybrid_cloud_environment",)
    HYBRID_CLOUD_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment: HybridCloudEnvironment
    def __init__(self, hybrid_cloud_environment: _Optional[_Union[HybridCloudEnvironment, _Mapping]] = ...) -> None: ...

class GetHybridCloudEnvironmentRequest(_message.Message):
    __slots__ = ("hybrid_cloud_environment_id", "account_id")
    HYBRID_CLOUD_ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment_id: str
    account_id: str
    def __init__(self, hybrid_cloud_environment_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetHybridCloudEnvironmentResponse(_message.Message):
    __slots__ = ("hybrid_cloud_environment",)
    HYBRID_CLOUD_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    hybrid_cloud_environment: HybridCloudEnvironment
    def __init__(self, hybrid_cloud_environment: _Optional[_Union[HybridCloudEnvironment, _Mapping]] = ...) -> None: ...

class ListHybridCloudEnvironmentsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListHybridCloudEnvironmentsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[HybridCloudEnvironment]
    def __init__(self, items: _Optional[_Iterable[_Union[HybridCloudEnvironment, _Mapping]]] = ...) -> None: ...

class HybridCloudEnvironment(_message.Message):
    __slots__ = ("id", "created_at", "modified_at", "account_id", "name", "created_by", "configuration", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    account_id: str
    name: str
    created_by: str
    configuration: HybridCloudEnvironmentConfiguration
    status: HybridCloudEnvironmentStatus
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., name: _Optional[str] = ..., created_by: _Optional[str] = ..., configuration: _Optional[_Union[HybridCloudEnvironmentConfiguration, _Mapping]] = ..., status: _Optional[_Union[HybridCloudEnvironmentStatus, _Mapping]] = ...) -> None: ...

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
    operator_config: _operator_pb2.OperatorConfiguration
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
    def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ..., operator_config: _Optional[_Union[_operator_pb2.OperatorConfiguration, _Mapping]] = ..., namespace: _Optional[str] = ..., http_proxy_url: _Optional[str] = ..., https_proxy_url: _Optional[str] = ..., no_proxy_config: _Optional[_Iterable[str]] = ..., container_registry_url: _Optional[str] = ..., chart_repository_url: _Optional[str] = ..., registry_secret_name: _Optional[str] = ..., ca_certificates: _Optional[str] = ..., qdrant_kubernetes_api_version: _Optional[str] = ..., agent_version: _Optional[str] = ..., operator_version: _Optional[str] = ..., prometheus_version: _Optional[str] = ..., kubernetes_event_exporter_version: _Optional[str] = ..., qdrant_node_exporter_version: _Optional[str] = ..., qdrant_cluster_exporter_version: _Optional[str] = ..., qdrant_cluster_manager_version: _Optional[str] = ..., created_by: _Optional[str] = ..., log_level: _Optional[str] = ..., tolerations: _Optional[_Iterable[_Union[_cluster_pb2.Toleration, _Mapping]]] = ..., node_selector: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

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
