from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.serverless.collections.v1 import collection_config_pb2 as _collection_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCollectionsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListCollectionsResponse(_message.Message):
    __slots__ = ("collections",)
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedCompositeFieldContainer[Collection]
    def __init__(self, collections: _Optional[_Iterable[_Union[Collection, _Mapping]]] = ...) -> None: ...

class CreateCollectionResponse(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: Collection
    def __init__(self, collection: _Optional[_Union[Collection, _Mapping]] = ...) -> None: ...

class CreateCollectionRequest(_message.Message):
    __slots__ = ("account_id", "collection_name", "configuration", "cloud_provider", "cloud_region")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REGION_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    collection_name: str
    configuration: _collection_config_pb2.CollectionConfiguration
    cloud_provider: str
    cloud_region: str
    def __init__(self, account_id: _Optional[str] = ..., collection_name: _Optional[str] = ..., configuration: _Optional[_Union[_collection_config_pb2.CollectionConfiguration, _Mapping]] = ..., cloud_provider: _Optional[str] = ..., cloud_region: _Optional[str] = ...) -> None: ...

class UpgradeCollectionRequest(_message.Message):
    __slots__ = ("account_id", "collection_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    collection_id: str
    def __init__(self, account_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...

class UpgradeCollectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCollectionRequest(_message.Message):
    __slots__ = ("account_id", "collection_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    collection_id: str
    def __init__(self, account_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...

class DeleteCollectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Collection(_message.Message):
    __slots__ = ("id", "name", "created_at", "configuration", "cloud_provider", "cloud_region", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REGION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_at: _timestamp_pb2.Timestamp
    configuration: _collection_config_pb2.CollectionConfiguration
    cloud_provider: str
    cloud_region: str
    state: CollectionState
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., configuration: _Optional[_Union[_collection_config_pb2.CollectionConfiguration, _Mapping]] = ..., cloud_provider: _Optional[str] = ..., cloud_region: _Optional[str] = ..., state: _Optional[_Union[CollectionState, _Mapping]] = ...) -> None: ...

class CollectionState(_message.Message):
    __slots__ = ("phase", "reason", "endpoint")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    phase: str
    reason: str
    endpoint: str
    def __init__(self, phase: _Optional[str] = ..., reason: _Optional[str] = ..., endpoint: _Optional[str] = ...) -> None: ...
