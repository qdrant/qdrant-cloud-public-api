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
# The identifier of the cluster (in Guid format).
# This is a required field.
    cluster_id: str = Field(default="")

class GlobalAccessRule(BaseModel):
    """
     Represents a global access rule that grants access to the entire database.
    """

# The type of access granted at the global level.
# "read" allows read-only access to the database, while "manage" allows read and write access.
# This is a required field.
    access_type: str = Field(default="")

class CollectionAccessRule(BaseModel):
    """
     Represents an access rule for a specific collection in the database.
    """

# The name of the collection.
# This is a required field.
    collection_name: str = Field(default="")
# The type of access granted for the collection.
# "read" allows read-only access, while "read-write" allows both read and write access.
# This is a required field.
    access_type: str = Field(default="")
# An optional payload containing key-value pairs.
    payload: typing.Dict[str, str] = Field(default_factory=dict)

class AccessRule(BaseModel):
    """
     Represents an access rule. An access rule can either define global access to
 the database or access to a specific collection.
    """

# A rule granting global access to the entire database.
# Only one of the fields (global_access or collection_access) should be set in a single rule.
    global_access: GlobalAccessRule = Field()
# A rule granting access to a specific collection in the database.
# Only one of the fields (global_access or collection_access) should be set in a single rule.
    collection_access: CollectionAccessRule = Field()

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
# The identifier of the cluster (in Guid format).
# This is a required field.
    cluster_id: str = Field(default="")
# Name of the database api key.
# This is a required field.
# Name can only contain letters, numbers, spaces, underscores and dashes.
    name: str = Field(default="")
# The expiration time of the database api key. The key will be invalid after this time.
# This field is optional, and if not provided, the key does not expire.
    expires_at: typing.Optional[datetime] = Field(default_factory=datetime.now)
# A list of rules to grant access to the Qdrant database or to specific
# collections. If no access rules are provided, global access to the database
# with manage permissions is assumed. The list can contain a maximum of 20
# access rules.
    access_rules: typing.List[AccessRule] = Field(default_factory=list)
# The email of the user who created the database api key.
# This is a read-only field and will be available after a database api key is created.
    created_by_email: str = Field(default="")
# Postfix for the database api key, this represents the last bytes of the key.
# This is a read-only field and will be available after a database api key is created.
    postfix: str = Field(default="")
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
    database_api_key: DatabaseApiKey = Field()

class CreateDatabaseApiKeyResponse(BaseModel):
    """
     CreateDatabaseApiKeyResponse is the response from the CreateDatabaseApiKey function.
    """

# The actual database api key.
    database_api_key: DatabaseApiKey = Field()

class DeleteDatabaseApiKeyRequest(BaseModel):
    """
     DeleteDatabaseApiKeyRequest is the request for the DeleteDatabaseApiKey function.
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier for the cluster (in Guid format).
# This cluster should be part of the provided account.
# This is a required field.
    cluster_id: str = Field(default="")
# The identifier of the database api key (in Guid format).
# This is a required field.
    database_api_key_id: str = Field(default="")

class DeleteDatabaseApiKeyResponse(BaseModel):#  Empty
    """
     DeleteDatabaseApiKeyResponse is the response from the DeleteDatabaseApiKey function.
    """
