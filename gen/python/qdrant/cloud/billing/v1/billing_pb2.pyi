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

class InvoiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVOICE_STATUS_UNSPECIFIED: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_DRAFT: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_OPEN: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_VOID: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_PAID: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_UNCOLLECTIBLE: _ClassVar[InvoiceStatus]

class Currency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURRENCY_UNSPECIFIED: _ClassVar[Currency]
    CURRENCY_USD: _ClassVar[Currency]
    CURRENCY_EUR: _ClassVar[Currency]
INVOICE_STATUS_UNSPECIFIED: InvoiceStatus
INVOICE_STATUS_DRAFT: InvoiceStatus
INVOICE_STATUS_OPEN: InvoiceStatus
INVOICE_STATUS_VOID: InvoiceStatus
INVOICE_STATUS_PAID: InvoiceStatus
INVOICE_STATUS_UNCOLLECTIBLE: InvoiceStatus
CURRENCY_UNSPECIFIED: Currency
CURRENCY_USD: Currency
CURRENCY_EUR: Currency

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
    __slots__ = ("name", "percentage", "fixed", "active_from", "active_to")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FROM_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TO_FIELD_NUMBER: _ClassVar[int]
    name: str
    percentage: DiscountPercentage
    fixed: DiscountFixed
    active_from: _timestamp_pb2.Timestamp
    active_to: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., percentage: _Optional[_Union[DiscountPercentage, _Mapping]] = ..., fixed: _Optional[_Union[DiscountFixed, _Mapping]] = ..., active_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., active_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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
    currency: Currency
    def __init__(self, value: _Optional[float] = ..., currency: _Optional[_Union[Currency, str]] = ...) -> None: ...
