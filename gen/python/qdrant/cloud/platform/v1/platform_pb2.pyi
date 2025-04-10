from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCloudProvidersRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListCloudProvidersResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CloudProvider]
    def __init__(self, items: _Optional[_Iterable[_Union[CloudProvider, _Mapping]]] = ...) -> None: ...

class ListGlobalCloudProvidersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGlobalCloudProvidersResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CloudProvider]
    def __init__(self, items: _Optional[_Iterable[_Union[CloudProvider, _Mapping]]] = ...) -> None: ...

class ListCloudProviderRegionsRequest(_message.Message):
    __slots__ = ("account_id", "cloud_provider_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cloud_provider_id: str
    def __init__(self, account_id: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ...) -> None: ...

class ListCloudProviderRegionsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CloudProviderRegion]
    def __init__(self, items: _Optional[_Iterable[_Union[CloudProviderRegion, _Mapping]]] = ...) -> None: ...

class CloudProvider(_message.Message):
    __slots__ = ("id", "name", "free_tier")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FREE_TIER_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    free_tier: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., free_tier: bool = ...) -> None: ...

class CloudProviderRegion(_message.Message):
    __slots__ = ("id", "name", "country_iso_code", "geographical_sub_region")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ISO_CODE_FIELD_NUMBER: _ClassVar[int]
    GEOGRAPHICAL_SUB_REGION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    country_iso_code: str
    geographical_sub_region: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., country_iso_code: _Optional[str] = ..., geographical_sub_region: _Optional[str] = ...) -> None: ...
