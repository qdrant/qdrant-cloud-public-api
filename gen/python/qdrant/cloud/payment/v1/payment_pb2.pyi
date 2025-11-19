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

class PaymentProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAYMENT_PROVIDER_TYPE_UNSPECIFIED: _ClassVar[PaymentProviderType]
    PAYMENT_PROVIDER_TYPE_STRIPE: _ClassVar[PaymentProviderType]
    PAYMENT_PROVIDER_TYPE_AWS_MARKETPLACE: _ClassVar[PaymentProviderType]
    PAYMENT_PROVIDER_TYPE_GCP_MARKETPLACE: _ClassVar[PaymentProviderType]
    PAYMENT_PROVIDER_TYPE_AZURE_MARKETPLACE: _ClassVar[PaymentProviderType]
    PAYMENT_PROVIDER_TYPE_CUSTOM: _ClassVar[PaymentProviderType]

class PaymentMethodStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAYMENT_METHOD_STATUS_UNSPECIFIED: _ClassVar[PaymentMethodStatus]
    PAYMENT_METHOD_STATUS_ACTIVE: _ClassVar[PaymentMethodStatus]
    PAYMENT_METHOD_STATUS_INACTIVE: _ClassVar[PaymentMethodStatus]
    PAYMENT_METHOD_STATUS_PENDING: _ClassVar[PaymentMethodStatus]

class StripeSetupIntentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STRIPE_SETUP_INTENT_STATUS_UNSPECIFIED: _ClassVar[StripeSetupIntentStatus]
    STRIPE_SETUP_INTENT_STATUS_REQUIRES_PAYMENT_METHOD: _ClassVar[StripeSetupIntentStatus]
    STRIPE_SETUP_INTENT_STATUS_REQUIRES_CONFIRMATION: _ClassVar[StripeSetupIntentStatus]
    STRIPE_SETUP_INTENT_STATUS_REQUIRES_ACTION: _ClassVar[StripeSetupIntentStatus]
    STRIPE_SETUP_INTENT_STATUS_PROCESSING: _ClassVar[StripeSetupIntentStatus]
    STRIPE_SETUP_INTENT_STATUS_CANCELED: _ClassVar[StripeSetupIntentStatus]
    STRIPE_SETUP_INTENT_STATUS_SUCCEEDED: _ClassVar[StripeSetupIntentStatus]
PAYMENT_PROVIDER_TYPE_UNSPECIFIED: PaymentProviderType
PAYMENT_PROVIDER_TYPE_STRIPE: PaymentProviderType
PAYMENT_PROVIDER_TYPE_AWS_MARKETPLACE: PaymentProviderType
PAYMENT_PROVIDER_TYPE_GCP_MARKETPLACE: PaymentProviderType
PAYMENT_PROVIDER_TYPE_AZURE_MARKETPLACE: PaymentProviderType
PAYMENT_PROVIDER_TYPE_CUSTOM: PaymentProviderType
PAYMENT_METHOD_STATUS_UNSPECIFIED: PaymentMethodStatus
PAYMENT_METHOD_STATUS_ACTIVE: PaymentMethodStatus
PAYMENT_METHOD_STATUS_INACTIVE: PaymentMethodStatus
PAYMENT_METHOD_STATUS_PENDING: PaymentMethodStatus
STRIPE_SETUP_INTENT_STATUS_UNSPECIFIED: StripeSetupIntentStatus
STRIPE_SETUP_INTENT_STATUS_REQUIRES_PAYMENT_METHOD: StripeSetupIntentStatus
STRIPE_SETUP_INTENT_STATUS_REQUIRES_CONFIRMATION: StripeSetupIntentStatus
STRIPE_SETUP_INTENT_STATUS_REQUIRES_ACTION: StripeSetupIntentStatus
STRIPE_SETUP_INTENT_STATUS_PROCESSING: StripeSetupIntentStatus
STRIPE_SETUP_INTENT_STATUS_CANCELED: StripeSetupIntentStatus
STRIPE_SETUP_INTENT_STATUS_SUCCEEDED: StripeSetupIntentStatus

class ListPaymentMethodsRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListPaymentMethodsResponse(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PaymentMethod]
    def __init__(self, items: _Optional[_Iterable[_Union[PaymentMethod, _Mapping]]] = ...) -> None: ...

class GetPaymentMethodRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    payment_method_id: str
    def __init__(self, account_id: _Optional[str] = ..., payment_method_id: _Optional[str] = ...) -> None: ...

class GetPaymentMethodResponse(_message.Message):
    __slots__ = ()
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class CreatePaymentMethodRequest(_message.Message):
    __slots__ = ()
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class CreatePaymentMethodResponse(_message.Message):
    __slots__ = ()
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class UpdatePaymentMethodRequest(_message.Message):
    __slots__ = ()
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class UpdatePaymentMethodResponse(_message.Message):
    __slots__ = ()
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class DeletePaymentMethodRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    payment_method_id: str
    def __init__(self, account_id: _Optional[str] = ..., payment_method_id: _Optional[str] = ...) -> None: ...

class DeletePaymentMethodResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStripeCheckoutSessionRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    session_id: str
    def __init__(self, account_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetStripeCheckoutSessionResponse(_message.Message):
    __slots__ = ()
    STRIPE_SESSION_FIELD_NUMBER: _ClassVar[int]
    stripe_session: StripeCheckoutSession
    def __init__(self, stripe_session: _Optional[_Union[StripeCheckoutSession, _Mapping]] = ...) -> None: ...

class CreateStripeCheckoutSessionRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URL_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    redirect_url: str
    def __init__(self, account_id: _Optional[str] = ..., redirect_url: _Optional[str] = ...) -> None: ...

class CreateStripeCheckoutSessionResponse(_message.Message):
    __slots__ = ()
    STRIPE_SESSION_FIELD_NUMBER: _ClassVar[int]
    stripe_session: StripeCheckoutSession
    def __init__(self, stripe_session: _Optional[_Union[StripeCheckoutSession, _Mapping]] = ...) -> None: ...

class StripeCheckoutSession(_message.Message):
    __slots__ = ()
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
    setup_intent_status: StripeSetupIntentStatus
    setup_intent_payment_method: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., customer: _Optional[str] = ..., setup_intent_id: _Optional[str] = ..., setup_intent_status: _Optional[_Union[StripeSetupIntentStatus, str]] = ..., setup_intent_payment_method: _Optional[str] = ...) -> None: ...

class PaymentMethod(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    TAX_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    type: PaymentProviderType
    payment_provider_id: str
    payment_method_details: PaymentMethodDetails
    billing_address: BillingAddress
    created_at: _timestamp_pb2.Timestamp
    last_modified_at: _timestamp_pb2.Timestamp
    tax_id: str
    is_default: bool
    status: PaymentMethodStatus
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., type: _Optional[_Union[PaymentProviderType, str]] = ..., payment_provider_id: _Optional[str] = ..., payment_method_details: _Optional[_Union[PaymentMethodDetails, _Mapping]] = ..., billing_address: _Optional[_Union[BillingAddress, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tax_id: _Optional[str] = ..., is_default: _Optional[bool] = ..., status: _Optional[_Union[PaymentMethodStatus, str]] = ...) -> None: ...

class RecordCloudMarketplaceEntitlementRequest(_message.Message):
    __slots__ = ()
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    entitlement_id: str
    def __init__(self, account_id: _Optional[str] = ..., entitlement_id: _Optional[str] = ...) -> None: ...

class RecordCloudMarketplaceEntitlementResponse(_message.Message):
    __slots__ = ()
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class BillingAddress(_message.Message):
    __slots__ = ()
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
    def __init__(self, name: _Optional[str] = ..., line1: _Optional[str] = ..., line2: _Optional[str] = ..., postal_code: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., country: _Optional[str] = ..., country_formatted: _Optional[str] = ..., state_formatted: _Optional[str] = ..., tax_supported_country: _Optional[bool] = ...) -> None: ...

class PaymentMethodDetails(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    card: Card
    def __init__(self, id: _Optional[str] = ..., card: _Optional[_Union[Card, _Mapping]] = ...) -> None: ...

class Card(_message.Message):
    __slots__ = ()
    BRAND_FIELD_NUMBER: _ClassVar[int]
    LAST4_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_MONTH_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_YEAR_FIELD_NUMBER: _ClassVar[int]
    brand: str
    last4: str
    expiration_month: int
    expiration_year: int
    def __init__(self, brand: _Optional[str] = ..., last4: _Optional[str] = ..., expiration_month: _Optional[int] = ..., expiration_year: _Optional[int] = ...) -> None: ...
