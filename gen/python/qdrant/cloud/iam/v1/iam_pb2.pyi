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

class UserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_STATUS_UNSPECIFIED: _ClassVar[UserStatus]
    USER_STATUS_ACTIVE: _ClassVar[UserStatus]
    USER_STATUS_BLOCKED: _ClassVar[UserStatus]
    USER_STATUS_DELETED: _ClassVar[UserStatus]

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

class RoleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_TYPE_UNSPECIFIED: _ClassVar[RoleType]
    ROLE_TYPE_SYSTEM: _ClassVar[RoleType]
    ROLE_TYPE_CUSTOM: _ClassVar[RoleType]
USER_STATUS_UNSPECIFIED: UserStatus
USER_STATUS_ACTIVE: UserStatus
USER_STATUS_BLOCKED: UserStatus
USER_STATUS_DELETED: UserStatus
LEGAL_DOCUMENT_TYPE_UNSPECIFIED: LegalDocumentType
LEGAL_DOCUMENT_TYPE_TERMS_OF_SERVICE: LegalDocumentType
LEGAL_DOCUMENT_TYPE_PRIVACY_POLICY: LegalDocumentType
LEGAL_DOCUMENT_TYPE_SLA: LegalDocumentType
USER_CONSENT_STATUS_UNSPECIFIED: UserConsentStatus
USER_CONSENT_STATUS_ACCEPTED: UserConsentStatus
USER_CONSENT_STATUS_REVOKED: UserConsentStatus
USER_CONSENT_STATUS_PENDING: UserConsentStatus
ROLE_TYPE_UNSPECIFIED: RoleType
ROLE_TYPE_SYSTEM: RoleType
ROLE_TYPE_CUSTOM: RoleType

class GetAuthenticatedUserRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAuthenticatedUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class GetUserConsentRequest(_message.Message):
    __slots__ = ("document_type",)
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    document_type: LegalDocumentType
    def __init__(self, document_type: _Optional[_Union[LegalDocumentType, str]] = ...) -> None: ...

class GetUserConsentResponse(_message.Message):
    __slots__ = ("document_type", "status", "last_modified_at", "is_accepted")
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    document_type: LegalDocumentType
    status: UserConsentStatus
    last_modified_at: _timestamp_pb2.Timestamp
    is_accepted: bool
    def __init__(self, document_type: _Optional[_Union[LegalDocumentType, str]] = ..., status: _Optional[_Union[UserConsentStatus, str]] = ..., last_modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_accepted: bool = ...) -> None: ...

class RecordUserConsentRequest(_message.Message):
    __slots__ = ("document_type", "status_update")
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    document_type: LegalDocumentType
    status_update: UserConsentStatus
    def __init__(self, document_type: _Optional[_Union[LegalDocumentType, str]] = ..., status_update: _Optional[_Union[UserConsentStatus, str]] = ...) -> None: ...

class RecordUserConsentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPermissionsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListPermissionsResponse(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class ListRolesRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListRolesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Role]
    def __init__(self, items: _Optional[_Iterable[_Union[Role, _Mapping]]] = ...) -> None: ...

class GetRoleRequest(_message.Message):
    __slots__ = ("account_id", "role_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    role_id: str
    def __init__(self, account_id: _Optional[str] = ..., role_id: _Optional[str] = ...) -> None: ...

class GetRoleResponse(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class CreateRoleRequest(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class CreateRoleResponse(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class UpdateRoleRequest(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class UpdateRoleResponse(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class DeleteRoleRequest(_message.Message):
    __slots__ = ("account_id", "role_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    role_id: str
    def __init__(self, account_id: _Optional[str] = ..., role_id: _Optional[str] = ...) -> None: ...

class DeleteRoleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEffectivePermissionsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListEffectivePermissionsResponse(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignUserRolesRequest(_message.Message):
    __slots__ = ("account_id", "user_id", "role_ids_to_add", "role_ids_to_delete")
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
    __slots__ = ("id", "created_at", "last_modified_at", "email", "status", "default_account_id", "notification_preferences")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    last_modified_at: _timestamp_pb2.Timestamp
    email: str
    status: UserStatus
    default_account_id: str
    notification_preferences: NotificationPreferences
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., email: _Optional[str] = ..., status: _Optional[_Union[UserStatus, str]] = ..., default_account_id: _Optional[str] = ..., notification_preferences: _Optional[_Union[NotificationPreferences, _Mapping]] = ...) -> None: ...

class NotificationPreferences(_message.Message):
    __slots__ = ("email_newsletter_enabled",)
    EMAIL_NEWSLETTER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    email_newsletter_enabled: bool
    def __init__(self, email_newsletter_enabled: bool = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("id", "created_at", "last_modified_at", "account_id", "name", "description", "role_type", "permissions")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    last_modified_at: _timestamp_pb2.Timestamp
    account_id: str
    name: str
    description: str
    role_type: RoleType
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., role_type: _Optional[_Union[RoleType, str]] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...
