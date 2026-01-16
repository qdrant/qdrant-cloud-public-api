import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.event.v1 import events_pb2 as _events_pb2
from qdrant.cloud.iam.v1 import iam_pb2 as _iam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Account]
    def __init__(self, items: _Optional[_Iterable[_Union[Account, _Mapping]]] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class GetAccountResponse(_message.Message):
    __slots__ = ()
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class CreateAccountRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class CreateAccountResponse(_message.Message):
    __slots__ = ()
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class UpdateAccountRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class UpdateAccountResponse(_message.Message):
    __slots__ = ()
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class DeleteAccountRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class DeleteAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LeaveAccountRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class LeaveAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAccountInvitesRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    statuses: _containers.RepeatedScalarFieldContainer[AccountInviteStatus]
    def __init__(self, account_id: _Optional[str] = ..., statuses: _Optional[_Iterable[_Union[AccountInviteStatus, str]]] = ...) -> None: ...

class ListAccountInvitesResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AccountInvite]
    def __init__(self, items: _Optional[_Iterable[_Union[AccountInvite, _Mapping]]] = ...) -> None: ...

class ListReceivedAccountInvitesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListReceivedAccountInvitesResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AccountInvite]
    def __init__(self, items: _Optional[_Iterable[_Union[AccountInvite, _Mapping]]] = ...) -> None: ...

class GetAccountInviteRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    invite_id: str
    def __init__(self, account_id: _Optional[str] = ..., invite_id: _Optional[str] = ...) -> None: ...

class GetAccountInviteResponse(_message.Message):
    __slots__ = ()
    ACCOUNT_INVITE_FIELD_NUMBER: _ClassVar[int]
    account_invite: AccountInvite
    def __init__(self, account_invite: _Optional[_Union[AccountInvite, _Mapping]] = ...) -> None: ...

class CreateAccountInviteRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_INVITE_FIELD_NUMBER: _ClassVar[int]
    account_invite: AccountInvite
    def __init__(self, account_invite: _Optional[_Union[AccountInvite, _Mapping]] = ...) -> None: ...

class CreateAccountInviteResponse(_message.Message):
    __slots__ = ()
    ACCOUNT_INVITE_FIELD_NUMBER: _ClassVar[int]
    account_invite: AccountInvite
    def __init__(self, account_invite: _Optional[_Union[AccountInvite, _Mapping]] = ...) -> None: ...

class DeleteAccountInviteRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    invite_id: str
    def __init__(self, account_id: _Optional[str] = ..., invite_id: _Optional[str] = ...) -> None: ...

class DeleteAccountInviteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AcceptAccountInviteRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    invite_id: str
    def __init__(self, account_id: _Optional[str] = ..., invite_id: _Optional[str] = ...) -> None: ...

class AcceptAccountInviteResponse(_message.Message):
    __slots__ = ()
    INVITE_FIELD_NUMBER: _ClassVar[int]
    invite: AccountInvite
    def __init__(self, invite: _Optional[_Union[AccountInvite, _Mapping]] = ...) -> None: ...

class RejectAccountInviteRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    invite_id: str
    def __init__(self, account_id: _Optional[str] = ..., invite_id: _Optional[str] = ...) -> None: ...

class RejectAccountInviteResponse(_message.Message):
    __slots__ = ()
    INVITE_FIELD_NUMBER: _ClassVar[int]
    invite: AccountInvite
    def __init__(self, invite: _Optional[_Union[AccountInvite, _Mapping]] = ...) -> None: ...

class ListAccountMembersRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListAccountMembersResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AccountMember]
    def __init__(self, items: _Optional[_Iterable[_Union[AccountMember, _Mapping]]] = ...) -> None: ...

class GetAccountMemberRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    user_id: str
    def __init__(self, account_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GetAccountMemberResponse(_message.Message):
    __slots__ = ()
    ACCOUNT_MEMBER_FIELD_NUMBER: _ClassVar[int]
    account_member: AccountMember
    def __init__(self, account_member: _Optional[_Union[AccountMember, _Mapping]] = ...) -> None: ...

class DeleteAccountMemberRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    user_id: str
    def __init__(self, account_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class DeleteAccountMemberResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateAccountCompanyRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    company: Company
    def __init__(self, account_id: _Optional[str] = ..., company: _Optional[_Union[Company, _Mapping]] = ...) -> None: ...

class UpdateAccountCompanyResponse(_message.Message):
    __slots__ = ()
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class SuggestCompanyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    email: str
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class SuggestCompanyResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Company]
    def __init__(self, items: _Optional[_Iterable[_Union[Company, _Mapping]]] = ...) -> None: ...

class Account(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    last_modified_at: _timestamp_pb2.Timestamp
    name: str
    external_owner_id: str
    owner_email: str
    privileges: _containers.RepeatedScalarFieldContainer[str]
    company: Company
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., external_owner_id: _Optional[str] = ..., owner_email: _Optional[str] = ..., privileges: _Optional[_Iterable[str]] = ..., company: _Optional[_Union[Company, _Mapping]] = ...) -> None: ...

class AccountInvite(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    account_name: str
    user_email: str
    user_role_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    created_by_user_id: str
    created_by_email: str
    last_modified_at: _timestamp_pb2.Timestamp
    status: AccountInviteStatus
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., account_name: _Optional[str] = ..., user_email: _Optional[str] = ..., user_role_ids: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_by_email: _Optional[str] = ..., last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[AccountInviteStatus, str]] = ...) -> None: ...

class AccountMember(_message.Message):
    __slots__ = ()
    ACCOUNT_MEMBER_FIELD_NUMBER: _ClassVar[int]
    IS_OWNER_FIELD_NUMBER: _ClassVar[int]
    account_member: _iam_pb2.User
    is_owner: bool
    def __init__(self, account_member: _Optional[_Union[_iam_pb2.User, _Mapping]] = ..., is_owner: _Optional[bool] = ...) -> None: ...

class Company(_message.Message):
    __slots__ = ()
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    domain: str
    name: str
    def __init__(self, domain: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
