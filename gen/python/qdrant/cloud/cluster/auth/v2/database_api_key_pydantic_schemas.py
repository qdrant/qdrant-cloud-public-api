# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class ListDatabaseApiKeysRequest(BaseModel):
    """
     ListDatabaseApiKeysRequest is the request for the ListDatabaseApiKeys function.
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")

class DatabaseApiKey(BaseModel):
    """
     A DatabaseApiKey represents one database api key of a Qdrant cloud account.
 This database key can grant access to one or more Qdrant databases (clusters).
    """

# Unique identifier for the database api key (in Guid format).
# This is a read-only field and will be available after a database api key is created.
    id: str = Field(default="")
# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Timestamp when the database api key was created.
# This is a read-only field and will be available after a database api key is created.
    created_at: datetime = Field(default_factory=datetime.now)
# A list of cluster IDs.
# It should contain at least one ID.
# After creation, this field cannot be changed.
    cluster_ids: typing.List[str] = Field(default_factory=list)
# Prefix for the database api key, this represents the first bytes of the key.
# This is a read-only field and will be available after a database api key is created.
    prefix: str = Field(default="")
# The key for the database api key.
# This is a read-only field and will be available only once in the response of CreateDatabaseApiKey.
# You should securely store this key and it should be handled as a secret.
    key: str = Field(default="")

class ListDatabaseApiKeysResponse(BaseModel):
    """
     ListDatabaseApiKeysResponse is the response from the ListDatabaseApiKeys function.
    """

# The actual database api keys in this list.
    items: typing.List[DatabaseApiKey] = Field(default_factory=list)

class CreateDatabaseApiKeyRequest(BaseModel):
    """
     CreateDatabaseApiKeyRequest is the request for the CreateDatabaseApiKey function.
    """

# The actual database api key.
    api_key: DatabaseApiKey = Field()

class CreateDatabaseApiKeyResponse(BaseModel):
    """
     CreateDatabaseApiKeyResponse is the response from the CreateDatabaseApiKey function.
    """

# The actual database api key.
    api_key: DatabaseApiKey = Field()

class DeleteDatabaseApiKeyRequest(BaseModel):
    """
     DeleteDatabaseApiKeyRequest is the request for the DeleteDatabaseApiKey function.
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the database api key (in Guid format).
# This is a required field.
    database_api_key_id: str = Field(default="")

class DeleteDatabaseApiKeyResponse(BaseModel):#  Empty
    """
     DeleteDatabaseApiKeyResponse is the response from the DeleteDatabaseApiKey function.
    """
