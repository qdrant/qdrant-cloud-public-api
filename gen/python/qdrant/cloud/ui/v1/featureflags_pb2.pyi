from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetFeatureFlagsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetFeatureFlagsResponse(_message.Message):
    __slots__ = ()
    CLUSTER_CREATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CREATION_PAGE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BILLING_CYCLES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_CANCEL_FLOW_ENABLED_FIELD_NUMBER: _ClassVar[int]
    QDRANT_CLUSTERS_QUERYING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STORAGE_TIER_CONFIGURATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    cluster_creation_enabled: bool
    cluster_creation_page_enabled: bool
    billing_cycles_enabled: bool
    entitlement_cancel_flow_enabled: bool
    qdrant_clusters_querying_enabled: bool
    cluster_storage_tier_configuration_enabled: bool
    def __init__(self, cluster_creation_enabled: _Optional[bool] = ..., cluster_creation_page_enabled: _Optional[bool] = ..., billing_cycles_enabled: _Optional[bool] = ..., entitlement_cancel_flow_enabled: _Optional[bool] = ..., qdrant_clusters_querying_enabled: _Optional[bool] = ..., cluster_storage_tier_configuration_enabled: _Optional[bool] = ...) -> None: ...
