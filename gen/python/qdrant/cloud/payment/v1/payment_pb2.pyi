import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAYMENT_PROVIDER_TYPE_UNSPECIFIED: _ClassVar[PaymentProviderType]
    PAYMENT_PROVIDER_TYPE_STRIPE: _ClassVar[PaymentProviderType]
    PAYMENT_PROVIDER_TYPE_AWS_MARKETPLACE: _ClassVar[PaymentProviderType]
    PAYMENT_PROVIDER_TYPE_GCP_MARKETPLACE: _ClassVar[PaymentProviderType]
    PAYMENT_PROVIDER_TYPE_AZURE_MARKETPLACE: _ClassVar[PaymentProviderType]
    PAYMENT_PROVIDER_TYPE_CUSTOM: _ClassVar[PaymentProviderType]

class PaymentInformationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAYMENT_INFORMATION_STATUS_UNSPECIFIED: _ClassVar[PaymentInformationStatus]
    PAYMENT_INFORMATION_STATUS_ACTIVE: _ClassVar[PaymentInformationStatus]
    PAYMENT_INFORMATION_STATUS_INACTIVE: _ClassVar[PaymentInformationStatus]
    PAYMENT_INFORMATION_STATUS_PENDING: _ClassVar[PaymentInformationStatus]

class SetupIntentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SETUP_INTENT_STATUS_UNSPECIFIED: _ClassVar[SetupIntentStatus]
    SETUP_INTENT_STATUS_REQUIRES_PAYMENT_METHOD: _ClassVar[SetupIntentStatus]
    SETUP_INTENT_STATUS_REQUIRES_CONFIRMATION: _ClassVar[SetupIntentStatus]
    SETUP_INTENT_STATUS_REQUIRES_ACTION: _ClassVar[SetupIntentStatus]
    SETUP_INTENT_STATUS_PROCESSING: _ClassVar[SetupIntentStatus]
    SETUP_INTENT_STATUS_CANCELED: _ClassVar[SetupIntentStatus]
    SETUP_INTENT_STATUS_SUCCEEDED: _ClassVar[SetupIntentStatus]
PAYMENT_PROVIDER_TYPE_UNSPECIFIED: PaymentProviderType
PAYMENT_PROVIDER_TYPE_STRIPE: PaymentProviderType
PAYMENT_PROVIDER_TYPE_AWS_MARKETPLACE: PaymentProviderType
PAYMENT_PROVIDER_TYPE_GCP_MARKETPLACE: PaymentProviderType
PAYMENT_PROVIDER_TYPE_AZURE_MARKETPLACE: PaymentProviderType
PAYMENT_PROVIDER_TYPE_CUSTOM: PaymentProviderType
PAYMENT_INFORMATION_STATUS_UNSPECIFIED: PaymentInformationStatus
PAYMENT_INFORMATION_STATUS_ACTIVE: PaymentInformationStatus
PAYMENT_INFORMATION_STATUS_INACTIVE: PaymentInformationStatus
PAYMENT_INFORMATION_STATUS_PENDING: PaymentInformationStatus
SETUP_INTENT_STATUS_UNSPECIFIED: SetupIntentStatus
SETUP_INTENT_STATUS_REQUIRES_PAYMENT_METHOD: SetupIntentStatus
SETUP_INTENT_STATUS_REQUIRES_CONFIRMATION: SetupIntentStatus
SETUP_INTENT_STATUS_REQUIRES_ACTION: SetupIntentStatus
SETUP_INTENT_STATUS_PROCESSING: SetupIntentStatus
SETUP_INTENT_STATUS_CANCELED: SetupIntentStatus
SETUP_INTENT_STATUS_SUCCEEDED: SetupIntentStatus

class ListPaymentInformationRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListPaymentInformationResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PaymentInformation]
    def __init__(self, items: _Optional[_Iterable[_Union[PaymentInformation, _Mapping]]] = ...) -> None: ...

class GetPaymentInformationRequest(_message.Message):
    __slots__ = ("account_id", "payment_information_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_INFORMATION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    payment_information_id: str
    def __init__(self, account_id: _Optional[str] = ..., payment_information_id: _Optional[str] = ...) -> None: ...

class GetPaymentInformationResponse(_message.Message):
    __slots__ = ("payment_information",)
    PAYMENT_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    payment_information: PaymentInformation
    def __init__(self, payment_information: _Optional[_Union[PaymentInformation, _Mapping]] = ...) -> None: ...

class DeletePaymentInformationRequest(_message.Message):
    __slots__ = ("account_id", "payment_information_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_INFORMATION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    payment_information_id: str
    def __init__(self, account_id: _Optional[str] = ..., payment_information_id: _Optional[str] = ...) -> None: ...

class DeletePaymentInformationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateStripeSessionRequest(_message.Message):
    __slots__ = ("account_id", "redirect_url")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URL_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    redirect_url: str
    def __init__(self, account_id: _Optional[str] = ..., redirect_url: _Optional[str] = ...) -> None: ...

class CreateStripeSessionResponse(_message.Message):
    __slots__ = ("stripe_session",)
    STRIPE_SESSION_FIELD_NUMBER: _ClassVar[int]
    stripe_session: StripeSession
    def __init__(self, stripe_session: _Optional[_Union[StripeSession, _Mapping]] = ...) -> None: ...

class GetStripeSessionRequest(_message.Message):
    __slots__ = ("account_id", "session_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    session_id: str
    def __init__(self, account_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetStripeSessionResponse(_message.Message):
    __slots__ = ("stripe_session",)
    STRIPE_SESSION_FIELD_NUMBER: _ClassVar[int]
    stripe_session: StripeSession
    def __init__(self, stripe_session: _Optional[_Union[StripeSession, _Mapping]] = ...) -> None: ...

class ChangePaymentInformationRequest(_message.Message):
    __slots__ = ("account_id", "new_payment_information_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_PAYMENT_INFORMATION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    new_payment_information_id: str
    def __init__(self, account_id: _Optional[str] = ..., new_payment_information_id: _Optional[str] = ...) -> None: ...

class ChangePaymentInformationResponse(_message.Message):
    __slots__ = ("payment_information",)
    PAYMENT_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    payment_information: PaymentInformation
    def __init__(self, payment_information: _Optional[_Union[PaymentInformation, _Mapping]] = ...) -> None: ...

class StripeSession(_message.Message):
    __slots__ = ("id", "url", "customer", "setup_intent_id", "setup_intent_status", "setup_intent_payment_method")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    SETUP_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    SETUP_INTENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    SETUP_INTENT_PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    customer: str
    setup_intent_id: str
    setup_intent_status: SetupIntentStatus
    setup_intent_payment_method: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., customer: _Optional[str] = ..., setup_intent_id: _Optional[str] = ..., setup_intent_status: _Optional[_Union[SetupIntentStatus, str]] = ..., setup_intent_payment_method: _Optional[str] = ...) -> None: ...

class PaymentInformation(_message.Message):
    __slots__ = ("id", "account_id", "type", "payment_provider_id", "payment_method", "billing_address", "created_at", "last_modified_at", "tax_id", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    TAX_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    type: PaymentProviderType
    payment_provider_id: str
    payment_method: PaymentMethod
    billing_address: BillingAddress
    created_at: _timestamp_pb2.Timestamp
    last_modified_at: _timestamp_pb2.Timestamp
    tax_id: str
    status: PaymentInformationStatus
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., type: _Optional[_Union[PaymentProviderType, str]] = ..., payment_provider_id: _Optional[str] = ..., payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ..., billing_address: _Optional[_Union[BillingAddress, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tax_id: _Optional[str] = ..., status: _Optional[_Union[PaymentInformationStatus, str]] = ...) -> None: ...

class BillingAddress(_message.Message):
    __slots__ = ("name", "line1", "line2", "postal_code", "city", "state", "country", "country_formatted", "state_formatted", "tax_supported_country")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINE1_FIELD_NUMBER: _ClassVar[int]
    LINE2_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FORMATTED_FIELD_NUMBER: _ClassVar[int]
    STATE_FORMATTED_FIELD_NUMBER: _ClassVar[int]
    TAX_SUPPORTED_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    name: str
    line1: str
    line2: str
    postal_code: str
    city: str
    state: str
    country: str
    country_formatted: str
    state_formatted: str
    tax_supported_country: bool
    def __init__(self, name: _Optional[str] = ..., line1: _Optional[str] = ..., line2: _Optional[str] = ..., postal_code: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., country: _Optional[str] = ..., country_formatted: _Optional[str] = ..., state_formatted: _Optional[str] = ..., tax_supported_country: bool = ...) -> None: ...

class PaymentMethod(_message.Message):
    __slots__ = ("id", "card")
    ID_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    card: Card
    def __init__(self, id: _Optional[str] = ..., card: _Optional[_Union[Card, _Mapping]] = ...) -> None: ...

class Card(_message.Message):
    __slots__ = ("brand", "last4", "expiration_month", "expiration_year")
    BRAND_FIELD_NUMBER: _ClassVar[int]
    LAST4_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_MONTH_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_YEAR_FIELD_NUMBER: _ClassVar[int]
    brand: str
    last4: str
    expiration_month: int
    expiration_year: int
    def __init__(self, brand: _Optional[str] = ..., last4: _Optional[str] = ..., expiration_month: _Optional[int] = ..., expiration_year: _Optional[int] = ...) -> None: ...
