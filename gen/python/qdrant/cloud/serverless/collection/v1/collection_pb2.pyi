from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.serverless.collection.v1 import collection_config_pb2 as _collection_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CollectionStatePhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLLECTION_STATE_PHASE_UNSPECIFIED: _ClassVar[CollectionStatePhase]
    COLLECTION_STATE_PHASE_READY: _ClassVar[CollectionStatePhase]
    COLLECTION_STATE_PHASE_PROCESSING: _ClassVar[CollectionStatePhase]
    COLLECTION_STATE_PHASE_DISABLED: _ClassVar[CollectionStatePhase]
COLLECTION_STATE_PHASE_UNSPECIFIED: CollectionStatePhase
COLLECTION_STATE_PHASE_READY: CollectionStatePhase
COLLECTION_STATE_PHASE_PROCESSING: CollectionStatePhase
COLLECTION_STATE_PHASE_DISABLED: CollectionStatePhase

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

class CreateCollectionRequest(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: Collection
    def __init__(self, collection: _Optional[_Union[Collection, _Mapping]] = ...) -> None: ...

class CreateCollectionResponse(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: Collection
    def __init__(self, collection: _Optional[_Union[Collection, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("id", "created_at", "account_id", "name", "deleted_at", "cloud_provider_id", "cloud_provider_region_id", "configuration", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    account_id: str
    name: str
    deleted_at: _timestamp_pb2.Timestamp
    cloud_provider_id: str
    cloud_provider_region_id: str
    configuration: _collection_config_pb2.CollectionConfiguration
    state: CollectionState
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., name: _Optional[str] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cloud_provider_id: _Optional[str] = ..., cloud_provider_region_id: _Optional[str] = ..., configuration: _Optional[_Union[_collection_config_pb2.CollectionConfiguration, _Mapping]] = ..., state: _Optional[_Union[CollectionState, _Mapping]] = ...) -> None: ...

class CollectionState(_message.Message):
    __slots__ = ("phase", "reason", "endpoint")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    phase: CollectionStatePhase
    reason: str
    endpoint: CollectionEndpoint
    def __init__(self, phase: _Optional[_Union[CollectionStatePhase, str]] = ..., reason: _Optional[str] = ..., endpoint: _Optional[_Union[CollectionEndpoint, _Mapping]] = ...) -> None: ...

class CollectionEndpoint(_message.Message):
    __slots__ = ("url", "rest_port", "grpc_port")
    URL_FIELD_NUMBER: _ClassVar[int]
    REST_PORT_FIELD_NUMBER: _ClassVar[int]
    GRPC_PORT_FIELD_NUMBER: _ClassVar[int]
    url: str
    rest_port: int
    grpc_port: int
    def __init__(self, url: _Optional[str] = ..., rest_port: _Optional[int] = ..., grpc_port: _Optional[int] = ...) -> None: ...
