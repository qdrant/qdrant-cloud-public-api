from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Distance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISTANCE_UNSPECIFIED: _ClassVar[Distance]
    COSINE: _ClassVar[Distance]
    EUCLID: _ClassVar[Distance]
    DOT: _ClassVar[Distance]
    MANHATTAN: _ClassVar[Distance]

class PrecisionTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRECISION_TIER_UNSPECIFIED: _ClassVar[PrecisionTier]
    LOW: _ClassVar[PrecisionTier]
    MEDIUM: _ClassVar[PrecisionTier]
    HIGH: _ClassVar[PrecisionTier]

class Tokenizer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOKENIZER_UNSPECIFIED: _ClassVar[Tokenizer]
    PREFIX: _ClassVar[Tokenizer]
    WHITESPACE: _ClassVar[Tokenizer]
    WORD: _ClassVar[Tokenizer]
    MULTILINGUAL: _ClassVar[Tokenizer]
DISTANCE_UNSPECIFIED: Distance
COSINE: Distance
EUCLID: Distance
DOT: Distance
MANHATTAN: Distance
PRECISION_TIER_UNSPECIFIED: PrecisionTier
LOW: PrecisionTier
MEDIUM: PrecisionTier
HIGH: PrecisionTier
TOKENIZER_UNSPECIFIED: Tokenizer
PREFIX: Tokenizer
WHITESPACE: Tokenizer
WORD: Tokenizer
MULTILINGUAL: Tokenizer

class DenseVectorConfig(_message.Message):
    __slots__ = ("size", "distance", "multivector", "precision_tier")
    SIZE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    MULTIVECTOR_FIELD_NUMBER: _ClassVar[int]
    PRECISION_TIER_FIELD_NUMBER: _ClassVar[int]
    size: int
    distance: Distance
    multivector: bool
    precision_tier: PrecisionTier
    def __init__(self, size: _Optional[int] = ..., distance: _Optional[_Union[Distance, str]] = ..., multivector: _Optional[bool] = ..., precision_tier: _Optional[_Union[PrecisionTier, str]] = ...) -> None: ...

class SparseVectorConfig(_message.Message):
    __slots__ = ("use_idf", "precision_tier")
    USE_IDF_FIELD_NUMBER: _ClassVar[int]
    PRECISION_TIER_FIELD_NUMBER: _ClassVar[int]
    use_idf: bool
    precision_tier: PrecisionTier
    def __init__(self, use_idf: _Optional[bool] = ..., precision_tier: _Optional[_Union[PrecisionTier, str]] = ...) -> None: ...

class KeywordIndex(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntegerIndex(_message.Message):
    __slots__ = ("lookup", "range")
    LOOKUP_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    lookup: bool
    range: bool
    def __init__(self, lookup: _Optional[bool] = ..., range: _Optional[bool] = ...) -> None: ...

class FloatIndex(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UuidIndex(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DatetimeIndex(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TextIndex(_message.Message):
    __slots__ = ("tokenizer", "lowercase", "phrase_matching", "min_token_len", "max_token_len")
    TOKENIZER_FIELD_NUMBER: _ClassVar[int]
    LOWERCASE_FIELD_NUMBER: _ClassVar[int]
    PHRASE_MATCHING_FIELD_NUMBER: _ClassVar[int]
    MIN_TOKEN_LEN_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKEN_LEN_FIELD_NUMBER: _ClassVar[int]
    tokenizer: Tokenizer
    lowercase: bool
    phrase_matching: bool
    min_token_len: int
    max_token_len: int
    def __init__(self, tokenizer: _Optional[_Union[Tokenizer, str]] = ..., lowercase: _Optional[bool] = ..., phrase_matching: _Optional[bool] = ..., min_token_len: _Optional[int] = ..., max_token_len: _Optional[int] = ...) -> None: ...

class GeoIndex(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BoolIndex(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PayloadIndexConfig(_message.Message):
    __slots__ = ("keyword", "integer", "float", "uuid", "datetime", "text", "geo", "bool")
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    INTEGER_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    GEO_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    keyword: KeywordIndex
    integer: IntegerIndex
    float: FloatIndex
    uuid: UuidIndex
    datetime: DatetimeIndex
    text: TextIndex
    geo: GeoIndex
    bool: BoolIndex
    def __init__(self, keyword: _Optional[_Union[KeywordIndex, _Mapping]] = ..., integer: _Optional[_Union[IntegerIndex, _Mapping]] = ..., float: _Optional[_Union[FloatIndex, _Mapping]] = ..., uuid: _Optional[_Union[UuidIndex, _Mapping]] = ..., datetime: _Optional[_Union[DatetimeIndex, _Mapping]] = ..., text: _Optional[_Union[TextIndex, _Mapping]] = ..., geo: _Optional[_Union[GeoIndex, _Mapping]] = ..., bool: _Optional[_Union[BoolIndex, _Mapping]] = ...) -> None: ...

class CollectionConfig(_message.Message):
    __slots__ = ("dense_vectors", "sparse_vectors", "payload_indexes")
    class DenseVectorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DenseVectorConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DenseVectorConfig, _Mapping]] = ...) -> None: ...
    class SparseVectorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SparseVectorConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SparseVectorConfig, _Mapping]] = ...) -> None: ...
    class PayloadIndexesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PayloadIndexConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PayloadIndexConfig, _Mapping]] = ...) -> None: ...
    DENSE_VECTORS_FIELD_NUMBER: _ClassVar[int]
    SPARSE_VECTORS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_INDEXES_FIELD_NUMBER: _ClassVar[int]
    dense_vectors: _containers.MessageMap[str, DenseVectorConfig]
    sparse_vectors: _containers.MessageMap[str, SparseVectorConfig]
    payload_indexes: _containers.MessageMap[str, PayloadIndexConfig]
    def __init__(self, dense_vectors: _Optional[_Mapping[str, DenseVectorConfig]] = ..., sparse_vectors: _Optional[_Mapping[str, SparseVectorConfig]] = ..., payload_indexes: _Optional[_Mapping[str, PayloadIndexConfig]] = ...) -> None: ...

class CreateCollectionRequest(_message.Message):
    __slots__ = ("collection_name", "config")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    config: CollectionConfig
    def __init__(self, collection_name: _Optional[str] = ..., config: _Optional[_Union[CollectionConfig, _Mapping]] = ...) -> None: ...

class CreateCollectionResponse(_message.Message):
    __slots__ = ("collection_name", "result")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    result: str
    def __init__(self, collection_name: _Optional[str] = ..., result: _Optional[str] = ...) -> None: ...

class DeleteCollectionRequest(_message.Message):
    __slots__ = ("collection_name",)
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    def __init__(self, collection_name: _Optional[str] = ...) -> None: ...

class DeleteCollectionResponse(_message.Message):
    __slots__ = ("deleted", "objects_deleted")
    DELETED_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    objects_deleted: int
    def __init__(self, deleted: _Optional[bool] = ..., objects_deleted: _Optional[int] = ...) -> None: ...

class GetCollectionRequest(_message.Message):
    __slots__ = ("collection_name",)
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    def __init__(self, collection_name: _Optional[str] = ...) -> None: ...

class GetCollectionResponse(_message.Message):
    __slots__ = ("exists", "config", "point_count")
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    config: CollectionConfig
    point_count: int
    def __init__(self, exists: _Optional[bool] = ..., config: _Optional[_Union[CollectionConfig, _Mapping]] = ..., point_count: _Optional[int] = ...) -> None: ...

class ListCollectionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CollectionSummary(_message.Message):
    __slots__ = ("collection_name", "point_count")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    point_count: int
    def __init__(self, collection_name: _Optional[str] = ..., point_count: _Optional[int] = ...) -> None: ...

class ListCollectionsResponse(_message.Message):
    __slots__ = ("collections",)
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedCompositeFieldContainer[CollectionSummary]
    def __init__(self, collections: _Optional[_Iterable[_Union[CollectionSummary, _Mapping]]] = ...) -> None: ...
