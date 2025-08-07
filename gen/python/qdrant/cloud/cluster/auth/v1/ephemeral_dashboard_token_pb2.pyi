from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEphemeralDashboardTokenRequest(_message.Message):
    __slots__ = ("account_id", "cluster_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class CreateEphemeralDashboardTokenResponse(_message.Message):
    __slots__ = ("ephemeral_dashboard_token",)
    EPHEMERAL_DASHBOARD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ephemeral_dashboard_token: EphemeralDashboardToken
    def __init__(self, ephemeral_dashboard_token: _Optional[_Union[EphemeralDashboardToken, _Mapping]] = ...) -> None: ...

class EphemeralDashboardToken(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...
