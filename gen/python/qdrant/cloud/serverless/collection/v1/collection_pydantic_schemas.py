# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .collection_config_pydantic_schemas import CollectionConfiguration
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class ListCollectionsRequest(BaseModel):
    """
     ListCollectionsRequest is an empty request to list collections
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")

class ClusterEndpoint(BaseModel):
    """
     Endpoint information to access the qdrant collection (aka serverless database).
 All fields in this message are a read-only field.
    """

# URL to access the qdrant collection (aka serverless database) without port
    url: str = Field(default="")
# The port to use for HTTP REST calls (6333)
    rest_port: int = Field(default=0)
# The port to use for gRPC calls (6334)
    grpc_port: int = Field(default=0)

class CollectionState(BaseModel):
    """
     CollectionState represents the operational state of a collection in the Qdrant serverless environment.
 It provides status information, error details (if any), and endpoint access information.
    """

# The current operational status of the collection.
# - ready: Collection is fully operational and available for use
# - processing: Collection is being created, updated, or undergoing maintenance
# - disabled: Collection has been temporarily or permanently disabled
    phase: str = Field(default="")
# Descriptive message explaining any errors or issues with the collection.
# Empty when the collection is operating normally.
    reason: str = Field(default="")
# The URL endpoint where clients can connect to and interact with the collection.
# Not set if the collection is not yet ready or is disabled.
    endpoint: typing.Optional[ClusterEndpoint] = Field(default=None)

class Collection(BaseModel):
    """
     Collection represents a vector search collection in the Qdrant serverless environment
    """

# Unique identifier for the collection (in Guid format).
# This is a read-only field and will be available after a collection is created.
    id: str = Field(default="")
# Timestamp when the collection was created.
# This is a read-only field and will be available after a collection is created.
    created_at: datetime = Field(default_factory=datetime.now)
# Identifier of the account associated with the collection (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Name of the collection.
# This is a required field.
# Name can only contain letters, numbers, underscores and dashes
    name: str = Field(default="")
# Timestamp when the collection was deleted (or is started to be deleting).
# This is a read-only field and will be set after DeleteCollection is called.
    deleted_at: datetime = Field(default_factory=datetime.now)
# Cloud provider where the collection is hosted.
# This is a optional field (one of the following: aws, gcp, azure).
# After creation, this field cannot be changed.
# If not specified - use default provider
    cloud_provider: typing.Optional[str] = Field(default="")
# In which region the collection is hosted
# After creation, this field cannot be changed.
# Example: us-west1
# If not specified - use default region for the selected provider (or default provider if not specified)
    cloud_region: typing.Optional[str] = Field(default="")
# Configuration parameters
    configuration: CollectionConfiguration = Field()
# Status of the collection
# All fields inside `state` are read-only.
    state: CollectionState = Field()

class ListCollectionsResponse(BaseModel):
    """
     ListCollectionsResponse contains the list of collections
    """

# List of collections with their details
    collections: typing.List[Collection] = Field(default_factory=list)

class CreateCollectionRequest(BaseModel):
    """
     CreateCollectionRequest defines parameters for creating a new collection
    """

# Collection represents a vector search collection in the Qdrant serverless environment
    collection: Collection = Field()

class CreateCollectionResponse(BaseModel):
    """
     CollectionResponse provides details about a created collection
    """

# Collection represents a vector search collection in the Qdrant serverless environment
    collection: Collection = Field()

class UpgradeCollectionRequest(BaseModel):
    """
     Upgrade limits of the specified collection
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# ID of the collection to upgrade (in Guid format).
# This is a required field.
    collection_id: str = Field(default="")

class UpgradeCollectionResponse(BaseModel):#  Empty
    """
     Response for upgrading collection
    """

class DeleteCollectionRequest(BaseModel):
    """
     DeleteCollectionRequest identifies the collection to delete
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# ID of the collection to delete (in Guid format).
# This is a required field.
    collection_id: str = Field(default="")

class DeleteCollectionResponse(BaseModel):#  Empty
    """
     DeleteCollectionResponse is an empty response for deletion confirmation
    """
