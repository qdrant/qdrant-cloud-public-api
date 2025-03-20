# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from ...common.v1.common_pydantic_schemas import KeyValue
from ...common.v1.common_pydantic_schemas import SecretKeyRef
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator
import typing


class ListClustersRequest(BaseModel):
    """
     ListClustersRequest is the request for the ListClusters function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Optional filter for cloud provider where the cluster is hosted (one of the following: aws, gcp, azure, hybrid).
# If omitted all clusters, including the hybrid cloud ones, which belongs to the provided account are returned.
    cloud_provider: typing.Optional[str] = Field(default="")
# Optional filter for cloud region where the cluster is located
# If this field is set the cloud_provider is required to set as well (and it should match).
# For hybrid this should be the hybrid cloud environment ID.
    cloud_region: typing.Optional[str] = Field(default="")

class AdditionalResources(BaseModel):#  Currently not supported, but will be added in the near future:
 Additional CPU (expressed in milli vCPU)
 int cpu = 1;
 Additional Memory (expressed in Gib)
 int ram = 2;
    """
     AdditionalResources contains the information about additional resources
    """

# Additional Disk (expressed in Gib)
    disk: int = Field(default=0)

class DatabaseConfigurationCollectionVectors(BaseModel):
    """
     The default Qdrant database collection vectors configuration
    """

# If set, this will create a collection with all vectors immediately stored in memmap storage.
# This is the recommended way, in case your Qdrant instance operates with fast disks and you are working with large collections.
# For more info see: https://qdrant.tech/documentation/concepts/storage/#configuring-memmap-storage
# This is an optional field, the default value will be true.
    on_disk: typing.Optional[bool] = Field(default=False)

class DatabaseConfigurationCollection(BaseModel):
    """
     The default Qdrant database collection configuration
    """

# Number of replicas of each shard that network tries to maintain
# This is an optional, the default is 1
    replication_factor: typing.Optional[int] = Field(default=0)
# How many replicas should apply the operation for us to consider it successful
# This is an optional, the default is 1
    write_consistency_factor: int = Field(default=0)
# The default parameters for vectors.
    vectors: DatabaseConfigurationCollectionVectors = Field()

class DatabaseConfigurationStoragePerformance(BaseModel):
    """
     The performance related Qdrant database storage configuration
    """

# CPU budget, how many CPUs (threads) to allocate for an optimization job.
# If 0 - auto selection, keep 1 or more CPUs unallocated depending on CPU size
# If negative - subtract this number of CPUs from the available CPUs.
# If positive - use this exact number of CPUs.
    optimizer_cpu_budget: int = Field(default=0)
# Enable async scorer which uses io_uring when rescoring.
# Only supported on Linux, must be enabled in your kernel.
# See: https://qdrant.tech/articles/io_uring/#and-what-about-qdrant
    async_scorer: bool = Field(default=False)

class DatabaseConfigurationStorage(BaseModel):
    """
     The Qdrant storage configuration
    """

# The performance related Qdrant database storage configuration
    performance: DatabaseConfigurationStoragePerformance = Field()

class DatabaseConfigurationService(BaseModel):
    """
     The Qdrant database service configuration
    """

# Set an api-key.
# If set, all requests must include a header with the api-key.
# example header: `api-key: <API-KEY>`
    api_key: typing.Optional[SecretKeyRef] = Field(default=None)
# Set an api-key for read-only operations.
# If set, all requests must include a header with the api-key.
# example header: `api-key: <API-KEY>`
    read_only_api_key: typing.Optional[SecretKeyRef] = Field(default=None)
# Enable JWT Role Based Access Control (RBAC).
# If enabled, you can generate JWT tokens with fine-grained rules for access control.
# Use generated token instead of API key.
    jwt_rbac: bool = Field(default=False)
# Enable HTTPS for the REST and gRPC API
    enable_tls: bool = Field(default=False)

class DatabaseConfigurationTls(BaseModel):
    """
     DatabaseConfigurationTls contains the information to setup a TLS connection to the database endpoint
    """

# Secret to use for the certificate
    cert: SecretKeyRef = Field()
# Secret to use for the private key
    key: SecretKeyRef = Field()

class DatabaseConfigurationInference(BaseModel):
    """
     DatabaseConfigurationInference contains cloud inferencing configuration
    """

# If true, the database is configured to use cloud inferencing
    enabled: bool = Field(default=False)

class DatabaseConfiguration(BaseModel):
    """
     Configuration to setup a Qdrant database in a hybrid cloud.
 All settings apply to hybrid cloud only.
    """

# The default Qdrant database collection configuration
# This is an optional field
    collection: typing.Optional[DatabaseConfigurationCollection] = Field(default=None)
# The default Qdrant database storage configuration
# This is an optional field
    storage: typing.Optional[DatabaseConfigurationStorage] = Field(default=None)
# The Qdrant database service configuration
# This is an optional field
    service: typing.Optional[DatabaseConfigurationService] = Field(default=None)
# The log level for the database
# This is an optional field, default is Info
# The allowed values are: Trace, Debug, Info, Warn, Error, Off
# Qdrant is written in Rust and is using: https://docs.rs/log/latest/log/enum.LevelFilter.html
    log_level: typing.Optional[str] = Field(default="")
# The Qdrant database TLS configuration
# This is an optional field, if not set an unsecure connection is provided
    tls: typing.Optional[DatabaseConfigurationTls] = Field(default=None)
# The Qdrant database inference configuration
# This is an optional field, if unset, the database is not configured for cloud inferencing
    inference: typing.Optional[DatabaseConfigurationInference] = Field(default=None)

class Toleration(BaseModel):
    """
     The Toleration message represents a toleration object for Kubernetes.
    """

# The key to match against the key of a node label.
    key: str = Field(default="")
# The operator represents a key's relationship to the value.
# Valid operators are "Exists" and "Equal".
# The default is Exists
    operator: typing.Optional[str] = Field(default="")
# The value to match against the value of a node label.
    value: str = Field(default="")
# The effect indicates the taint effect to match.
# Valid effects are "NoSchedule", "PreferNoSchedule", and "NoExecute".
# The default is NoSchedule
    effect: typing.Optional[str] = Field(default="")
# The toleration seconds indicates the duration to tolerate the taint.
    toleration_seconds: typing.Optional[int] = Field(default=0)

class ClusterConfiguration(BaseModel):
    """
     A ClusterConfiguration represents the configuration of a cluster.
    """

# Timestamp when the cluster configuration was last updated.
# This is a read-only field and will be available after a cluster is created.
    last_modified_at: datetime = Field(default_factory=datetime.now)
# The number of nodes in a cluster.
# This should be a number 1...20 [both included].
    number_of_nodes: int = Field(default=0)
# Version of the cluster software.
# If omitted the latest version will be used and filled out during create.
# Use ListReleases() to determine which versions are allowed to be used.
# See upgrade guidelines for more info.
    version: str = Field(default="")
# TODO: Needing a package_id here is very bad usability for users.
# That means we would need to start documenting all package_ids somewhere.
# Rather we should introduce speaking package names in the public api (even if we have them different internally).
# In the price list we already have them kind of 'https://docs.google.com/spreadsheets/d/1dDo1u6YExocd2MJfi_Xgjnret2vJqo84S-9-gcOltkc/edit?gid=0#gid=0'
# We could derive them from the SKU, e.g. QN_16x128 fine with something else as well.
# The package identifier used to configure the resources of the cluster. Use ListPackages() to select one.
    package_id: str = Field(default="")
# The additional resources on top of the selected package.
# This is an optional field, if not specified all additional resources are 0.
    additional_resources: typing.Optional[AdditionalResources] = Field(default=None)
# Configuration to setup a qdrant database in a hybrid cloud.
# It is ignored for managed cloud clusters. This is an optional field
    database_configuration: typing.Optional[DatabaseConfiguration] = Field(default=None)
# The node selector for this cluster in a hybrid cloud.
# It is ignored for managed cloud clusters. This is an optional field
    node_selector: typing.List[KeyValue] = Field(default_factory=list)
# List of tolerations for this cluster in a hybrid cloud.
# It is ignored for managed cloud clusters. This is an optional field
    tolerations: typing.List[Toleration] = Field(default_factory=list)
# List of annotations for this cluster in a hybrid cloud.
# It is ignored for managed cloud clusters. This is an optional field
    annotations: typing.List[KeyValue] = Field(default_factory=list)
# List of allowed IP source ranges for this cluster.
# Field is used for both managed cloud and hybrid cloud and clusters. This is an optional field
# The CIDRs supports IPv4 only.
    allowed_ip_source_ranges: typing.List[str] = Field(default_factory=list)
# The percentage of CPU resources reserved for system components
# This is an optional field, default is 0.
# Number between 0..80
    reserved_cpu_percentage: int = Field(default=0)
# The percentage of RAM resources reserved for system components
# This is an optional field, default is 0.
# Number between 0..80
    reserved_memory_percentage: int = Field(default=0)

class ClusterEndpoint(BaseModel):
    """
     Endpoint information to access the qdrant cluster (aka database).
 All fields in this message are a read-only field.
    """

# URL to access the qdrant cluster (aka database) without port
    url: str = Field(default="")
# The port to use for HTTP REST calls (6333)
    rest_port: int = Field(default=0)
# The port to use for gRPC calls (6334)
    grpc_port: int = Field(default=0)

class ClusterNodeResources(BaseModel):
    """
     ClusterNodeResources represents the allocation of various resources for a cluster per node.
    """

# Base resources that are part of the standard allocation for the cluster per node.
# This includes default CPU, memory, storage, etc.
    base: float = Field(default=0.0)
# Complimentary resources provided to the cluster at no additional cost.
# This might include complimentary network bandwidth, credits, etc.
    complimentary: float = Field(default=0.0)
# Additional resources allocated to the cluster.
# This could include additional storage, compute power, etc.
    additional: float = Field(default=0.0)
# The reserved is the amount used by the system, which cannot be used by the database itself.
    reserved: float = Field(default=0.0)
# The available is the total (base+complimentary+additional) - reserved
    available: float = Field(default=0.0)

class ClusterNodeResourcesSummary(BaseModel):
    """
     ClusterNodeResourcesSummary represents the resources used in this cluster per node.
    """

# Disk resources
    disk: ClusterNodeResources = Field()
# Memory resources
    ram: ClusterNodeResources = Field()
# CPU resources
    cpu: ClusterNodeResources = Field()

class ClusterState(BaseModel):
    """
     ClusterState represents the current state of a cluster
 All fields in this message are read-only.
    """

# Version of the cluster software
    version: str = Field(default="")
# Number of cluster nodes that are up and running
    nodes_up: int = Field(default=0)
# The date and time when the cluster was restarted
    restarted_at: datetime = Field(default_factory=datetime.now)
# Current phase of the cluster
# One of the following: Creating, ...
    phase: str = Field(default="")
# Reason for the current phase of the cluster.
    reason: str = Field(default="")
# Endpoint information to access the qdrant cluster (aka database).
    endpoint: ClusterEndpoint = Field()
# The resources used by the cluster per node.
# For the complete cluster you have to multiply by cluster.configuration.number_of_nodes
    resources: ClusterNodeResourcesSummary = Field()

class Cluster(BaseModel):
    """
     A Cluster represents one cluster of a Qdrant database.
    """

# Unique identifier for the cluster (in Guid format).
# This is a read-only field and will be available after a cluster is created.
    id: str = Field(default="")
# Timestamp when the cluster was created.
# This is a read-only field and will be available after a cluster is created.
    created_at: datetime = Field(default_factory=datetime.now)
# Identifier of the account associated with the cluster (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# Name of the cluster.
# This is a required field.
# Name can only contain letters, numbers, underscores and dashes
    name: str = Field(default="")
# Timestamp when the cluster was deleted (or is started to be deleting).
# This is a read-only field and will be set after DeleteCluster is called.
    deleted_at: datetime = Field(default_factory=datetime.now)
# Cloud provider where the cluster is hosted.
# This is a required field (one of the following: aws, gcp, azure, hybrid).
# After creation, this field cannot be changed.
    cloud_provider: str = Field(default="")
# Cloud region where the cluster is located.
# For hybrid this should be the hybrid cloud environment ID.
# This is a required field.
# After creation, this field cannot be changed.
    cloud_region: str = Field(default="")
# Current configuration details of the cluster.
    configuration: ClusterConfiguration = Field()
# Current state of the cluster.
# All fields inside `state` are read-only.
    state: ClusterState = Field()

class ListClustersResponse(BaseModel):
    """
     ListClustersResponse is the response from the ListClusters function
    """

# The actual clusters in this list
    items: typing.List[Cluster] = Field(default_factory=list)

class GetClusterRequest(BaseModel):
    """
     GetClusterRequest is the request for the GetCluster function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier for the cluster (in Guid format).
# This cluster should be part of the provided account.
# This is a required field.
    cluster_id: str = Field(default="")

class GetClusterResponse(BaseModel):
    """
     GetClusterResponse is the response from the GetCluster function
    """

# The actual cluster
    cluster: Cluster = Field()

class CreateClusterRequest(BaseModel):
    """
     CreateClusterRequest is the request for the CreateCluster function
    """

# The actual cluster
    cluster: Cluster = Field()

class CreateClusterResponse(BaseModel):
    """
     CreateClusterResponse is the response from the CreateCluster function
    """

# The actual cluster
    cluster: Cluster = Field()

class UpdateClusterRequest(BaseModel):
    """
     UpdateClusterRequest is the request for the UpdateCluster function
    """

# The actual cluster
    cluster: Cluster = Field()

class UpdateClusterResponse(BaseModel):
    """
     UpdateClusterResponse is the response from the UpdateCluster function
    """

# The actual cluster
    cluster: Cluster = Field()

class DeleteClusterRequest(BaseModel):
    """
     DeleteClusterRequest is the request for the DeleteCluster function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier for the cluster (in Guid format).
# This cluster should be part of the provided account.
# This is a required field.
    cluster_id: str = Field(default="")
# If set, the backups of this cluster will be deleted as well.
    delete_backups: typing.Optional[bool] = Field(default=False)

class DeleteClusterResponse(BaseModel):#  Empty
    """
     DeleteClusterResponse is the response from the DeleteCluster function
    """

class RestartClusterRequest(BaseModel):
    """
     RestartClusterRequest is the request for the RestartCluster function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier for the cluster (in Guid format).
# This cluster should be part of the provided account.
# This is a required field.
    cluster_id: str = Field(default="")

class RestartClusterResponse(BaseModel):#  Empty
    """
     RestartClusterResponse is the response from the RestartCluster function
    """

class ListQdrantReleasesRequest(BaseModel):
    """
     ListQdrantReleasesRequest is the request for the ListQdrantReleases function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier for the cluster (in Guid format).
# This cluster should be part of the provided account.
# This is an optional field.
    cluster_id: typing.Optional[str] = Field(default="")

class QdrantRelease(BaseModel):
    """
     QdrantRelease represent a single Qdrant release
    """

# Version of the Qdrant release
    version: str = Field(default="")
# Flag to indicate if this is the default release
# There can be at most a single item in the list that have this property set.
    default: bool = Field(default=False)
# URL to the release notes
    release_notes_url: typing.Optional[str] = Field(default="")
# Additional message regarding this release that might be useful to the client"
    remarks: typing.Optional[str] = Field(default="")

class ListQdrantReleasesResponse(BaseModel):
    """
     ListQdrantReleasesResponse is the response from the ListQdrantReleases function
    """

# The actual Qdrant releases in this list
    items: typing.List[QdrantRelease] = Field(default_factory=list)

class ListClusterJWTsRequest(BaseModel):
    """
     ListClusterJWTsRequest is the request for the ListClusterJWTs function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the cluster (in Guid format).
# This is a required field.
    cluster_id: str = Field(default="")

class ClusterJWTPayloadAccess(BaseModel):
    """
     A ClusterJWTPayloadAccess defines an access rule for a collection in the cluster.
    """

# The name of the collection.
    collection: str = Field(default="")
# The level of access. Must be either "r" (read) or "rw" (read/write).
    access: str = Field(default="")
# TODO confirm if we could add some validation for this field (number of
# items in the list, key validation) or if it is ok let it like this.
#
# Optional payload as key-value pairs.
    payload: typing.Dict[str, str] = Field(default_factory=dict)

class ClusterJWTPayloadAccessList(BaseModel):
    """
     A list of access rules, each specifying access to a specific collection
 and optionally restricting access to data based on payload filters.
    """

# A repeated list of access rules for the JWT. Each rule specifies collection-level access.
    rules: typing.List[ClusterJWTPayloadAccess] = Field(default_factory=list)

class ClusterJWTPayload(BaseModel):
    """
     A ClusterJWTPayload represents the JWT payload for a Cluster JWT.
 This payload contains claims that define functionality and access control in the system.
    """

    _one_of_dict = {"ClusterJWTPayload.access_type": {"fields": {"access", "access_list"}}}
    one_of_validator = model_validator(mode="before")(check_one_of)
# A general access level claim, either "r" (read) or "m" (modify).
    access: str = Field(default="")
# A list of access rules per collection.
    access_list: ClusterJWTPayloadAccessList = Field()# TODO: Why not 'simply' repeated ClusterJWTPayloadAccess rules = 1;, do we expect to add more?
# TODO check if this field could be defined as duration instead of int64, or
# if there is a better type for it.
#
# The expiration time of the cluster JWT in seconds since the Unix epoch.
    exp: typing.Optional[int] = Field(default=0)

class ClusterJWT(BaseModel):
    """
     TODO: ClusterJWT we call them in the ui `Database Api Keys`, we should consider using a better name in the API.
 A ClusterJWT represents a JWT to access a Qdrant cloud cluster.
    """

# Unique identifier for the cluster JWT (in Guid format).
# This is a read-only field and will be available after a cluster JWT is created.
    id: str = Field(default="")
# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the cluster (in Guid format).
# This is a required field.
    cluster_id: str = Field(default="")
# Name of the cluster JWT.
# This is a required field
# Name can only contain letters, numbers, spaces, underscores and dashes
    name: str = Field(default="")
# TODO: rename to configuration?
# The JWT payload of the cluster JWT.
    jwt_payload: ClusterJWTPayload = Field()
# Timestamp when the cluster JWT was created.
# This is a read-only field and will be available after a cluster JWT is created.
    created_at: datetime = Field(default_factory=datetime.now)
# The email of the user who created the cluster JWT.
# This is a read-only field and will be available after a cluster JWT is created.
    created_by_email: str = Field(default="")
# Postfix for the Cluster JWT, this represents the last bytes of the token.
# This is a read-only field and will be available after a cluster JWT is created.
    postfix: str = Field(default="")
# The token for the Cluster JWT.
# This is a read-only field and will be available only once in the return of CreateClusterJWT.
# You should securely store this token and it should be handled as a secret.
    token: str = Field(default="")# TODO: rename to key?

class ListClusterJWTsResponse(BaseModel):
    """
     ListClusterJWTsResponse is the response from the ListClusterJWTs function
    """

# The actual cluster-jwts in this list
    items: typing.List[ClusterJWT] = Field(default_factory=list)

class CreateClusterJWTRequest(BaseModel):
    """
     CreateClusterJWTRequest is the request for the CreateClusterJWT function
    """

# The actual Cluster JWT
    cluster_jwt: ClusterJWT = Field()

class CreateClusterJWTResponse(BaseModel):
    """
     CreateClusterJWTResponse is the response from the the CreateClusterJWT function
    """

# The actual Cluster JWT
    cluster_jwt: ClusterJWT = Field()

class DeleteClusterJWTRequest(BaseModel):
    """
     DeleteClusterJWTRequest is the request for the DeleteClusterJWT function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier for the cluster (in Guid format).
# This cluster should be part of the provided account.
# This is a required field.
    cluster_id: str = Field(default="")
# The identifier for the JWT (in Guid format).
# This JWT should belong to the provided cluster.
    cluster_jwt_id: str = Field(default="")

class DeleteClusterJWTResponse(BaseModel):#  Empty
    """
     DeleteClusterJWTResponse is the response from the DeleteClusterJWT function
    """
