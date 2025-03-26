# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class ListManagementKeysRequest(BaseModel):
    """
     ListManagementKeysRequest is the request for the ListManagementKeys function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")

class ManagementKey(BaseModel):
    """
     A ManagementKey represents a management key of a Qdrant Cloud account.
 This management key grants access to the Qdrant Cloud API.
    """

# Unique identifier for the management key (in Guid format).
# This is a read-only field and will be available after a management key is created.
    id: str = Field(default="")
# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Timestamp when the management key was created.
# This is a read-only field and will be available after a management key is created.
    created_at: datetime = Field(default_factory=datetime.now)
# Prefix for the management key, this represents the first bytes of the key.
# This is a read-only field and will be available after a management key is created.
    prefix: str = Field(default="")
# The value of the key, to be used to authenticate requests to the Qdrant Cloud API.
# This is a read-only field and will be available only once in the response of CreateManagementKey.
# You should securely store this key and it should be handled as a secret.
    key: str = Field(default="")

class ListManagementKeysResponse(BaseModel):
    """
     ListManagementKeysResponse is the response from the ListManagementKeys function
    """

# The actual management keys in this list.
    items: typing.List[ManagementKey] = Field(default_factory=list)

class CreateManagementKeyRequest(BaseModel):
    """
     CreateManagementKeyRequest is the request for the CreateManagementKey function
    """

# The actual management key.
    management_key: ManagementKey = Field()

class CreateManagementKeyResponse(BaseModel):
    """
     CreateManagementKeyResponse is the response from the CreateManagementKey function
    """

# The actual management key.
    management_key: ManagementKey = Field()

class DeleteManagementKeyRequest(BaseModel):
    """
     DeleteManagementKeyRequest is the request for the DeleteManagementKey function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the management key (in Guid format).
# This is a required field.
    management_key_id: str = Field(default="")

class DeleteManagementKeyResponse(BaseModel):#  Empty
    """
     DeleteManagementKeyResponse is the response from the DeleteManagementKey function
    """
