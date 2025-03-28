# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class ListCollectionApiKeysRequest(BaseModel):
    """
     Request all API keys associated with a collection
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Collection the API keys belong to (in Guid format).
# This is a required field.
    collection_id: str = Field(default="")

class CollectionApiKey(BaseModel):
    """
     A CollectionApiKey represents one collection api key of a Qdrant cloud account.
 This collection key can grant access to a Qdrant cloud serverless collection.
    """

# Unique identifier for the collection api key (in Guid format).
# This is a read-only field and will be available after a collection api key is created.
    id: str = Field(default="")
# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Timestamp when the collection api key was created.
# This is a read-only field and will be available after a collection api key is created.
    created_at: datetime = Field(default_factory=datetime.now)
# The identifier of the collection (in Guid format).
# This is a required field.
    collection_id: str = Field(default="")
# Name of the collection api key.
# This is a required field.
# Name can only contain letters, numbers, spaces, underscores and dashes.
    name: str = Field(default="")
# The expiration time of the collection api key. The key will be invalid after this time.
# This field is optional, and if not provided, the key does not expire.
    expires_at: typing.Optional[datetime] = Field(default_factory=datetime.now)
# The type of access granted for the collection.
# - "read-only": Grants access to perform collection-related actions that only read data.
# - "read-write": Grants access to perform collection-related actions that read or write data (like `upsert points`).
# For a detailed list of actions allowed for each access type, see:
# https://qdrant.tech/documentation/guides/security/#table-of-access
# This is a required field.
    access_type: str = Field(default="")
# The email of the user who created the collection api key.
# This is a read-only field and will be available after a collection api key is created.
    created_by_email: str = Field(default="")
# Postfix for the collection api key, this represents the last bytes of the key.
# This is a read-only field and will be available after a collection api key is created.
    postfix: str = Field(default="")
# The key for the collection api key.
# This is a read-only field and will be available only once in the response of CreateCollectionApiKey.
# You should securely store this key and it should be handled as a secret.
    key: str = Field(default="")

class ListCollectionApiKeysResponse(BaseModel):
    """
     Response containing all API keys associated with a collection
    """

# List of API keys for the collection
    items: typing.List[CollectionApiKey] = Field(default_factory=list)

class CreateCollectionApiKeyRequest(BaseModel):
    """
     CreateCollectionApiKeyRequest defines parameters for creating a new collection API key
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Collection the key will access (in Guid format).
# This is a required field.
    collection_id: str = Field(default="")
# The API key to create.
# This is a required field.
    collection_api_key: CollectionApiKey = Field()

class CreateCollectionApiKeyResponse(BaseModel):
    """
     CollectionApiKeyResponse provides the API key after creation
    """

# The newly created API key value
    collection_api_key: CollectionApiKey = Field()

class DeleteCollectionApiKeyRequest(BaseModel):
    """
     DeleteCollectionApiKeyRequest identifies the API key to delete
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Collection the key belongs to (in Guid format).
# This is a required field.
    collection_id: str = Field(default="")
# ID of the key to delete (in Guid format).
# This is a required field.
    collection_api_key_id: str = Field(default="")

class DeleteCollectionApiKeyResponse(BaseModel):#  Empty
    """
     DeleteCollectionApiKeyResponse is an empty response for deletion confirmation
    """
