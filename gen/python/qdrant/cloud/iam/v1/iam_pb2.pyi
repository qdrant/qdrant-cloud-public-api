import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.event.v1 import events_pb2 as _events_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_STATUS_UNSPECIFIED: _ClassVar[UserStatus]
    USER_STATUS_ACTIVE: _ClassVar[UserStatus]
    USER_STATUS_BLOCKED: _ClassVar[UserStatus]
    USER_STATUS_DELETED: _ClassVar[UserStatus]

class RoleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_TYPE_UNSPECIFIED: _ClassVar[RoleType]
    ROLE_TYPE_SYSTEM: _ClassVar[RoleType]
    ROLE_TYPE_CUSTOM: _ClassVar[RoleType]

class SystemRoleSubType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYSTEM_ROLE_SUB_TYPE_UNSPECIFIED: _ClassVar[SystemRoleSubType]
    SYSTEM_ROLE_SUB_TYPE_OWNER: _ClassVar[SystemRoleSubType]
    SYSTEM_ROLE_SUB_TYPE_ADMIN: _ClassVar[SystemRoleSubType]
    SYSTEM_ROLE_SUB_TYPE_BASE: _ClassVar[SystemRoleSubType]

class LegalDocumentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LEGAL_DOCUMENT_TYPE_UNSPECIFIED: _ClassVar[LegalDocumentType]
    LEGAL_DOCUMENT_TYPE_TERMS_OF_SERVICE: _ClassVar[LegalDocumentType]
    LEGAL_DOCUMENT_TYPE_PRIVACY_POLICY: _ClassVar[LegalDocumentType]
    LEGAL_DOCUMENT_TYPE_SLA: _ClassVar[LegalDocumentType]

class UserConsentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_CONSENT_STATUS_UNSPECIFIED: _ClassVar[UserConsentStatus]
    USER_CONSENT_STATUS_ACCEPTED: _ClassVar[UserConsentStatus]
    USER_CONSENT_STATUS_REVOKED: _ClassVar[UserConsentStatus]
    USER_CONSENT_STATUS_PENDING: _ClassVar[UserConsentStatus]
USER_STATUS_UNSPECIFIED: UserStatus
USER_STATUS_ACTIVE: UserStatus
USER_STATUS_BLOCKED: UserStatus
USER_STATUS_DELETED: UserStatus
ROLE_TYPE_UNSPECIFIED: RoleType
ROLE_TYPE_SYSTEM: RoleType
ROLE_TYPE_CUSTOM: RoleType
SYSTEM_ROLE_SUB_TYPE_UNSPECIFIED: SystemRoleSubType
SYSTEM_ROLE_SUB_TYPE_OWNER: SystemRoleSubType
SYSTEM_ROLE_SUB_TYPE_ADMIN: SystemRoleSubType
SYSTEM_ROLE_SUB_TYPE_BASE: SystemRoleSubType
LEGAL_DOCUMENT_TYPE_UNSPECIFIED: LegalDocumentType
LEGAL_DOCUMENT_TYPE_TERMS_OF_SERVICE: LegalDocumentType
LEGAL_DOCUMENT_TYPE_PRIVACY_POLICY: LegalDocumentType
LEGAL_DOCUMENT_TYPE_SLA: LegalDocumentType
USER_CONSENT_STATUS_UNSPECIFIED: UserConsentStatus
USER_CONSENT_STATUS_ACCEPTED: UserConsentStatus
USER_CONSENT_STATUS_REVOKED: UserConsentStatus
USER_CONSENT_STATUS_PENDING: UserConsentStatus

class GetAuthenticatedUserRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAuthenticatedUserResponse(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, items: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class GetUserConsentRequest(_message.Message):
    __slots__ = ()
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    document_type: LegalDocumentType
    def __init__(self, document_type: _Optional[_Union[LegalDocumentType, str]] = ...) -> None: ...

class GetUserConsentResponse(_message.Message):
    __slots__ = ()
    USER_CONSENT_FIELD_NUMBER: _ClassVar[int]
    user_consent: UserConsent
    def __init__(self, user_consent: _Optional[_Union[UserConsent, _Mapping]] = ...) -> None: ...

class RecordUserConsentRequest(_message.Message):
    __slots__ = ()
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    document_type: LegalDocumentType
    status_update: UserConsentStatus
    def __init__(self, document_type: _Optional[_Union[LegalDocumentType, str]] = ..., status_update: _Optional[_Union[UserConsentStatus, str]] = ...) -> None: ...

class RecordUserConsentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPermissionsRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListPermissionsResponse(_message.Message):
    __slots__ = ()
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    def __init__(self, permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ...) -> None: ...

class ListRolesRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListRolesResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Role]
    def __init__(self, items: _Optional[_Iterable[_Union[Role, _Mapping]]] = ...) -> None: ...

class GetRoleRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    role_id: str
    def __init__(self, account_id: _Optional[str] = ..., role_id: _Optional[str] = ...) -> None: ...

class GetRoleResponse(_message.Message):
    __slots__ = ()
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class CreateRoleRequest(_message.Message):
    __slots__ = ()
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class CreateRoleResponse(_message.Message):
    __slots__ = ()
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class UpdateRoleRequest(_message.Message):
    __slots__ = ()
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class UpdateRoleResponse(_message.Message):
    __slots__ = ()
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class DeleteRoleRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    role_id: str
    def __init__(self, account_id: _Optional[str] = ..., role_id: _Optional[str] = ...) -> None: ...

class DeleteRoleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEffectivePermissionsRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListEffectivePermissionsResponse(_message.Message):
    __slots__ = ()
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    def __init__(self, permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ...) -> None: ...

class ListUserRolesRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    user_id: str
    def __init__(self, account_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class ListUserRolesResponse(_message.Message):
    __slots__ = ()
    ROLES_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Role]
    def __init__(self, roles: _Optional[_Iterable[_Union[Role, _Mapping]]] = ...) -> None: ...

class ListRoleUsersRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    role_id: str
    def __init__(self, account_id: _Optional[str] = ..., role_id: _Optional[str] = ...) -> None: ...

class ListRoleUsersResponse(_message.Message):
    __slots__ = ()
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class AssignUserRolesRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    user_id: str
    role_ids_to_add: _containers.RepeatedScalarFieldContainer[str]
    role_ids_to_delete: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, account_id: _Optional[str] = ..., user_id: _Optional[str] = ..., role_ids_to_add: _Optional[_Iterable[str]] = ..., role_ids_to_delete: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignUserRolesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class User(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    last_modified_at: _timestamp_pb2.Timestamp
    email: str
    status: UserStatus
    default_account_id: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., email: _Optional[str] = ..., status: _Optional[_Union[UserStatus, str]] = ..., default_account_id: _Optional[str] = ...) -> None: ...

class Permission(_message.Message):
    __slots__ = ()
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    value: str
    category: str
    def __init__(self, value: _Optional[str] = ..., category: _Optional[str] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    last_modified_at: _timestamp_pb2.Timestamp
    account_id: str
    name: str
    description: str
    role_type: RoleType
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    sub_type: SystemRoleSubType
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., role_type: _Optional[_Union[RoleType, str]] = ..., permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ..., sub_type: _Optional[_Union[SystemRoleSubType, str]] = ...) -> None: ...

class LogoutUserRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LogoutUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UserConsent(_message.Message):
    __slots__ = ()
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    document_type: LegalDocumentType
    status: UserConsentStatus
    last_modified_at: _timestamp_pb2.Timestamp
    is_accepted: bool
    def __init__(self, document_type: _Optional[_Union[LegalDocumentType, str]] = ..., status: _Optional[_Union[UserConsentStatus, str]] = ..., last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_accepted: _Optional[bool] = ...) -> None: ...
