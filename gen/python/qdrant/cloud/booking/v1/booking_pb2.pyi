from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackageStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PACKAGE_STATUS_UNSPECIFIED: _ClassVar[PackageStatus]
    PACKAGE_STATUS_ACTIVE: _ClassVar[PackageStatus]
    PACKAGE_STATUS_DEACTIVATED: _ClassVar[PackageStatus]
PACKAGE_STATUS_UNSPECIFIED: PackageStatus
PACKAGE_STATUS_ACTIVE: PackageStatus
PACKAGE_STATUS_DEACTIVATED: PackageStatus

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
    __slots__ = ("id", "name", "type", "resource_configuration", "currency", "unit_int_price_per_hour", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    UNIT_INT_PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    resource_configuration: ResourceConfiguration
    currency: str
    unit_int_price_per_hour: int
    status: PackageStatus
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., resource_configuration: _Optional[_Union[ResourceConfiguration, _Mapping]] = ..., currency: _Optional[str] = ..., unit_int_price_per_hour: _Optional[int] = ..., status: _Optional[_Union[PackageStatus, str]] = ...) -> None: ...

class ResourceConfiguration(_message.Message):
    __slots__ = ("ram", "cpu", "disk")
    RAM_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    ram: str
    cpu: str
    disk: str
    def __init__(self, ram: _Optional[str] = ..., cpu: _Optional[str] = ..., disk: _Optional[str] = ...) -> None: ...
