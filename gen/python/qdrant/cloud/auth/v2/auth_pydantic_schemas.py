# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from ...common.v1.common_pydantic_schemas import Version
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class GetAPIVersionRequest(BaseModel):#  Empty
    """
     GetAPIVersionRequest is the request for the GetAPIVersion function
    """

class GetAPIVersionResponse(BaseModel):
    """
     GetAPIVersionResponse is the response from the GetAPIVersion function
    """

# The actual version
    version: Version = Field()

class ListApiKeysRequest(BaseModel):
    """
     ListApiKeysRequest is the request for the ListApiKeys function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")# TODO: ListOptions

class ApiKey(BaseModel):
    """
     A ApiKey represents one api-key of a Qdrant cloud account.
 This api-key can grant access to one or more Qdrant databases (clusters)
    """

# Unique identifier for the api-key (in Guid format).
# This is a read-only field and will be available after an api-key is created.
    id: str = Field(default="")
# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Timestamp when the api-key was created.
# This is a read-only field and will be available after an api-key is created.
    created_at: datetime = Field(default_factory=datetime.now)
# A list of cluster IDs
# Should contain at least a single ID.
# After creation, this field cannot be changed. TODO: Changable!
    cluster_ids: typing.List[str] = Field(default_factory=list)
# Prefix for the API key, this represents the first bytes of the token
# This is a read-only field and will be available after an api-key is created.
    prefix: str = Field(default="")
# The token for the API key.
# This is a read-only field and will be available only once in the return of CreateApiKey.
# You should securely store this token and it should be handled as a secret.
    token: str = Field(default="")

class ListApiKeysResponse(BaseModel):
    """
     ListApiKeysResponse is the response from the ListApiKeys function
    """

# The actual api-keys in this list
    items: typing.List[ApiKey] = Field(default_factory=list)# TODO: Add an operation timestamp the ListApiKeys is started, to support the `since` in ListOptions

class CreateApiKeyRequest(BaseModel):
    """
     CreateApiKeyRequest is the request for the CreateApiKey function
    """

# The actual API Key
    api_key: ApiKey = Field()

class CreateApiKeyResponse(BaseModel):
    """
     CreateApiKeyResponse is the response from the CreateApiKey function
    """

# The actual API Key
    api_key: ApiKey = Field()

class DeleteApiKeyRequest(BaseModel):
    """
     DeleteApiKeyRequest is the request for the DeleteApiKey function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the api-key (in Guid format).
# This is a required field.
    api_key_id: str = Field(default="")

class DeleteApiKeyResponse(BaseModel):#  Empty
    """
     DeleteApiKeyResponse is the response from the DeleteApiKey function
    """
