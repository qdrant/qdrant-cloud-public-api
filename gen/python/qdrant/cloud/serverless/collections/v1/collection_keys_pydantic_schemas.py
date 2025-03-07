# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator
import typing


class ListCollectionKeysRequest(BaseModel):
    """
     Request all api-keys associated with a collection
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Collection the keys belong to
    collection_id: str = Field(default="")

class ApiKey(BaseModel):
    """
     An ApiKey represents a JWT token to access a Qdrant cloud serverless collection.
    """

    _one_of_dict = {"ApiKey.access_type": {"fields": {"access"}}}
    one_of_validator = model_validator(mode="before")(check_one_of)
# Unique identifier for the API key
    id: str = Field(default="")
# Human-readable name for the API key
    name: str = Field(default="")
# The api key itself.
# This is a read-only field and will be available only once in the return of CreateCollectionKey.
# You should securely store this token, and it should be handled as a secret.
    key: str = Field(default="")
# Postfix for the collection api key, this represents the last bytes of the key.
# This is a read-only field and will be available after a collection api key is created.
    postfix: str = Field(default="")
# Timestamp when the collection api key was created.
# This is a read-only field and will be available after a collection api key is created.
    created_at: datetime = Field(default_factory=datetime.now)
# The email of the user who created the collection api key.
# This is a read-only field and will be available after a collection api key is created.
    created_by_email: str = Field(default="")
# A general access level claim, either "r" (read) or "w" (write).
    access: str = Field(default="")
# The expiration time of the collection api key in seconds since the Unix epoch.
    exp: typing.Optional[int] = Field(default=0)
# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the collection (in Guid format).
# This is a required field.
    collection_id: str = Field(default="")

class ListCollectionKeysResponse(BaseModel):
    """
     Response containing all api-keys associated with a collection
    """

# List of API keys for the collection
    keys: typing.List[ApiKey] = Field(default_factory=list)

class CreateCollectionKeyRequest(BaseModel):
    """
     CreateCollectionKeyRequest defines parameters for creating a new API key
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Collection the key will access
    collection_id: str = Field(default="")
# The API key to create
    api_key: ApiKey = Field()

class CreateCollectionKeyResponse(BaseModel):
    """
     CollectionKeyResponse provides the API key after creation
    """

# The newly created API key value
    api_key: ApiKey = Field()

class DeleteCollectionKeyRequest(BaseModel):
    """
     DeleteCollectionKeyRequest identifies the API key to delete
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Collection the key belongs to
    collection_id: str = Field(default="")
# ID of the key to delete
    key_id: str = Field(default="")

class DeleteCollectionKeyResponse(BaseModel):#  Empty
    """
     DeleteCollectionKeyResponse is an empty response for deletion confirmation
    """
