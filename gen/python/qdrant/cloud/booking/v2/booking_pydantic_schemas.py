# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from ...common.v1.common_pydantic_schemas import Version
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

class ListPackagesRequest(BaseModel):
    """
     ListPackagesRequest is the request for the ListPackages function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Cloud provider where the cluster will be hosted.
# This is an optional field (if set, it should be one of the following: aws, gcp, azure or hybrid).
    cloud_provider: typing.Optional[str] = Field(default="")
# Cloud region where the cluster is located.
# This is an optional field and is ignored if the provider is set to 'hybrid'.
    cloud_region: str = Field(default="")
# The status of the packages to filter.
# This is an optional field. If value is not set, all packages are returned.
    statuses: typing.List[str] = Field(default_factory=list)# TODO: ListOptions (however without since, the result doesn't contain any created_at/updated_at)

class ResourceConfiguration(BaseModel):
    """
     ResourceConfiguration configures a specific resource in a total resource configuration
    """

# The amount in the specified unit
    amount: int = Field(default=0)
# The unit of the resource, specifying what kind of unit the resource is measured in (e.g., m, Gib).
    resource_unit: str = Field(default="")
# The type of the resource, specifying the category or type of resource (e.g., vCPU, DiskSize).
    resource_type: str = Field(default="")

class Package(BaseModel):
    """
     Package represents a single package.
 A package is a configuration (CPU/Memory/Disk size) for a cluster with a price.
    """

# The unique identifier of the package.
# A unique string ID assigned to each package.
    id: str = Field(default="")
# The name of the package.
# A human-readable identifier for the package.
    name: str = Field(default="")
# Specifies if this is a free or paid package.
    type: str = Field(default="")
# A repeated field representing the resource configurations associated with the package.
    resource_configurations: typing.List[ResourceConfiguration] = Field(default_factory=list)
# The currency of the prices.
# Specifies the currency in which the prices are denominated.
    currency: str = Field(default="")
# The unit price per hour in millicents, in integer format.
# Represents the cost per hour for a single unit of the resource.
# TODO: You will be billed by minutes? @Mikheil do you know?
    unit_int_price_per_hour: int = Field(default=0)
# The status of the package.
# Indicates the current status of the package.
# One of: Active, Deactivated
    status: str = Field(default="")

class ListPackagesResponse(BaseModel):
    """
     ListPackagesResponse is the response from the ListPackages function
    """

# The actual packages in this list
    items: typing.List[Package] = Field(default_factory=list)

class GetPackageRequest(BaseModel):
    """
     GetAPIVersionRequest is the request for the GetAPIVersion function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The unique identifier of the package.
# A unique string ID assigned to each package.
    id: str = Field(default="")

class GetPackageResponse(BaseModel):
    """
     GetPackageResponse is the response from the GetPackage function
    """

# The actual package
    package: Package = Field()
