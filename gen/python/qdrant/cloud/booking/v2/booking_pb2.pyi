from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListPackagesRequest(_message.Message):
    __slots__ = ("account_id", "cloud_provider", "cloud_region", "statuses")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REGION_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cloud_provider: str
    cloud_region: str
    statuses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, account_id: _Optional[str] = ..., cloud_provider: _Optional[str] = ..., cloud_region: _Optional[str] = ..., statuses: _Optional[_Iterable[str]] = ...) -> None: ...

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
    __slots__ = ("id", "name", "type", "resource_configurations", "currency", "unit_int_price_per_hour", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    UNIT_INT_PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    resource_configurations: _containers.RepeatedCompositeFieldContainer[ResourceConfiguration]
    currency: str
    unit_int_price_per_hour: int
    status: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., resource_configurations: _Optional[_Iterable[_Union[ResourceConfiguration, _Mapping]]] = ..., currency: _Optional[str] = ..., unit_int_price_per_hour: _Optional[int] = ..., status: _Optional[str] = ...) -> None: ...

class ResourceConfiguration(_message.Message):
    __slots__ = ("amount", "resource_unit", "resource_type")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_UNIT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    amount: int
    resource_unit: str
    resource_type: str
    def __init__(self, amount: _Optional[int] = ..., resource_unit: _Optional[str] = ..., resource_type: _Optional[str] = ...) -> None: ...
