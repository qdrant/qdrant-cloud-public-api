# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator
import typing


class CollectionConfiguration(BaseModel):
    """
     CollectionConfiguration defines the structure and settings for a collection
    """

# Field name used for tenant isolation
    tenant_key: typing.Optional[str] = Field(default="")
# Map of dense vector configurations with field name as key
    dense_vectors: typing.Dict[str, DenseVectorConfiguration] = Field(default_factory=dict)
# Map of sparse vector configurations with field name as key
    sparse_vectors: typing.Dict[str, SparseVectorConfiguration] = Field(default_factory=dict)
# Schema definition for payload fields
    payload_schema: typing.Dict[str, PayloadFieldSchema] = Field(default_factory=dict)

class DenseVectorConfiguration(BaseModel):
    """
     DenseVectorConfiguration defines the settings for dense vector fields
    """

# The dimensionality of the vector space
    dimension: int = Field(default=0)
# The distance metric used for vector similarity calculations
    distance: str = Field(default="")
# Whether to use multi-vector storage for this configuration
    multivector: typing.Optional[bool] = Field(default=False)
# Whether to enable rescoring for search results
    rescoring: typing.Optional[bool] = Field(default=False)
# The storage performance tier to use (STORAGE, BALANCED, or PERFORMANCE)
    storage_tier: typing.Optional[str] = Field(default="")
# The precision level for vector operations (LOW, MEDIUM, or HIGH)
    precision_tier: typing.Optional[str] = Field(default="")

class SparseVectorConfiguration(BaseModel):
    """
     SparseVectorConfiguration defines the settings for sparse vector fields
    """

# Precision tier for vector operations
    precision_tier: str = Field(default="")
# Vector value modification approach
    modifier: str = Field(default="")

class KeywordIndexParams(BaseModel):
    """
     KeywordIndexParams defines parameters for keyword indexing
    """

# Whether this field is used as tenant identifier
    is_tenant: typing.Optional[bool] = Field(default=False)
# Whether to store index on disk vs memory
    on_disk: typing.Optional[bool] = Field(default=False)

class IntegerIndexParams(BaseModel):
    """
     IntegerIndexParams defines parameters for integer indexing
    """

# Enable lookup operations
    lookup: typing.Optional[bool] = Field(default=False)
# Enable range queries
    range: typing.Optional[bool] = Field(default=False)
# Whether this is a principal field
    is_principal: typing.Optional[bool] = Field(default=False)
# Whether to store index on disk vs memory
    on_disk: typing.Optional[bool] = Field(default=False)

class FloatIndexParams(BaseModel):
    """
     FloatIndexParams defines parameters for float indexing
    """

# Whether this is a principal field
    is_principal: typing.Optional[bool] = Field(default=False)
# Whether to store index on disk vs memory
    on_disk: typing.Optional[bool] = Field(default=False)

class GeoIndexParams(BaseModel):
    """
     GeoIndexParams defines parameters for geographical indexing
    """

# Whether to store index on disk vs memory
    on_disk: typing.Optional[bool] = Field(default=False)

class TextIndexParams(BaseModel):
    """
     TextIndexParams defines parameters for text indexing
    """

# Tokenization strategy
    tokenizer: typing.Optional[str] = Field(default="")
# Minimum token length to index
    min_token_len: typing.Optional[int] = Field(default=0)
# Maximum token length to index
    max_token_len: typing.Optional[int] = Field(default=0)
# Whether to lowercase text before indexing
    lowercase: typing.Optional[bool] = Field(default=False)
# Whether to store index on disk vs memory
    on_disk: typing.Optional[bool] = Field(default=False)

class BoolIndexParams(BaseModel):
    """
     BoolIndexParams defines parameters for boolean indexing
    """

# Whether to store index on disk vs memory
    on_disk: typing.Optional[bool] = Field(default=False)

class DatetimeIndexParams(BaseModel):
    """
     DatetimeIndexParams defines parameters for datetime indexing
    """

# Whether this is a principal field
    is_principal: typing.Optional[bool] = Field(default=False)
# Whether to store index on disk vs memory
    on_disk: typing.Optional[bool] = Field(default=False)

class UuidIndexParams(BaseModel):
    """
     UuidIndexParams defines parameters for UUID indexing
    """

# Whether this field is used as tenant identifier
    is_tenant: typing.Optional[bool] = Field(default=False)
# Whether to store index on disk vs memory
    on_disk: typing.Optional[bool] = Field(default=False)

class PayloadFieldSchema(BaseModel):
    """
     Describes the schema for a payload field
    """

    _one_of_dict = {"PayloadFieldSchema.index_params": {"fields": {"bool", "datetime", "float", "geo", "integer", "keyword", "text", "uuid"}}}
    one_of_validator = model_validator(mode="before")(check_one_of)
# Keyword index parameters
    keyword: KeywordIndexParams = Field()
# Integer index parameters
    integer: IntegerIndexParams = Field()
# Float index parameters
    float: FloatIndexParams = Field()
# Geo Index parameters
    geo: GeoIndexParams = Field()
# Text index parameters
    text: TextIndexParams = Field()
# Boolean index parameters
    bool: BoolIndexParams = Field()
# Datetime index parameters
    datetime: DatetimeIndexParams = Field()
# UUID index parameters
    uuid: UuidIndexParams = Field()
