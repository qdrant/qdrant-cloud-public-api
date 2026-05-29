from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.hybrid.v1 import hybrid_cloud_pb2 as _hybrid_cloud_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterCreationBlockingReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_CREATION_BLOCKING_REASON_UNSPECIFIED: _ClassVar[ClusterCreationBlockingReason]
    CLUSTER_CREATION_BLOCKING_REASON_NONE: _ClassVar[ClusterCreationBlockingReason]
    CLUSTER_CREATION_BLOCKING_REASON_ENVIRONMENT_NOT_READY: _ClassVar[ClusterCreationBlockingReason]
    CLUSTER_CREATION_BLOCKING_REASON_STORAGE_CONFIGURATION_NOT_READY: _ClassVar[ClusterCreationBlockingReason]

class PlatformMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLATFORM_MODE_UNSPECIFIED: _ClassVar[PlatformMode]
    PLATFORM_MODE_DEDICATED_CLUSTERS: _ClassVar[PlatformMode]
    PLATFORM_MODE_SERVERLESS_SPACES: _ClassVar[PlatformMode]
CLUSTER_CREATION_BLOCKING_REASON_UNSPECIFIED: ClusterCreationBlockingReason
CLUSTER_CREATION_BLOCKING_REASON_NONE: ClusterCreationBlockingReason
CLUSTER_CREATION_BLOCKING_REASON_ENVIRONMENT_NOT_READY: ClusterCreationBlockingReason
CLUSTER_CREATION_BLOCKING_REASON_STORAGE_CONFIGURATION_NOT_READY: ClusterCreationBlockingReason
PLATFORM_MODE_UNSPECIFIED: PlatformMode
PLATFORM_MODE_DEDICATED_CLUSTERS: PlatformMode
PLATFORM_MODE_SERVERLESS_SPACES: PlatformMode

class ListCloudProvidersRequest(_message.Message):
    __slots__ = ("account_id", "supported_mode")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_MODE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    supported_mode: PlatformMode
    def __init__(self, account_id: _Optional[str] = ..., supported_mode: _Optional[_Union[PlatformMode, str]] = ...) -> None: ...

class ListCloudProvidersResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CloudProvider]
    def __init__(self, items: _Optional[_Iterable[_Union[CloudProvider, _Mapping]]] = ...) -> None: ...

class ListGlobalCloudProvidersRequest(_message.Message):
    __slots__ = ("supported_mode",)
    SUPPORTED_MODE_FIELD_NUMBER: _ClassVar[int]
    supported_mode: PlatformMode
    def __init__(self, supported_mode: _Optional[_Union[PlatformMode, str]] = ...) -> None: ...

class ListGlobalCloudProvidersResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CloudProvider]
    def __init__(self, items: _Optional[_Iterable[_Union[CloudProvider, _Mapping]]] = ...) -> None: ...

class ListGlobalCloudProviderRegionsRequest(_message.Message):
    __slots__ = ("cloud_provider_id", "supported_mode")
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_MODE_FIELD_NUMBER: _ClassVar[int]
    cloud_provider_id: str
    supported_mode: PlatformMode
    def __init__(self, cloud_provider_id: _Optional[str] = ..., supported_mode: _Optional[_Union[PlatformMode, str]] = ...) -> None: ...

class ListGlobalCloudProviderRegionsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CloudProviderRegion]
    def __init__(self, items: _Optional[_Iterable[_Union[CloudProviderRegion, _Mapping]]] = ...) -> None: ...

class GetGlobalCloudProviderRegionRequest(_message.Message):
    __slots__ = ("cloud_provider_id", "region_id")
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    cloud_provider_id: str
    region_id: str
    def __init__(self, cloud_provider_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class GetGlobalCloudProviderRegionResponse(_message.Message):
    __slots__ = ("region",)
    REGION_FIELD_NUMBER: _ClassVar[int]
    region: CloudProviderRegion
    def __init__(self, region: _Optional[_Union[CloudProviderRegion, _Mapping]] = ...) -> None: ...

class ListCloudProviderRegionsRequest(_message.Message):
    __slots__ = ("account_id", "cloud_provider_id", "supported_mode")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_MODE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cloud_provider_id: str
    supported_mode: PlatformMode
    def __init__(self, account_id: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ..., supported_mode: _Optional[_Union[PlatformMode, str]] = ...) -> None: ...

class ListCloudProviderRegionsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CloudProviderRegion]
    def __init__(self, items: _Optional[_Iterable[_Union[CloudProviderRegion, _Mapping]]] = ...) -> None: ...

class GetCloudProviderRegionRequest(_message.Message):
    __slots__ = ("account_id", "cloud_provider_id", "region_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cloud_provider_id: str
    region_id: str
    def __init__(self, account_id: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class GetCloudProviderRegionResponse(_message.Message):
    __slots__ = ("region",)
    REGION_FIELD_NUMBER: _ClassVar[int]
    region: CloudProviderRegion
    def __init__(self, region: _Optional[_Union[CloudProviderRegion, _Mapping]] = ...) -> None: ...

class CloudProvider(_message.Message):
    __slots__ = ("id", "name", "free_tier", "available", "supported_modes")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FREE_TIER_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_MODES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    free_tier: bool
    available: bool
    supported_modes: _containers.RepeatedScalarFieldContainer[PlatformMode]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., free_tier: _Optional[bool] = ..., available: _Optional[bool] = ..., supported_modes: _Optional[_Iterable[_Union[PlatformMode, str]]] = ...) -> None: ...

class CloudProviderRegion(_message.Message):
    __slots__ = ("id", "name", "free_tier", "available", "provider", "country_iso_code", "geographical_sub_region", "namespace", "capabilities", "cluster_creation_blocking_reason", "storage_classes", "volume_snapshot_classes", "supported_modes")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FREE_TIER_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ISO_CODE_FIELD_NUMBER: _ClassVar[int]
    GEOGRAPHICAL_SUB_REGION_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CREATION_BLOCKING_REASON_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASSES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_MODES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    free_tier: bool
    available: bool
    provider: str
    country_iso_code: str
    geographical_sub_region: str
    namespace: str
    capabilities: CloudProviderRegionCapabilities
    cluster_creation_blocking_reason: ClusterCreationBlockingReason
    storage_classes: _containers.RepeatedCompositeFieldContainer[_hybrid_cloud_pb2.HybridCloudEnvironmentStorageClass]
    volume_snapshot_classes: _containers.RepeatedCompositeFieldContainer[_hybrid_cloud_pb2.HybridCloudEnvironmentVolumeSnapshotClass]
    supported_modes: _containers.RepeatedScalarFieldContainer[PlatformMode]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., free_tier: _Optional[bool] = ..., available: _Optional[bool] = ..., provider: _Optional[str] = ..., country_iso_code: _Optional[str] = ..., geographical_sub_region: _Optional[str] = ..., namespace: _Optional[str] = ..., capabilities: _Optional[_Union[CloudProviderRegionCapabilities, _Mapping]] = ..., cluster_creation_blocking_reason: _Optional[_Union[ClusterCreationBlockingReason, str]] = ..., storage_classes: _Optional[_Iterable[_Union[_hybrid_cloud_pb2.HybridCloudEnvironmentStorageClass, _Mapping]]] = ..., volume_snapshot_classes: _Optional[_Iterable[_Union[_hybrid_cloud_pb2.HybridCloudEnvironmentVolumeSnapshotClass, _Mapping]]] = ..., supported_modes: _Optional[_Iterable[_Union[PlatformMode, str]]] = ...) -> None: ...

class CloudProviderRegionCapabilities(_message.Message):
    __slots__ = ("volume_snapshot", "volume_expansion")
    VOLUME_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_EXPANSION_FIELD_NUMBER: _ClassVar[int]
    volume_snapshot: bool
    volume_expansion: bool
    def __init__(self, volume_snapshot: _Optional[bool] = ..., volume_expansion: _Optional[bool] = ...) -> None: ...
