import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from k8s.io.api.networking.v1 import generated_pb2 as _generated_pb2
from qdrant.cloud.cluster.v1 import cluster_pb2 as _cluster_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HybridCloudEnvironmentConfigurationLogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HYBRID_CLOUD_ENVIRONMENT_CONFIGURATION_LOG_LEVEL_UNSPECIFIED: _ClassVar[HybridCloudEnvironmentConfigurationLogLevel]
    HYBRID_CLOUD_ENVIRONMENT_CONFIGURATION_LOG_LEVEL_DEBUG: _ClassVar[HybridCloudEnvironmentConfigurationLogLevel]
    HYBRID_CLOUD_ENVIRONMENT_CONFIGURATION_LOG_LEVEL_INFO: _ClassVar[HybridCloudEnvironmentConfigurationLogLevel]
    HYBRID_CLOUD_ENVIRONMENT_CONFIGURATION_LOG_LEVEL_WARN: _ClassVar[HybridCloudEnvironmentConfigurationLogLevel]
    HYBRID_CLOUD_ENVIRONMENT_CONFIGURATION_LOG_LEVEL_ERROR: _ClassVar[HybridCloudEnvironmentConfigurationLogLevel]

class QdrantClusterCreationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QDRANT_CLUSTER_CREATION_STATUS_UNSPECIFIED: _ClassVar[QdrantClusterCreationStatus]
    QDRANT_CLUSTER_CREATION_STATUS_READY: _ClassVar[QdrantClusterCreationStatus]
    QDRANT_CLUSTER_CREATION_STATUS_NOT_READY: _ClassVar[QdrantClusterCreationStatus]

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
HYBRID_CLOUD_ENVIRONMENT_CONFIGURATION_LOG_LEVEL_UNSPECIFIED: HybridCloudEnvironmentConfigurationLogLevel
HYBRID_CLOUD_ENVIRONMENT_CONFIGURATION_LOG_LEVEL_DEBUG: HybridCloudEnvironmentConfigurationLogLevel
HYBRID_CLOUD_ENVIRONMENT_CONFIGURATION_LOG_LEVEL_INFO: HybridCloudEnvironmentConfigurationLogLevel
HYBRID_CLOUD_ENVIRONMENT_CONFIGURATION_LOG_LEVEL_WARN: HybridCloudEnvironmentConfigurationLogLevel
HYBRID_CLOUD_ENVIRONMENT_CONFIGURATION_LOG_LEVEL_ERROR: HybridCloudEnvironmentConfigurationLogLevel
QDRANT_CLUSTER_CREATION_STATUS_UNSPECIFIED: QdrantClusterCreationStatus
QDRANT_CLUSTER_CREATION_STATUS_READY: QdrantClusterCreationStatus
QDRANT_CLUSTER_CREATION_STATUS_NOT_READY: QdrantClusterCreationStatus
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

class GetBootstrapCommandsRequest(_message.Message):
    __slots__ = ("account_id", "hybrid_cloud_environment_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HYBRID_CLOUD_ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    hybrid_cloud_environment_id: str
    def __init__(self, account_id: _Optional[str] = ..., hybrid_cloud_environment_id: _Optional[str] = ...) -> None: ...

class GetBootstrapCommandsResponse(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, commands: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteHybridCloudEnvironmentRequest(_message.Message):
    __slots__ = ("account_id", "hybrid_cloud_environment_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HYBRID_CLOUD_ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    hybrid_cloud_environment_id: str
    def __init__(self, account_id: _Optional[str] = ..., hybrid_cloud_environment_id: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("account_id", "hybrid_cloud_environment_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HYBRID_CLOUD_ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    hybrid_cloud_environment_id: str
    def __init__(self, account_id: _Optional[str] = ..., hybrid_cloud_environment_id: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("account_id", "id", "created_at", "last_modified_at", "name", "configuration", "status")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    id: str
    created_at: _timestamp_pb2.Timestamp
    last_modified_at: _timestamp_pb2.Timestamp
    name: str
    configuration: HybridCloudEnvironmentConfiguration
    status: HybridCloudEnvironmentStatus
    def __init__(self, account_id: _Optional[str] = ..., id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., configuration: _Optional[_Union[HybridCloudEnvironmentConfiguration, _Mapping]] = ..., status: _Optional[_Union[HybridCloudEnvironmentStatus, _Mapping]] = ...) -> None: ...

class HybridCloudEnvironmentConfiguration(_message.Message):
    __slots__ = ("last_modified_at", "namespace", "http_proxy_url", "https_proxy_url", "no_proxy_configs", "container_registry_url", "chart_repository_url", "registry_secret_name", "ca_certificates", "database_storage_class", "snapshot_storage_class", "volume_snapshot_storage_class", "ingress", "egress", "log_level", "tolerations", "node_selector")
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    HTTP_PROXY_URL_FIELD_NUMBER: _ClassVar[int]
    HTTPS_PROXY_URL_FIELD_NUMBER: _ClassVar[int]
    NO_PROXY_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_REGISTRY_URL_FIELD_NUMBER: _ClassVar[int]
    CHART_REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    DATABASE_STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    INGRESS_FIELD_NUMBER: _ClassVar[int]
    EGRESS_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TOLERATIONS_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    last_modified_at: _timestamp_pb2.Timestamp
    namespace: str
    http_proxy_url: str
    https_proxy_url: str
    no_proxy_configs: _containers.RepeatedScalarFieldContainer[str]
    container_registry_url: str
    chart_repository_url: str
    registry_secret_name: str
    ca_certificates: str
    database_storage_class: str
    snapshot_storage_class: str
    volume_snapshot_storage_class: str
    ingress: _containers.RepeatedCompositeFieldContainer[_generated_pb2.NetworkPolicyIngressRule]
    egress: _containers.RepeatedCompositeFieldContainer[_generated_pb2.NetworkPolicyEgressRule]
    log_level: HybridCloudEnvironmentConfigurationLogLevel
    tolerations: _containers.RepeatedCompositeFieldContainer[_cluster_pb2.Toleration]
    node_selector: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValue]
    def __init__(self, last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., namespace: _Optional[str] = ..., http_proxy_url: _Optional[str] = ..., https_proxy_url: _Optional[str] = ..., no_proxy_configs: _Optional[_Iterable[str]] = ..., container_registry_url: _Optional[str] = ..., chart_repository_url: _Optional[str] = ..., registry_secret_name: _Optional[str] = ..., ca_certificates: _Optional[str] = ..., database_storage_class: _Optional[str] = ..., snapshot_storage_class: _Optional[str] = ..., volume_snapshot_storage_class: _Optional[str] = ..., ingress: _Optional[_Iterable[_Union[_generated_pb2.NetworkPolicyIngressRule, _Mapping]]] = ..., egress: _Optional[_Iterable[_Union[_generated_pb2.NetworkPolicyEgressRule, _Mapping]]] = ..., log_level: _Optional[_Union[HybridCloudEnvironmentConfigurationLogLevel, str]] = ..., tolerations: _Optional[_Iterable[_Union[_cluster_pb2.Toleration, _Mapping]]] = ..., node_selector: _Optional[_Iterable[_Union[_common_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class HybridCloudEnvironmentStatus(_message.Message):
    __slots__ = ("last_modified_at", "phase", "kubernetes_version", "kubernetes_distribution", "number_of_nodes", "capabilities", "component_statuses", "cluster_creation_readiness", "message", "storage_classes", "volume_snapshot_classes")
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_VERSION_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_NODES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_STATUSES_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CREATION_READINESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASSES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    last_modified_at: _timestamp_pb2.Timestamp
    phase: HybridCloudEnvironmentStatusPhase
    kubernetes_version: str
    kubernetes_distribution: KubernetesDistribution
    number_of_nodes: int
    capabilities: HybridCloudEnvironmentCapabilities
    component_statuses: _containers.RepeatedCompositeFieldContainer[HybridCloudEnvironmentComponentStatus]
    cluster_creation_readiness: QdrantClusterCreationStatus
    message: str
    storage_classes: _containers.RepeatedCompositeFieldContainer[HybridCloudEnvironmentStorageClass]
    volume_snapshot_classes: _containers.RepeatedCompositeFieldContainer[HybridCloudEnvironmentVolumeSnapshotClass]
    def __init__(self, last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., phase: _Optional[_Union[HybridCloudEnvironmentStatusPhase, str]] = ..., kubernetes_version: _Optional[str] = ..., kubernetes_distribution: _Optional[_Union[KubernetesDistribution, str]] = ..., number_of_nodes: _Optional[int] = ..., capabilities: _Optional[_Union[HybridCloudEnvironmentCapabilities, _Mapping]] = ..., component_statuses: _Optional[_Iterable[_Union[HybridCloudEnvironmentComponentStatus, _Mapping]]] = ..., cluster_creation_readiness: _Optional[_Union[QdrantClusterCreationStatus, str]] = ..., message: _Optional[str] = ..., storage_classes: _Optional[_Iterable[_Union[HybridCloudEnvironmentStorageClass, _Mapping]]] = ..., volume_snapshot_classes: _Optional[_Iterable[_Union[HybridCloudEnvironmentVolumeSnapshotClass, _Mapping]]] = ...) -> None: ...

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
