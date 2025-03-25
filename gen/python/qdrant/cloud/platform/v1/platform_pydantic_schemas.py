# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class CloudProvider(BaseModel):
    """
     CloudProvider represents a cloud provider identifier and name.
    """

# The identifier for the cloud provider.
# e.g. "aws", "gcp", "azure", "hybrid"
    id: str = Field(default="")
# The human-readable name of the cloud provider.
# e.g. "Amazon Web Services", "Google Cloud", "Microsoft Azure", "Hybrid Cloud"
    name: str = Field(default="")

class ListCloudProvidersRequest(BaseModel):
    """
     ListCloudProvidersRequest is the request for the ListCloudProviders function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")

class ListCloudProvidersResponse(BaseModel):
    """
     ListCloudProvidersResponse is the response from the ListCloudProviders function
    """

# The cloud providers
    items: typing.List[CloudProvider] = Field(default_factory=list)

class CloudProviderRegion(BaseModel):
    """
     CloudProvider represents a cloud provider region identifier
    """

# The identifier for the cloud provider region.
# e.g. "us-west-1", "europe-west1", "eastus", "hybrid"
    id: str = Field(default="")

class ListCloudProviderRegionsRequest(BaseModel):
    """
     ListCloudProviderRegionsRequest is the request for the ListCloudProviderRegions function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier for the cloud provider. One of the providers from response of the ListCloudProviders function.
# This is an required field.
    cloud_provider_id: str = Field(default="")

class ListCloudProviderRegionsResponse(BaseModel):
    """
     ListCloudProviderRegionsResponse is the response from the ListCloudProviderRegions function
    """

# The cloud provider regions
    items: typing.List[CloudProviderRegion] = Field(default_factory=list)
