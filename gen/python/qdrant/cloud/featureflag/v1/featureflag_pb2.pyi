from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureFlagStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEATURE_FLAG_STATUS_UNSPECIFIED: _ClassVar[FeatureFlagStatus]
    FEATURE_FLAG_STATUS_ENABLED: _ClassVar[FeatureFlagStatus]
    FEATURE_FLAG_STATUS_DISABLED: _ClassVar[FeatureFlagStatus]
FEATURE_FLAG_STATUS_UNSPECIFIED: FeatureFlagStatus
FEATURE_FLAG_STATUS_ENABLED: FeatureFlagStatus
FEATURE_FLAG_STATUS_DISABLED: FeatureFlagStatus

class ListFeatureFlagsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListFeatureFlagsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FeatureFlag]
    def __init__(self, items: _Optional[_Iterable[_Union[FeatureFlag, _Mapping]]] = ...) -> None: ...

class FeatureFlag(_message.Message):
    __slots__ = ("name", "status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: FeatureFlagStatus
    def __init__(self, name: _Optional[str] = ..., status: _Optional[_Union[FeatureFlagStatus, str]] = ...) -> None: ...
