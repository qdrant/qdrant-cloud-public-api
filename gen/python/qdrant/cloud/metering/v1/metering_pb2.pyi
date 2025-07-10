import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMonthlyMeteringsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListMonthlyMeteringsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[MonthlyMeteringSummary]
    def __init__(self, items: _Optional[_Iterable[_Union[MonthlyMeteringSummary, _Mapping]]] = ...) -> None: ...

class ListMeteringsRequest(_message.Message):
    __slots__ = ("account_id", "year", "month")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    year: int
    month: int
    def __init__(self, account_id: _Optional[str] = ..., year: _Optional[int] = ..., month: _Optional[int] = ...) -> None: ...

class ListMeteringsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[MeteringItem]
    def __init__(self, items: _Optional[_Iterable[_Union[MeteringItem, _Mapping]]] = ...) -> None: ...

class MonthlyMeteringSummary(_message.Message):
    __slots__ = ("year", "month", "amount_millicents", "currency")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MILLICENTS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: int
    amount_millicents: int
    currency: str
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., amount_millicents: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class MeteringItem(_message.Message):
    __slots__ = ("account_id", "cluster_id", "cluster_name", "start_time", "end_time", "billable_entity_id", "billable_entity_type", "partner", "price_per_hour", "usage_hours", "amount_millicents", "discount_amount_millicents", "discount_amount_percent", "currency")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    BILLABLE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    BILLABLE_ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTNER_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    USAGE_HOURS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MILLICENTS_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNT_MILLICENTS_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    cluster_name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    billable_entity_id: str
    billable_entity_type: str
    partner: str
    price_per_hour: int
    usage_hours: float
    amount_millicents: int
    discount_amount_millicents: int
    discount_amount_percent: float
    currency: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster_name: _Optional[str] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., billable_entity_id: _Optional[str] = ..., billable_entity_type: _Optional[str] = ..., partner: _Optional[str] = ..., price_per_hour: _Optional[int] = ..., usage_hours: _Optional[float] = ..., amount_millicents: _Optional[int] = ..., discount_amount_millicents: _Optional[int] = ..., discount_amount_percent: _Optional[float] = ..., currency: _Optional[str] = ...) -> None: ...
