from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.iam.v1 import iam_pb2 as _iam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListUsersWithRolesRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListUsersWithRolesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[UserWithRoles]
    def __init__(self, items: _Optional[_Iterable[_Union[UserWithRoles, _Mapping]]] = ...) -> None: ...

class UserWithRoles(_message.Message):
    __slots__ = ("user", "roles")
    USER_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    user: _iam_pb2.User
    roles: _containers.RepeatedCompositeFieldContainer[_iam_pb2.Role]
    def __init__(self, user: _Optional[_Union[_iam_pb2.User, _Mapping]] = ..., roles: _Optional[_Iterable[_Union[_iam_pb2.Role, _Mapping]]] = ...) -> None: ...
