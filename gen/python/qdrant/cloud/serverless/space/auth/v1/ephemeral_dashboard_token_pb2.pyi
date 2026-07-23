from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.event.v1 import events_pb2 as _events_pb2
from qdrant.cloud.serverless.space.auth.v1 import space_api_key_pb2 as _space_api_key_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEphemeralDashboardTokenRequest(_message.Message):
    __slots__ = ("account_id", "space_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...

class CreateEphemeralDashboardTokenResponse(_message.Message):
    __slots__ = ("ephemeral_dashboard_token",)
    EPHEMERAL_DASHBOARD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ephemeral_dashboard_token: EphemeralDashboardToken
    def __init__(self, ephemeral_dashboard_token: _Optional[_Union[EphemeralDashboardToken, _Mapping]] = ...) -> None: ...

class ListEphemeralDashboardTokensRequest(_message.Message):
    __slots__ = ("account_id", "space_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_id: str
    def __init__(self, account_id: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...

class ListEphemeralDashboardTokensResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_space_api_key_pb2.SpaceApiKey]
    def __init__(self, items: _Optional[_Iterable[_Union[_space_api_key_pb2.SpaceApiKey, _Mapping]]] = ...) -> None: ...

class RevokeEphemeralDashboardTokenRequest(_message.Message):
    __slots__ = ("account_id", "space_api_key_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    space_api_key_id: str
    def __init__(self, account_id: _Optional[str] = ..., space_api_key_id: _Optional[str] = ...) -> None: ...

class RevokeEphemeralDashboardTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EphemeralDashboardToken(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...
