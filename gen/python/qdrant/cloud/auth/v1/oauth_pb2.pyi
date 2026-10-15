import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.event.v1 import events_pb2 as _events_pb2
from qdrant.cloud.facade.mcp.v1 import mcp_options_pb2 as _mcp_options_pb2
from qdrant.cloud.facade.v1 import facade_options_pb2 as _facade_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMyOAuthGrantsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListMyOAuthGrantsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[OAuthGrant]
    def __init__(self, items: _Optional[_Iterable[_Union[OAuthGrant, _Mapping]]] = ...) -> None: ...

class ListAccountOAuthGrantsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListAccountOAuthGrantsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[OAuthGrant]
    def __init__(self, items: _Optional[_Iterable[_Union[OAuthGrant, _Mapping]]] = ...) -> None: ...

class RevokeMyOAuthGrantRequest(_message.Message):
    __slots__ = ("oauth_grant_id",)
    OAUTH_GRANT_ID_FIELD_NUMBER: _ClassVar[int]
    oauth_grant_id: str
    def __init__(self, oauth_grant_id: _Optional[str] = ...) -> None: ...

class RevokeMyOAuthGrantResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokeAccountOAuthGrantRequest(_message.Message):
    __slots__ = ("account_id", "oauth_grant_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    OAUTH_GRANT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    oauth_grant_id: str
    def __init__(self, account_id: _Optional[str] = ..., oauth_grant_id: _Optional[str] = ...) -> None: ...

class RevokeAccountOAuthGrantResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OAuthGrant(_message.Message):
    __slots__ = ("id", "user_id", "user_email", "client_id", "client_name", "scope", "account_ids", "created_at", "last_used_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    user_email: str
    client_id: str
    client_name: str
    scope: _common_pb2.OauthScope
    account_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., user_email: _Optional[str] = ..., client_id: _Optional[str] = ..., client_name: _Optional[str] = ..., scope: _Optional[_Union[_common_pb2.OauthScope, str]] = ..., account_ids: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
