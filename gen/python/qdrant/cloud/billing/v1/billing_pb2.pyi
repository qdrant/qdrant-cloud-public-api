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

class BillingFrequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BILLING_FREQUENCY_UNSPECIFIED: _ClassVar[BillingFrequency]
    BILLING_FREQUENCY_MONTHLY: _ClassVar[BillingFrequency]
    BILLING_FREQUENCY_QUARTERLY: _ClassVar[BillingFrequency]
    BILLING_FREQUENCY_SEMI_ANNUAL: _ClassVar[BillingFrequency]
    BILLING_FREQUENCY_ANNUAL: _ClassVar[BillingFrequency]

class InvoiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVOICE_STATUS_UNSPECIFIED: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_DRAFT: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_OPEN: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_VOID: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_PAID: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_UNCOLLECTIBLE: _ClassVar[InvoiceStatus]
BILLING_FREQUENCY_UNSPECIFIED: BillingFrequency
BILLING_FREQUENCY_MONTHLY: BillingFrequency
BILLING_FREQUENCY_QUARTERLY: BillingFrequency
BILLING_FREQUENCY_SEMI_ANNUAL: BillingFrequency
BILLING_FREQUENCY_ANNUAL: BillingFrequency
INVOICE_STATUS_UNSPECIFIED: InvoiceStatus
INVOICE_STATUS_DRAFT: InvoiceStatus
INVOICE_STATUS_OPEN: InvoiceStatus
INVOICE_STATUS_VOID: InvoiceStatus
INVOICE_STATUS_PAID: InvoiceStatus
INVOICE_STATUS_UNCOLLECTIBLE: InvoiceStatus

class ListInvoicesRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListInvoicesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Invoice]
    def __init__(self, items: _Optional[_Iterable[_Union[Invoice, _Mapping]]] = ...) -> None: ...

class ListDiscountsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListDiscountsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Discount]
    def __init__(self, items: _Optional[_Iterable[_Union[Discount, _Mapping]]] = ...) -> None: ...

class Invoice(_message.Message):
    __slots__ = ("id", "number", "total_amount", "created_at", "status", "pdf_url")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PDF_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    number: str
    total_amount: int
    created_at: _timestamp_pb2.Timestamp
    status: InvoiceStatus
    pdf_url: str
    def __init__(self, id: _Optional[str] = ..., number: _Optional[str] = ..., total_amount: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[InvoiceStatus, str]] = ..., pdf_url: _Optional[str] = ...) -> None: ...

class Discount(_message.Message):
    __slots__ = ("name", "percentage", "fixed", "valid_from", "valid_until")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    percentage: DiscountPercentage
    fixed: DiscountFixed
    valid_from: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., percentage: _Optional[_Union[DiscountPercentage, _Mapping]] = ..., fixed: _Optional[_Union[DiscountFixed, _Mapping]] = ..., valid_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DiscountPercentage(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class DiscountFixed(_message.Message):
    __slots__ = ("value", "currency")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    value: float
    currency: str
    def __init__(self, value: _Optional[float] = ..., currency: _Optional[str] = ...) -> None: ...

class ListCreditContractsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListCreditContractsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CreditContract]
    def __init__(self, items: _Optional[_Iterable[_Union[CreditContract, _Mapping]]] = ...) -> None: ...

class ListCreditContractConsumptionsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListCreditContractConsumptionsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CreditContractConsumption]
    def __init__(self, items: _Optional[_Iterable[_Union[CreditContractConsumption, _Mapping]]] = ...) -> None: ...

class CreditContractConsumption(_message.Message):
    __slots__ = ("credit_contract_id", "total_amount", "used_amount", "remaining_amount", "currency")
    CREDIT_CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    USED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    REMAINING_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    credit_contract_id: str
    total_amount: float
    used_amount: float
    remaining_amount: float
    currency: str
    def __init__(self, credit_contract_id: _Optional[str] = ..., total_amount: _Optional[float] = ..., used_amount: _Optional[float] = ..., remaining_amount: _Optional[float] = ..., currency: _Optional[str] = ...) -> None: ...

class CreditContract(_message.Message):
    __slots__ = ("id", "account_id", "total_amount", "currency", "billing_frequency", "active_from", "active_to", "notes")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    BILLING_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FROM_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TO_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    total_amount: float
    currency: str
    billing_frequency: BillingFrequency
    active_from: _timestamp_pb2.Timestamp
    active_to: _timestamp_pb2.Timestamp
    notes: str
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., total_amount: _Optional[float] = ..., currency: _Optional[str] = ..., billing_frequency: _Optional[_Union[BillingFrequency, str]] = ..., active_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., active_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ...) -> None: ...

class GetBillingAccountParentRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class GetBillingAccountParentResponse(_message.Message):
    __slots__ = ("parent_account_id",)
    PARENT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    parent_account_id: str
    def __init__(self, parent_account_id: _Optional[str] = ...) -> None: ...

class ListBillingAccountChildrenRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListBillingAccountChildrenResponse(_message.Message):
    __slots__ = ("child_account_ids",)
    CHILD_ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    child_account_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, child_account_ids: _Optional[_Iterable[str]] = ...) -> None: ...
