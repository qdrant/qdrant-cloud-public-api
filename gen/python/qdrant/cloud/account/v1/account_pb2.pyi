from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountInviteStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCOUNT_INVITE_STATUS_UNSPECIFIED: _ClassVar[AccountInviteStatus]
    ACCOUNT_INVITE_STATUS_PENDING: _ClassVar[AccountInviteStatus]
    ACCOUNT_INVITE_STATUS_ACCEPTED: _ClassVar[AccountInviteStatus]
    ACCOUNT_INVITE_STATUS_REJECTED: _ClassVar[AccountInviteStatus]
    ACCOUNT_INVITE_STATUS_CANCELED: _ClassVar[AccountInviteStatus]
ACCOUNT_INVITE_STATUS_UNSPECIFIED: AccountInviteStatus
ACCOUNT_INVITE_STATUS_PENDING: AccountInviteStatus
ACCOUNT_INVITE_STATUS_ACCEPTED: AccountInviteStatus
ACCOUNT_INVITE_STATUS_REJECTED: AccountInviteStatus
ACCOUNT_INVITE_STATUS_CANCELED: AccountInviteStatus

class ListAccountsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAccountsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Account]
    def __init__(self, items: _Optional[_Iterable[_Union[Account, _Mapping]]] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class GetAccountResponse(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class CreateAccountRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class CreateAccountResponse(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class UpdateAccountRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class UpdateAccountResponse(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class DeleteAccountRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class DeleteAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAccountInvitesRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListAccountInvitesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AccountInvite]
    def __init__(self, items: _Optional[_Iterable[_Union[AccountInvite, _Mapping]]] = ...) -> None: ...

class ListReceivedAccountInvitesRequest(_message.Message):
    __slots__ = ("status_filter",)
    STATUS_FILTER_FIELD_NUMBER: _ClassVar[int]
    status_filter: AccountInviteStatus
    def __init__(self, status_filter: _Optional[_Union[AccountInviteStatus, str]] = ...) -> None: ...

class ListReceivedAccountInvitesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AccountInvite]
    def __init__(self, items: _Optional[_Iterable[_Union[AccountInvite, _Mapping]]] = ...) -> None: ...

class GetAccountInviteRequest(_message.Message):
    __slots__ = ("account_id", "invite_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    invite_id: str
    def __init__(self, account_id: _Optional[str] = ..., invite_id: _Optional[str] = ...) -> None: ...

class GetAccountInviteResponse(_message.Message):
    __slots__ = ("account_invite",)
    ACCOUNT_INVITE_FIELD_NUMBER: _ClassVar[int]
    account_invite: AccountInvite
    def __init__(self, account_invite: _Optional[_Union[AccountInvite, _Mapping]] = ...) -> None: ...

class CreateAccountInviteRequest(_message.Message):
    __slots__ = ("account_invite",)
    ACCOUNT_INVITE_FIELD_NUMBER: _ClassVar[int]
    account_invite: AccountInvite
    def __init__(self, account_invite: _Optional[_Union[AccountInvite, _Mapping]] = ...) -> None: ...

class CreateAccountInviteResponse(_message.Message):
    __slots__ = ("account_invite",)
    ACCOUNT_INVITE_FIELD_NUMBER: _ClassVar[int]
    account_invite: AccountInvite
    def __init__(self, account_invite: _Optional[_Union[AccountInvite, _Mapping]] = ...) -> None: ...

class DeleteAccountInviteRequest(_message.Message):
    __slots__ = ("account_id", "invite_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    invite_id: str
    def __init__(self, account_id: _Optional[str] = ..., invite_id: _Optional[str] = ...) -> None: ...

class DeleteAccountInviteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AcceptAccountInviteRequest(_message.Message):
    __slots__ = ("account_id", "invite_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    invite_id: str
    def __init__(self, account_id: _Optional[str] = ..., invite_id: _Optional[str] = ...) -> None: ...

class AcceptAccountInviteResponse(_message.Message):
    __slots__ = ("invite",)
    INVITE_FIELD_NUMBER: _ClassVar[int]
    invite: AccountInvite
    def __init__(self, invite: _Optional[_Union[AccountInvite, _Mapping]] = ...) -> None: ...

class RejectAccountInviteRequest(_message.Message):
    __slots__ = ("account_id", "invite_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    invite_id: str
    def __init__(self, account_id: _Optional[str] = ..., invite_id: _Optional[str] = ...) -> None: ...

class RejectAccountInviteResponse(_message.Message):
    __slots__ = ("invite",)
    INVITE_FIELD_NUMBER: _ClassVar[int]
    invite: AccountInvite
    def __init__(self, invite: _Optional[_Union[AccountInvite, _Mapping]] = ...) -> None: ...

class Account(_message.Message):
    __slots__ = ("id", "created_at", "last_modified_at", "name", "owner_id", "owner_email", "privileges")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    last_modified_at: _timestamp_pb2.Timestamp
    name: str
    owner_id: str
    owner_email: str
    privileges: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., owner_id: _Optional[str] = ..., owner_email: _Optional[str] = ..., privileges: _Optional[_Iterable[str]] = ...) -> None: ...

class AccountInvite(_message.Message):
    __slots__ = ("id", "account_id", "account_name", "user_email", "user_role_ids", "created_at", "created_by_user_id", "created_by_name", "last_modified_at", "user_id", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    account_name: str
    user_email: str
    user_role_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    created_by_user_id: str
    created_by_name: str
    last_modified_at: _timestamp_pb2.Timestamp
    user_id: str
    status: AccountInviteStatus
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., account_name: _Optional[str] = ..., user_email: _Optional[str] = ..., user_role_ids: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_by_name: _Optional[str] = ..., last_modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., status: _Optional[_Union[AccountInviteStatus, str]] = ...) -> None: ...
