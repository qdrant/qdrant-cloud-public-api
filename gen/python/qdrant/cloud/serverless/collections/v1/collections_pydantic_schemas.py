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
# May be empty if the collection is not yet ready or is disabled.
    endpoint: typing.Optional[str] = Field(default="")

class Collection(BaseModel):
    """
     Collection represents a vector search collection in the Qdrant serverless environment
    """

# Unique identifier for the collection
    id: str = Field(default="")
# Name of the collection
    name: str = Field(default="")
# When the collection was created
    created_at: datetime = Field(default_factory=datetime.now)
# Configuration parameters
    configuration: CollectionConfiguration = Field()
# Cloud provider where the cluster is hosted.
# This is a required field (one of the following: aws, gcp, azure).
# After creation, this field cannot be changed.
# If not specified - use default provider
    cloud_provider: typing.Optional[str] = Field(default="")
# In which region the collection is hosted
# Example: us-west1
    cloud_region: typing.Optional[str] = Field(default="")
# URL to access the hosting cluster
# Status of the collection
    state: CollectionState = Field()

class ListCollectionsResponse(BaseModel):
    """
     ListCollectionsResponse contains the list of collections
    """

# List of collections with their details
    collections: typing.List[Collection] = Field(default_factory=list)

class CreateCollectionResponse(BaseModel):
    """
     CollectionResponse provides details about a created collection
    """

# Collection represents a vector search collection in the Qdrant serverless environment
    collection: Collection = Field()

class CreateCollectionRequest(BaseModel):
    """
     CreateCollectionRequest defines parameters for creating a new collection
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Name for the new collection
# This is a read-only field and will be available after a collection is created.
    collection_name: str = Field(default="")
# Configuration settings for the collection
    configuration: CollectionConfiguration = Field()
# Cloud provider where the cluster is hosted.
# This is a required field (one of the following: aws, gcp, azure, hybrid).
# After creation, this field cannot be changed.
# If not specified - use default provider
    cloud_provider: typing.Optional[str] = Field(default="")
# Optional region to host the collection in.
# If not specified - use default region.
    cloud_region: typing.Optional[str] = Field(default="")

class UpgradeCollectionRequest(BaseModel):
    """
     Upgrade limits of the specified collection
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# ID of the collection to upgrade
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
# ID of the collection to delete
    collection_id: str = Field(default="")

class DeleteCollectionResponse(BaseModel):#  Empty
    """
     DeleteCollectionResponse is an empty response for deletion confirmation
    """
