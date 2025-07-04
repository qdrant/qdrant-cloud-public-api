from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetAuthenticatedUserQuotasRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAuthenticatedUserQuotasResponse(_message.Message):
    __slots__ = ("max_owned_accounts",)
    MAX_OWNED_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    max_owned_accounts: int
    def __init__(self, max_owned_accounts: _Optional[int] = ...) -> None: ...

class GetAccountQuotasRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class GetAccountQuotasResponse(_message.Message):
    __slots__ = ("account_id", "max_clusters", "max_cluster_nodes", "max_cluster_database_api_keys")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    MAX_CLUSTER_NODES_FIELD_NUMBER: _ClassVar[int]
    MAX_CLUSTER_DATABASE_API_KEYS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    max_clusters: int
    max_cluster_nodes: int
    max_cluster_database_api_keys: int
    def __init__(self, account_id: _Optional[str] = ..., max_clusters: _Optional[int] = ..., max_cluster_nodes: _Optional[int] = ..., max_cluster_database_api_keys: _Optional[int] = ...) -> None: ...
