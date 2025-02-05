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

class ListClustersRequest(BaseModel):
    """
     ListClustersRequest is the request for the ListClusters function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The optional identifier for hybrid cloud (in Guid format).
# If ommited all clusters, including the hybrid cloud ones, which belongs to the provided account are returned.
    hybrid_cloud_id: typing.Optional[str] = Field(default="")# TODO: ListOptions

class AdditionalResources(BaseModel):#  Currently not supported, but will be added in the near future:
 Additional CPU (expressed in milli vCPU)
 int cpu = 1;
 Additional Memory (expressed in Gib)
 int ram = 2;
# Additional Disk (expressed in Gib)
    disk: int = Field(default=0)

class QdrantConfigurationCollectionVectors(BaseModel):
    on_disk: bool = Field(default=False)

class QdrantConfigurationCollection(BaseModel):
    replication_factor: int = Field(default=0)
    write_consistency_factor: int = Field(default=0)
    vectors: QdrantConfigurationCollectionVectors = Field()

class QdrantConfigurationStoragePerformance(BaseModel):
    optimizer_cpu_budget: int = Field(default=0)
    async_scorer: bool = Field(default=False)

class QdrantConfigurationStorage(BaseModel):
    performance: QdrantConfigurationStoragePerformance = Field()

class SecretKeyRef(BaseModel):
    key: str = Field(default="")
    name: str = Field(default="")

class QdrantConfigApiKey(BaseModel):
    secret_key_ref: SecretKeyRef = Field()

class QdrantConfigurationService(BaseModel):
    api_key: QdrantConfigApiKey = Field()
    read_only_api_key: QdrantConfigApiKey = Field()
    jwt_rbac: bool = Field(default=False)
    enable_tls: bool = Field(default=False)

class QdrantConfigSecretKey(BaseModel):
    secret_key_ref: SecretKeyRef = Field()

class QdrantConfigurationTls(BaseModel):
    cert: QdrantConfigSecretKey = Field()
    key: QdrantConfigSecretKey = Field()

class DatabaseConfiguration(BaseModel):
    """
    TODO: Messages below needs comments and validation!
 Configuration to setup a qdrant database in a hybrid cloud.
    """

    collection: QdrantConfigurationCollection = Field()
    storage: QdrantConfigurationStorage = Field()
    service: QdrantConfigurationService = Field()
    log_level: str = Field(default="")
    tls: QdrantConfigurationTls = Field()

class KeyValue(BaseModel):
    """
     KeyValue is a key-value tuple (used in e.g. node selectors / annotations)
 The message represents an object for Kubernetes.
 TODO: Move to common.v1
    """

# The key part of a key-value pair
    key: str = Field(default="")
# The value part of a key-value pair
    value: str = Field(default="")

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
# If ommited the latest version will be used and filled out during create.
# Use ListReleases() to determine which versions are allowed to be used.
# See upgrade guidelines for more info.
    version: str = Field(default="")
# The package identifier used to configure the resources of the cluster. Use ListPackages() to select one.
    package_id: str = Field(default="")
# The additional resources on top of the selected package.
# This is an optional field, if not specified all additional resources are 0.
    additional_resources: typing.Optional[AdditionalResources] = Field(default=None)
# Configuration to setup a qdrant database in a hybrid cloud.
# It is ignored for Managed Cloud clusters. This is an optional field
    database_configuration: typing.Optional[DatabaseConfiguration] = Field(default=None)
# The node selector for this cluster in a hybrid cloud.
# It is ignored for Managed Cloud clusters. This is an optional field
    node_selector: typing.List[KeyValue] = Field(default_factory=list)
# List of tolerations for this cluster in a hybrid cloud.
# It is ignored for Managed Cloud clusters. This is an optional field
    tolerations: typing.List[Toleration] = Field(default_factory=list)
# List of annotations for this cluster in a hybrid cloud.
# It is ignored for Managed Cloud clusters. This is an optional field
    annotations: typing.List[KeyValue] = Field(default_factory=list)
# List of allowed IP source ranges for this cluster. Field is used for both
# hybrid cloud and Managed Cloud clusters. This is an optional field
# TODO: Are both IPv4 and IPv6 supported? --> IPv4 only for now?
# TODO: Do we want to create a reg-ex for validation?
    allowed_ip_source_ranges: typing.List[str] = Field(default_factory=list)
# TODO: Ask Bastian if 80 is OK (or it should be 99/100)?
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
     ClusterResourcesSummary represents the summary of the resources used in this cluster per node.
    """

# Disk resources
    disk: ClusterNodeResources = Field()
# Memory resources
    ram: ClusterNodeResources = Field()
# CPU resouces
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
# Summary of the resources used by the cluster per node.
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
# Cloud provider where the cluster is hosted.
# This is a required field (one of the following: aws, gcp, azure, hybrid).
# After creation, this field cannot be changed.
    cloud_provider: str = Field(default="")
# Cloud region where the cluster is located.
# For hybrid this should be the hybrid cloud ID.
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
    items: typing.List[Cluster] = Field(default_factory=list)# TODO: Add an operation timestamp the ListClusters is started, to support the `since` in ListOptions

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
