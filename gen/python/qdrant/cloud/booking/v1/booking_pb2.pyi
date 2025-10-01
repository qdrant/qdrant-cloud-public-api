from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackageStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PACKAGE_STATUS_UNSPECIFIED: _ClassVar[PackageStatus]
    PACKAGE_STATUS_ACTIVE: _ClassVar[PackageStatus]
    PACKAGE_STATUS_DEACTIVATED: _ClassVar[PackageStatus]

class PackageTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PACKAGE_TIER_STATUS_UNSPECIFIED: _ClassVar[PackageTier]
    PACKAGE_TIER_STANDARD: _ClassVar[PackageTier]
    PACKAGE_TIER_PREMIUM: _ClassVar[PackageTier]
PACKAGE_STATUS_UNSPECIFIED: PackageStatus
PACKAGE_STATUS_ACTIVE: PackageStatus
PACKAGE_STATUS_DEACTIVATED: PackageStatus
PACKAGE_TIER_STATUS_UNSPECIFIED: PackageTier
PACKAGE_TIER_STANDARD: PackageTier
PACKAGE_TIER_PREMIUM: PackageTier

class ListPackagesRequest(_message.Message):
    __slots__ = ("account_id", "cloud_provider_id", "cloud_provider_region_id", "statuses")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cloud_provider_id: str
    cloud_provider_region_id: str
    statuses: _containers.RepeatedScalarFieldContainer[PackageStatus]
    def __init__(self, account_id: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ..., cloud_provider_region_id: _Optional[str] = ..., statuses: _Optional[_Iterable[_Union[PackageStatus, str]]] = ...) -> None: ...

class ListPackagesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Package]
    def __init__(self, items: _Optional[_Iterable[_Union[Package, _Mapping]]] = ...) -> None: ...

class ListGlobalPackagesRequest(_message.Message):
    __slots__ = ("cloud_provider_id", "cloud_provider_region_id")
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    cloud_provider_id: str
    cloud_provider_region_id: str
    def __init__(self, cloud_provider_id: _Optional[str] = ..., cloud_provider_region_id: _Optional[str] = ...) -> None: ...

class ListGlobalPackagesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Package]
    def __init__(self, items: _Optional[_Iterable[_Union[Package, _Mapping]]] = ...) -> None: ...

class GetPackageRequest(_message.Message):
    __slots__ = ("account_id", "id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    id: str
    def __init__(self, account_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetPackageResponse(_message.Message):
    __slots__ = ("package",)
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    package: Package
    def __init__(self, package: _Optional[_Union[Package, _Mapping]] = ...) -> None: ...

class Package(_message.Message):
    __slots__ = ("id", "name", "type", "resource_configuration", "currency", "unit_int_price_per_hour", "status", "tier", "available_additional_resources")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    UNIT_INT_PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_ADDITIONAL_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    resource_configuration: ResourceConfiguration
    currency: str
    unit_int_price_per_hour: int
    status: PackageStatus
    tier: PackageTier
    available_additional_resources: AvailableAdditionalResources
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., resource_configuration: _Optional[_Union[ResourceConfiguration, _Mapping]] = ..., currency: _Optional[str] = ..., unit_int_price_per_hour: _Optional[int] = ..., status: _Optional[_Union[PackageStatus, str]] = ..., tier: _Optional[_Union[PackageTier, str]] = ..., available_additional_resources: _Optional[_Union[AvailableAdditionalResources, _Mapping]] = ...) -> None: ...

class AvailableAdditionalResources(_message.Message):
    __slots__ = ("disk_price_per_hour",)
    DISK_PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    disk_price_per_hour: int
    def __init__(self, disk_price_per_hour: _Optional[int] = ...) -> None: ...

class ResourceConfiguration(_message.Message):
    __slots__ = ("ram", "cpu", "disk")
    RAM_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    ram: str
    cpu: str
    disk: str
    def __init__(self, ram: _Optional[str] = ..., cpu: _Optional[str] = ..., disk: _Optional[str] = ...) -> None: ...

class GetQuoteRequest(_message.Message):
    __slots__ = ("account_id", "cloud_provider_id", "cloud_provider_region_id", "number_of_nodes", "package_id", "additional_disk_gib")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_NODES_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DISK_GIB_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cloud_provider_id: str
    cloud_provider_region_id: str
    number_of_nodes: int
    package_id: str
    additional_disk_gib: int
    def __init__(self, account_id: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ..., cloud_provider_region_id: _Optional[str] = ..., number_of_nodes: _Optional[int] = ..., package_id: _Optional[str] = ..., additional_disk_gib: _Optional[int] = ...) -> None: ...

class GetQuoteResponse(_message.Message):
    __slots__ = ("currency", "original_price_per_hour", "discounted_price_per_hour", "discount_percentage")
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    DISCOUNTED_PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    currency: str
    original_price_per_hour: int
    discounted_price_per_hour: int
    discount_percentage: float
    def __init__(self, currency: _Optional[str] = ..., original_price_per_hour: _Optional[int] = ..., discounted_price_per_hour: _Optional[int] = ..., discount_percentage: _Optional[float] = ...) -> None: ...
