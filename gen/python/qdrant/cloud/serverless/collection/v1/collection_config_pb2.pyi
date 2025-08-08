from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DistanceMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISTANCE_METRIC_UNSPECIFIED: _ClassVar[DistanceMetric]
    DISTANCE_METRIC_COSINE: _ClassVar[DistanceMetric]
    DISTANCE_METRIC_EUCLID: _ClassVar[DistanceMetric]
    DISTANCE_METRIC_DOT: _ClassVar[DistanceMetric]
    DISTANCE_METRIC_MANHATTAN: _ClassVar[DistanceMetric]

class StorageTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORAGE_TIER_UNSPECIFIED: _ClassVar[StorageTier]
    STORAGE_TIER_STORAGE: _ClassVar[StorageTier]
    STORAGE_TIER_BALANCED: _ClassVar[StorageTier]
    STORAGE_TIER_PERFORMANCE: _ClassVar[StorageTier]

class PrecisionTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRECISION_TIER_UNSPECIFIED: _ClassVar[PrecisionTier]
    PRECISION_TIER_LOW: _ClassVar[PrecisionTier]
    PRECISION_TIER_MEDIUM: _ClassVar[PrecisionTier]
    PRECISION_TIER_HIGH: _ClassVar[PrecisionTier]

class VectorModifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VECTOR_MODIFIER_UNSPECIFIED: _ClassVar[VectorModifier]
    VECTOR_MODIFIER_NONE: _ClassVar[VectorModifier]
    VECTOR_MODIFIER_IDF: _ClassVar[VectorModifier]

class Tokenizer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOKENIZER_UNSPECIFIED: _ClassVar[Tokenizer]
    TOKENIZER_PREFIX: _ClassVar[Tokenizer]
    TOKENIZER_WHITESPACE: _ClassVar[Tokenizer]
    TOKENIZER_WORD: _ClassVar[Tokenizer]
    TOKENIZER_MULTILINGUAL: _ClassVar[Tokenizer]
DISTANCE_METRIC_UNSPECIFIED: DistanceMetric
DISTANCE_METRIC_COSINE: DistanceMetric
DISTANCE_METRIC_EUCLID: DistanceMetric
DISTANCE_METRIC_DOT: DistanceMetric
DISTANCE_METRIC_MANHATTAN: DistanceMetric
STORAGE_TIER_UNSPECIFIED: StorageTier
STORAGE_TIER_STORAGE: StorageTier
STORAGE_TIER_BALANCED: StorageTier
STORAGE_TIER_PERFORMANCE: StorageTier
PRECISION_TIER_UNSPECIFIED: PrecisionTier
PRECISION_TIER_LOW: PrecisionTier
PRECISION_TIER_MEDIUM: PrecisionTier
PRECISION_TIER_HIGH: PrecisionTier
VECTOR_MODIFIER_UNSPECIFIED: VectorModifier
VECTOR_MODIFIER_NONE: VectorModifier
VECTOR_MODIFIER_IDF: VectorModifier
TOKENIZER_UNSPECIFIED: Tokenizer
TOKENIZER_PREFIX: Tokenizer
TOKENIZER_WHITESPACE: Tokenizer
TOKENIZER_WORD: Tokenizer
TOKENIZER_MULTILINGUAL: Tokenizer

class CollectionConfiguration(_message.Message):
    __slots__ = ("tenant_key", "dense_vectors", "sparse_vectors", "payload_schema")
    class DenseVectorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DenseVectorConfiguration
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DenseVectorConfiguration, _Mapping]] = ...) -> None: ...
    class SparseVectorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SparseVectorConfiguration
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SparseVectorConfiguration, _Mapping]] = ...) -> None: ...
    class PayloadSchemaEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PayloadFieldSchema
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PayloadFieldSchema, _Mapping]] = ...) -> None: ...
    TENANT_KEY_FIELD_NUMBER: _ClassVar[int]
    DENSE_VECTORS_FIELD_NUMBER: _ClassVar[int]
    SPARSE_VECTORS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    tenant_key: str
    dense_vectors: _containers.MessageMap[str, DenseVectorConfiguration]
    sparse_vectors: _containers.MessageMap[str, SparseVectorConfiguration]
    payload_schema: _containers.MessageMap[str, PayloadFieldSchema]
    def __init__(self, tenant_key: _Optional[str] = ..., dense_vectors: _Optional[_Mapping[str, DenseVectorConfiguration]] = ..., sparse_vectors: _Optional[_Mapping[str, SparseVectorConfiguration]] = ..., payload_schema: _Optional[_Mapping[str, PayloadFieldSchema]] = ...) -> None: ...

class DenseVectorConfiguration(_message.Message):
    __slots__ = ("dimension", "distance", "multivector", "rescoring", "storage_tier", "precision_tier")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    MULTIVECTOR_FIELD_NUMBER: _ClassVar[int]
    RESCORING_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TIER_FIELD_NUMBER: _ClassVar[int]
    PRECISION_TIER_FIELD_NUMBER: _ClassVar[int]
    dimension: int
    distance: DistanceMetric
    multivector: bool
    rescoring: bool
    storage_tier: StorageTier
    precision_tier: PrecisionTier
    def __init__(self, dimension: _Optional[int] = ..., distance: _Optional[_Union[DistanceMetric, str]] = ..., multivector: bool = ..., rescoring: bool = ..., storage_tier: _Optional[_Union[StorageTier, str]] = ..., precision_tier: _Optional[_Union[PrecisionTier, str]] = ...) -> None: ...

class SparseVectorConfiguration(_message.Message):
    __slots__ = ("precision_tier", "modifier")
    PRECISION_TIER_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_FIELD_NUMBER: _ClassVar[int]
    precision_tier: PrecisionTier
    modifier: VectorModifier
    def __init__(self, precision_tier: _Optional[_Union[PrecisionTier, str]] = ..., modifier: _Optional[_Union[VectorModifier, str]] = ...) -> None: ...

class KeywordIndexParams(_message.Message):
    __slots__ = ("is_tenant", "on_disk")
    IS_TENANT_FIELD_NUMBER: _ClassVar[int]
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    is_tenant: bool
    on_disk: bool
    def __init__(self, is_tenant: bool = ..., on_disk: bool = ...) -> None: ...

class IntegerIndexParams(_message.Message):
    __slots__ = ("lookup", "range", "is_principal", "on_disk")
    LOOKUP_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    IS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    lookup: bool
    range: bool
    is_principal: bool
    on_disk: bool
    def __init__(self, lookup: bool = ..., range: bool = ..., is_principal: bool = ..., on_disk: bool = ...) -> None: ...

class FloatIndexParams(_message.Message):
    __slots__ = ("is_principal", "on_disk")
    IS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    is_principal: bool
    on_disk: bool
    def __init__(self, is_principal: bool = ..., on_disk: bool = ...) -> None: ...

class GeoIndexParams(_message.Message):
    __slots__ = ("on_disk",)
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    on_disk: bool
    def __init__(self, on_disk: bool = ...) -> None: ...

class TextIndexParams(_message.Message):
    __slots__ = ("tokenizer", "min_token_len", "max_token_len", "lowercase", "on_disk")
    TOKENIZER_FIELD_NUMBER: _ClassVar[int]
    MIN_TOKEN_LEN_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKEN_LEN_FIELD_NUMBER: _ClassVar[int]
    LOWERCASE_FIELD_NUMBER: _ClassVar[int]
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    tokenizer: Tokenizer
    min_token_len: int
    max_token_len: int
    lowercase: bool
    on_disk: bool
    def __init__(self, tokenizer: _Optional[_Union[Tokenizer, str]] = ..., min_token_len: _Optional[int] = ..., max_token_len: _Optional[int] = ..., lowercase: bool = ..., on_disk: bool = ...) -> None: ...

class BoolIndexParams(_message.Message):
    __slots__ = ("on_disk",)
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    on_disk: bool
    def __init__(self, on_disk: bool = ...) -> None: ...

class DatetimeIndexParams(_message.Message):
    __slots__ = ("is_principal", "on_disk")
    IS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    is_principal: bool
    on_disk: bool
    def __init__(self, is_principal: bool = ..., on_disk: bool = ...) -> None: ...

class UuidIndexParams(_message.Message):
    __slots__ = ("is_tenant", "on_disk")
    IS_TENANT_FIELD_NUMBER: _ClassVar[int]
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    is_tenant: bool
    on_disk: bool
    def __init__(self, is_tenant: bool = ..., on_disk: bool = ...) -> None: ...

class PayloadFieldSchema(_message.Message):
    __slots__ = ("keyword", "integer", "float", "geo", "text", "bool", "datetime", "uuid")
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    INTEGER_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    GEO_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    keyword: KeywordIndexParams
    integer: IntegerIndexParams
    float: FloatIndexParams
    geo: GeoIndexParams
    text: TextIndexParams
    bool: BoolIndexParams
    datetime: DatetimeIndexParams
    uuid: UuidIndexParams
    def __init__(self, keyword: _Optional[_Union[KeywordIndexParams, _Mapping]] = ..., integer: _Optional[_Union[IntegerIndexParams, _Mapping]] = ..., float: _Optional[_Union[FloatIndexParams, _Mapping]] = ..., geo: _Optional[_Union[GeoIndexParams, _Mapping]] = ..., text: _Optional[_Union[TextIndexParams, _Mapping]] = ..., bool: _Optional[_Union[BoolIndexParams, _Mapping]] = ..., datetime: _Optional[_Union[DatetimeIndexParams, _Mapping]] = ..., uuid: _Optional[_Union[UuidIndexParams, _Mapping]] = ...) -> None: ...
