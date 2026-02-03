from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCollectionsRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class ListCollectionsResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CollectionInfo]
    def __init__(self, items: _Optional[_Iterable[_Union[CollectionInfo, _Mapping]]] = ...) -> None: ...

class CollectionInfo(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
