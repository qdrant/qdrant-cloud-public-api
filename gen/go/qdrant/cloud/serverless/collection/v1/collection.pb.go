// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        (unknown)
// source: qdrant/cloud/serverless/collection/v1/collection.proto

package collectionv1

import (
	_ "buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate"
	_ "github.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/common/v1"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	reflect "reflect"
	sync "sync"
	unsafe "unsafe"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// CollectionStatePhase defines the operational phases of a Qdrant collection.
type CollectionStatePhase int32

const (
	// Unspecified phase.
	CollectionStatePhase_COLLECTION_STATE_PHASE_UNSPECIFIED CollectionStatePhase = 0
	// The Collection is fully operational and available for use.
	CollectionStatePhase_COLLECTION_STATE_PHASE_READY CollectionStatePhase = 1
	// The Collection is being created, updated, or undergoing maintenance.
	CollectionStatePhase_COLLECTION_STATE_PHASE_PROCESSING CollectionStatePhase = 2
	// The Collection has been temporarily or permanently disabled.
	CollectionStatePhase_COLLECTION_STATE_PHASE_DISABLED CollectionStatePhase = 3
)

// Enum value maps for CollectionStatePhase.
var (
	CollectionStatePhase_name = map[int32]string{
		0: "COLLECTION_STATE_PHASE_UNSPECIFIED",
		1: "COLLECTION_STATE_PHASE_READY",
		2: "COLLECTION_STATE_PHASE_PROCESSING",
		3: "COLLECTION_STATE_PHASE_DISABLED",
	}
	CollectionStatePhase_value = map[string]int32{
		"COLLECTION_STATE_PHASE_UNSPECIFIED": 0,
		"COLLECTION_STATE_PHASE_READY":       1,
		"COLLECTION_STATE_PHASE_PROCESSING":  2,
		"COLLECTION_STATE_PHASE_DISABLED":    3,
	}
)

func (x CollectionStatePhase) Enum() *CollectionStatePhase {
	p := new(CollectionStatePhase)
	*p = x
	return p
}

func (x CollectionStatePhase) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (CollectionStatePhase) Descriptor() protoreflect.EnumDescriptor {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_enumTypes[0].Descriptor()
}

func (CollectionStatePhase) Type() protoreflect.EnumType {
	return &file_qdrant_cloud_serverless_collection_v1_collection_proto_enumTypes[0]
}

func (x CollectionStatePhase) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use CollectionStatePhase.Descriptor instead.
func (CollectionStatePhase) EnumDescriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{0}
}

// ListCollectionsRequest is an empty request to list collections
type ListCollectionsRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The identifier of the account (in GUID format).
	// This is a required field.
	AccountId     string `protobuf:"bytes,1,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListCollectionsRequest) Reset() {
	*x = ListCollectionsRequest{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListCollectionsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListCollectionsRequest) ProtoMessage() {}

func (x *ListCollectionsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListCollectionsRequest.ProtoReflect.Descriptor instead.
func (*ListCollectionsRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{0}
}

func (x *ListCollectionsRequest) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

// ListCollectionsResponse contains the list of collections
type ListCollectionsResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// List of collections with their details
	Collections   []*Collection `protobuf:"bytes,1,rep,name=collections,proto3" json:"collections,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListCollectionsResponse) Reset() {
	*x = ListCollectionsResponse{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListCollectionsResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListCollectionsResponse) ProtoMessage() {}

func (x *ListCollectionsResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListCollectionsResponse.ProtoReflect.Descriptor instead.
func (*ListCollectionsResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{1}
}

func (x *ListCollectionsResponse) GetCollections() []*Collection {
	if x != nil {
		return x.Collections
	}
	return nil
}

// CreateCollectionRequest defines parameters for creating a new collection
type CreateCollectionRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// Collection represents a vector search collection in the Qdrant serverless environment
	Collection    *Collection `protobuf:"bytes,1,opt,name=collection,proto3" json:"collection,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CreateCollectionRequest) Reset() {
	*x = CreateCollectionRequest{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreateCollectionRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateCollectionRequest) ProtoMessage() {}

func (x *CreateCollectionRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateCollectionRequest.ProtoReflect.Descriptor instead.
func (*CreateCollectionRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{2}
}

func (x *CreateCollectionRequest) GetCollection() *Collection {
	if x != nil {
		return x.Collection
	}
	return nil
}

// CollectionResponse provides details about a created collection
type CreateCollectionResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// Collection represents a vector search collection in the Qdrant serverless environment
	Collection    *Collection `protobuf:"bytes,1,opt,name=collection,proto3" json:"collection,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CreateCollectionResponse) Reset() {
	*x = CreateCollectionResponse{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreateCollectionResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateCollectionResponse) ProtoMessage() {}

func (x *CreateCollectionResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateCollectionResponse.ProtoReflect.Descriptor instead.
func (*CreateCollectionResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{3}
}

func (x *CreateCollectionResponse) GetCollection() *Collection {
	if x != nil {
		return x.Collection
	}
	return nil
}

// Upgrade limits of the specified collection
type UpgradeCollectionRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The identifier of the account (in GUID format).
	// This is a required field.
	AccountId string `protobuf:"bytes,1,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	// ID of the collection to upgrade (in GUID format).
	// This is a required field.
	CollectionId  string `protobuf:"bytes,2,opt,name=collection_id,json=collectionId,proto3" json:"collection_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *UpgradeCollectionRequest) Reset() {
	*x = UpgradeCollectionRequest{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpgradeCollectionRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpgradeCollectionRequest) ProtoMessage() {}

func (x *UpgradeCollectionRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpgradeCollectionRequest.ProtoReflect.Descriptor instead.
func (*UpgradeCollectionRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{4}
}

func (x *UpgradeCollectionRequest) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

func (x *UpgradeCollectionRequest) GetCollectionId() string {
	if x != nil {
		return x.CollectionId
	}
	return ""
}

// Response for upgrading collection
type UpgradeCollectionResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *UpgradeCollectionResponse) Reset() {
	*x = UpgradeCollectionResponse{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpgradeCollectionResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpgradeCollectionResponse) ProtoMessage() {}

func (x *UpgradeCollectionResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpgradeCollectionResponse.ProtoReflect.Descriptor instead.
func (*UpgradeCollectionResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{5}
}

// DeleteCollectionRequest identifies the collection to delete
type DeleteCollectionRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The identifier of the account (in GUID format).
	// This is a required field.
	AccountId string `protobuf:"bytes,1,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	// ID of the collection to delete (in GUID format).
	// This is a required field.
	CollectionId  string `protobuf:"bytes,2,opt,name=collection_id,json=collectionId,proto3" json:"collection_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *DeleteCollectionRequest) Reset() {
	*x = DeleteCollectionRequest{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DeleteCollectionRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DeleteCollectionRequest) ProtoMessage() {}

func (x *DeleteCollectionRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DeleteCollectionRequest.ProtoReflect.Descriptor instead.
func (*DeleteCollectionRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{6}
}

func (x *DeleteCollectionRequest) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

func (x *DeleteCollectionRequest) GetCollectionId() string {
	if x != nil {
		return x.CollectionId
	}
	return ""
}

// DeleteCollectionResponse is an empty response for deletion confirmation
type DeleteCollectionResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *DeleteCollectionResponse) Reset() {
	*x = DeleteCollectionResponse{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[7]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DeleteCollectionResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DeleteCollectionResponse) ProtoMessage() {}

func (x *DeleteCollectionResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[7]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DeleteCollectionResponse.ProtoReflect.Descriptor instead.
func (*DeleteCollectionResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{7}
}

// Collection represents a vector search collection in the Qdrant serverless environment
type Collection struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// Unique identifier for the collection (in GUID format).
	// This is a read-only field and will be available after a collection is created.
	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// Timestamp when the collection was created.
	// This is a read-only field and will be available after a collection is created.
	CreatedAt *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	// Identifier of the account associated with the collection (in GUID format).
	// This is a required field.
	AccountId string `protobuf:"bytes,3,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	// Name of the collection.
	// This is a required field.
	// Name can only contain letters, numbers, underscores and dashes
	Name string `protobuf:"bytes,4,opt,name=name,proto3" json:"name,omitempty"`
	// Timestamp when the collection was deleted (or is started to be deleting).
	// This is a read-only field and will be set after DeleteCollection is called.
	DeletedAt *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=deleted_at,json=deletedAt,proto3" json:"deleted_at,omitempty"`
	// Cloud provider where the collection is hosted.
	// Must match one of the provider IDs returned by the `qdrant.cloud.platform.v1.PlatformService.ListCloudProviders` method.
	// In this case, `hybrid` isn't supported.
	// After creation, this field cannot be changed.
	CloudProviderId string `protobuf:"bytes,10,opt,name=cloud_provider_id,json=cloudProviderId,proto3" json:"cloud_provider_id,omitempty"`
	// Cloud provider region where the collection is hosted.
	// Must match one of the region IDs returned by the `qdrant.cloud.platform.v1.PlatformService.ListCloudProviderRegions` method.
	// After creation, this field cannot be changed.
	CloudProviderRegionId string `protobuf:"bytes,11,opt,name=cloud_provider_region_id,json=cloudProviderRegionId,proto3" json:"cloud_provider_region_id,omitempty"`
	// Configuration parameters
	Configuration *CollectionConfiguration `protobuf:"bytes,20,opt,name=configuration,proto3" json:"configuration,omitempty"`
	// Status of the collection
	// All fields inside `state` are read-only.
	State         *CollectionState `protobuf:"bytes,100,opt,name=state,proto3" json:"state,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *Collection) Reset() {
	*x = Collection{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[8]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Collection) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Collection) ProtoMessage() {}

func (x *Collection) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[8]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Collection.ProtoReflect.Descriptor instead.
func (*Collection) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{8}
}

func (x *Collection) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *Collection) GetCreatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.CreatedAt
	}
	return nil
}

func (x *Collection) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

func (x *Collection) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *Collection) GetDeletedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.DeletedAt
	}
	return nil
}

func (x *Collection) GetCloudProviderId() string {
	if x != nil {
		return x.CloudProviderId
	}
	return ""
}

func (x *Collection) GetCloudProviderRegionId() string {
	if x != nil {
		return x.CloudProviderRegionId
	}
	return ""
}

func (x *Collection) GetConfiguration() *CollectionConfiguration {
	if x != nil {
		return x.Configuration
	}
	return nil
}

func (x *Collection) GetState() *CollectionState {
	if x != nil {
		return x.State
	}
	return nil
}

// CollectionState represents the operational state of a collection in the Qdrant serverless environment.
// It provides status information, error details (if any), and endpoint access information.
type CollectionState struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The current operational status of the collection.
	Phase CollectionStatePhase `protobuf:"varint,1,opt,name=phase,proto3,enum=qdrant.cloud.serverless.collection.v1.CollectionStatePhase" json:"phase,omitempty"`
	// Descriptive message explaining any errors or issues with the collection.
	// Empty when the collection is operating normally.
	Reason string `protobuf:"bytes,2,opt,name=reason,proto3" json:"reason,omitempty"`
	// The URL endpoint where clients can connect to and interact with the collection.
	// Not set if the collection is not yet ready or is disabled.
	Endpoint      *CollectionEndpoint `protobuf:"bytes,7,opt,name=endpoint,proto3,oneof" json:"endpoint,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CollectionState) Reset() {
	*x = CollectionState{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[9]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CollectionState) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CollectionState) ProtoMessage() {}

func (x *CollectionState) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[9]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CollectionState.ProtoReflect.Descriptor instead.
func (*CollectionState) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{9}
}

func (x *CollectionState) GetPhase() CollectionStatePhase {
	if x != nil {
		return x.Phase
	}
	return CollectionStatePhase_COLLECTION_STATE_PHASE_UNSPECIFIED
}

func (x *CollectionState) GetReason() string {
	if x != nil {
		return x.Reason
	}
	return ""
}

func (x *CollectionState) GetEndpoint() *CollectionEndpoint {
	if x != nil {
		return x.Endpoint
	}
	return nil
}

// Endpoint information to access the qdrant collection (aka serverless database).
// All fields in this message are a read-only field.
type CollectionEndpoint struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// URL to access the qdrant collection (aka serverless database) without port
	Url string `protobuf:"bytes,1,opt,name=url,proto3" json:"url,omitempty"`
	// The port to use for HTTP REST calls (6333)
	RestPort int32 `protobuf:"varint,2,opt,name=rest_port,json=restPort,proto3" json:"rest_port,omitempty"`
	// The port to use for gRPC calls (6334)
	GrpcPort      int32 `protobuf:"varint,3,opt,name=grpc_port,json=grpcPort,proto3" json:"grpc_port,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CollectionEndpoint) Reset() {
	*x = CollectionEndpoint{}
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[10]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CollectionEndpoint) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CollectionEndpoint) ProtoMessage() {}

func (x *CollectionEndpoint) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[10]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CollectionEndpoint.ProtoReflect.Descriptor instead.
func (*CollectionEndpoint) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP(), []int{10}
}

func (x *CollectionEndpoint) GetUrl() string {
	if x != nil {
		return x.Url
	}
	return ""
}

func (x *CollectionEndpoint) GetRestPort() int32 {
	if x != nil {
		return x.RestPort
	}
	return 0
}

func (x *CollectionEndpoint) GetGrpcPort() int32 {
	if x != nil {
		return x.GrpcPort
	}
	return 0
}

var File_qdrant_cloud_serverless_collection_v1_collection_proto protoreflect.FileDescriptor

const file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDesc = "" +
	"\n" +
	"6qdrant/cloud/serverless/collection/v1/collection.proto\x12%qdrant.cloud.serverless.collection.v1\x1a\x1bbuf/validate/validate.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a#qdrant/cloud/common/v1/common.proto\x1a=qdrant/cloud/serverless/collection/v1/collection_config.proto\"A\n" +
	"\x16ListCollectionsRequest\x12'\n" +
	"\n" +
	"account_id\x18\x01 \x01(\tB\b\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"n\n" +
	"\x17ListCollectionsResponse\x12S\n" +
	"\vcollections\x18\x01 \x03(\v21.qdrant.cloud.serverless.collection.v1.CollectionR\vcollections\"l\n" +
	"\x17CreateCollectionRequest\x12Q\n" +
	"\n" +
	"collection\x18\x01 \x01(\v21.qdrant.cloud.serverless.collection.v1.CollectionR\n" +
	"collection\"m\n" +
	"\x18CreateCollectionResponse\x12Q\n" +
	"\n" +
	"collection\x18\x01 \x01(\v21.qdrant.cloud.serverless.collection.v1.CollectionR\n" +
	"collection\"r\n" +
	"\x18UpgradeCollectionRequest\x12'\n" +
	"\n" +
	"account_id\x18\x01 \x01(\tB\b\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12-\n" +
	"\rcollection_id\x18\x02 \x01(\tB\b\xbaH\x05r\x03\xb0\x01\x01R\fcollectionId\"\x1b\n" +
	"\x19UpgradeCollectionResponse\"q\n" +
	"\x17DeleteCollectionRequest\x12'\n" +
	"\n" +
	"account_id\x18\x01 \x01(\tB\b\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12-\n" +
	"\rcollection_id\x18\x02 \x01(\tB\b\xbaH\x05r\x03\xb0\x01\x01R\fcollectionId\"\x1a\n" +
	"\x18DeleteCollectionResponse\"\xbe\x05\n" +
	"\n" +
	"Collection\x12\x0e\n" +
	"\x02id\x18\x01 \x01(\tR\x02id\x129\n" +
	"\n" +
	"created_at\x18\x02 \x01(\v2\x1a.google.protobuf.TimestampR\tcreatedAt\x12'\n" +
	"\n" +
	"account_id\x18\x03 \x01(\tB\b\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12/\n" +
	"\x04name\x18\x04 \x01(\tB\x1b\xbaH\x18r\x16\x10\x04\x18@2\x10^[a-zA-Z0-9-_]+$R\x04name\x129\n" +
	"\n" +
	"deleted_at\x18\x05 \x01(\v2\x1a.google.protobuf.TimestampR\tdeletedAt\x123\n" +
	"\x11cloud_provider_id\x18\n" +
	" \x01(\tB\a\xbaH\x04r\x02\x10\x03R\x0fcloudProviderId\x127\n" +
	"\x18cloud_provider_region_id\x18\v \x01(\tR\x15cloudProviderRegionId\x12d\n" +
	"\rconfiguration\x18\x14 \x01(\v2>.qdrant.cloud.serverless.collection.v1.CollectionConfigurationR\rconfiguration\x12L\n" +
	"\x05state\x18d \x01(\v26.qdrant.cloud.serverless.collection.v1.CollectionStateR\x05state:\xad\x01\xbaH\xa9\x01\x1a\xa6\x01\n" +
	"\rcollection.id\x12\x1avalue must be a valid UUID\x1aythis.id.matches('^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$') || !has(this.created_at)\"\xe5\x01\n" +
	"\x0fCollectionState\x12Q\n" +
	"\x05phase\x18\x01 \x01(\x0e2;.qdrant.cloud.serverless.collection.v1.CollectionStatePhaseR\x05phase\x12\x16\n" +
	"\x06reason\x18\x02 \x01(\tR\x06reason\x12Z\n" +
	"\bendpoint\x18\a \x01(\v29.qdrant.cloud.serverless.collection.v1.CollectionEndpointH\x00R\bendpoint\x88\x01\x01B\v\n" +
	"\t_endpoint\"j\n" +
	"\x12CollectionEndpoint\x12\x1a\n" +
	"\x03url\x18\x01 \x01(\tB\b\xbaH\x05r\x03\xa8\x01\x01R\x03url\x12\x1b\n" +
	"\trest_port\x18\x02 \x01(\x05R\brestPort\x12\x1b\n" +
	"\tgrpc_port\x18\x03 \x01(\x05R\bgrpcPort*\xac\x01\n" +
	"\x14CollectionStatePhase\x12&\n" +
	"\"COLLECTION_STATE_PHASE_UNSPECIFIED\x10\x00\x12 \n" +
	"\x1cCOLLECTION_STATE_PHASE_READY\x10\x01\x12%\n" +
	"!COLLECTION_STATE_PHASE_PROCESSING\x10\x02\x12#\n" +
	"\x1fCOLLECTION_STATE_PHASE_DISABLED\x10\x032\xfd\a\n" +
	"\x11CollectionService\x12\xe2\x01\n" +
	"\x0fListCollections\x12=.qdrant.cloud.serverless.collection.v1.ListCollectionsRequest\x1a>.qdrant.cloud.serverless.collection.v1.ListCollectionsResponse\"P\x8a\xb5\x18\x10write:serverless\x82\xd3\xe4\x93\x026\x124/api/serverless/v1/accounts/{account_id}/collections\x12\x8c\x02\n" +
	"\x10CreateCollection\x12>.qdrant.cloud.serverless.collection.v1.CreateCollectionRequest\x1a?.qdrant.cloud.serverless.collection.v1.CreateCollectionResponse\"w\x8a\xb5\x18\x10write:serverless\x92\xb5\x18\x15collection.account_id\x82\xd3\xe4\x93\x02D:\x01*\"?/api/serverless/v1/accounts/{collection.account_id}/collections\x12\xfb\x01\n" +
	"\x11UpgradeCollection\x12?.qdrant.cloud.serverless.collection.v1.UpgradeCollectionRequest\x1a@.qdrant.cloud.serverless.collection.v1.UpgradeCollectionResponse\"c\x8a\xb5\x18\x10write:serverless\x82\xd3\xe4\x93\x02I:\x01*\x1aD/api/serverless/v1/accounts/{account_id}/collections/{collection_id}\x12\xf5\x01\n" +
	"\x10DeleteCollection\x12>.qdrant.cloud.serverless.collection.v1.DeleteCollectionRequest\x1a?.qdrant.cloud.serverless.collection.v1.DeleteCollectionResponse\"`\x8a\xb5\x18\x10write:serverless\x82\xd3\xe4\x93\x02F*D/api/serverless/v1/accounts/{account_id}/collections/{collection_id}B\xda\x02\n" +
	")com.qdrant.cloud.serverless.collection.v1B\x0fCollectionProtoP\x01Zcgithub.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/serverless/collection/v1;collectionv1\xa2\x02\x04QCSC\xaa\x02%Qdrant.Cloud.Serverless.Collection.V1\xca\x02%Qdrant\\Cloud\\Serverless\\Collection\\V1\xe2\x021Qdrant\\Cloud\\Serverless\\Collection\\V1\\GPBMetadata\xea\x02)Qdrant::Cloud::Serverless::Collection::V1b\x06proto3"

var (
	file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescOnce sync.Once
	file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescData []byte
)

func file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescGZIP() []byte {
	file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescOnce.Do(func() {
		file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDesc), len(file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDesc)))
	})
	return file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDescData
}

var file_qdrant_cloud_serverless_collection_v1_collection_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes = make([]protoimpl.MessageInfo, 11)
var file_qdrant_cloud_serverless_collection_v1_collection_proto_goTypes = []any{
	(CollectionStatePhase)(0),         // 0: qdrant.cloud.serverless.collection.v1.CollectionStatePhase
	(*ListCollectionsRequest)(nil),    // 1: qdrant.cloud.serverless.collection.v1.ListCollectionsRequest
	(*ListCollectionsResponse)(nil),   // 2: qdrant.cloud.serverless.collection.v1.ListCollectionsResponse
	(*CreateCollectionRequest)(nil),   // 3: qdrant.cloud.serverless.collection.v1.CreateCollectionRequest
	(*CreateCollectionResponse)(nil),  // 4: qdrant.cloud.serverless.collection.v1.CreateCollectionResponse
	(*UpgradeCollectionRequest)(nil),  // 5: qdrant.cloud.serverless.collection.v1.UpgradeCollectionRequest
	(*UpgradeCollectionResponse)(nil), // 6: qdrant.cloud.serverless.collection.v1.UpgradeCollectionResponse
	(*DeleteCollectionRequest)(nil),   // 7: qdrant.cloud.serverless.collection.v1.DeleteCollectionRequest
	(*DeleteCollectionResponse)(nil),  // 8: qdrant.cloud.serverless.collection.v1.DeleteCollectionResponse
	(*Collection)(nil),                // 9: qdrant.cloud.serverless.collection.v1.Collection
	(*CollectionState)(nil),           // 10: qdrant.cloud.serverless.collection.v1.CollectionState
	(*CollectionEndpoint)(nil),        // 11: qdrant.cloud.serverless.collection.v1.CollectionEndpoint
	(*timestamppb.Timestamp)(nil),     // 12: google.protobuf.Timestamp
	(*CollectionConfiguration)(nil),   // 13: qdrant.cloud.serverless.collection.v1.CollectionConfiguration
}
var file_qdrant_cloud_serverless_collection_v1_collection_proto_depIdxs = []int32{
	9,  // 0: qdrant.cloud.serverless.collection.v1.ListCollectionsResponse.collections:type_name -> qdrant.cloud.serverless.collection.v1.Collection
	9,  // 1: qdrant.cloud.serverless.collection.v1.CreateCollectionRequest.collection:type_name -> qdrant.cloud.serverless.collection.v1.Collection
	9,  // 2: qdrant.cloud.serverless.collection.v1.CreateCollectionResponse.collection:type_name -> qdrant.cloud.serverless.collection.v1.Collection
	12, // 3: qdrant.cloud.serverless.collection.v1.Collection.created_at:type_name -> google.protobuf.Timestamp
	12, // 4: qdrant.cloud.serverless.collection.v1.Collection.deleted_at:type_name -> google.protobuf.Timestamp
	13, // 5: qdrant.cloud.serverless.collection.v1.Collection.configuration:type_name -> qdrant.cloud.serverless.collection.v1.CollectionConfiguration
	10, // 6: qdrant.cloud.serverless.collection.v1.Collection.state:type_name -> qdrant.cloud.serverless.collection.v1.CollectionState
	0,  // 7: qdrant.cloud.serverless.collection.v1.CollectionState.phase:type_name -> qdrant.cloud.serverless.collection.v1.CollectionStatePhase
	11, // 8: qdrant.cloud.serverless.collection.v1.CollectionState.endpoint:type_name -> qdrant.cloud.serverless.collection.v1.CollectionEndpoint
	1,  // 9: qdrant.cloud.serverless.collection.v1.CollectionService.ListCollections:input_type -> qdrant.cloud.serverless.collection.v1.ListCollectionsRequest
	3,  // 10: qdrant.cloud.serverless.collection.v1.CollectionService.CreateCollection:input_type -> qdrant.cloud.serverless.collection.v1.CreateCollectionRequest
	5,  // 11: qdrant.cloud.serverless.collection.v1.CollectionService.UpgradeCollection:input_type -> qdrant.cloud.serverless.collection.v1.UpgradeCollectionRequest
	7,  // 12: qdrant.cloud.serverless.collection.v1.CollectionService.DeleteCollection:input_type -> qdrant.cloud.serverless.collection.v1.DeleteCollectionRequest
	2,  // 13: qdrant.cloud.serverless.collection.v1.CollectionService.ListCollections:output_type -> qdrant.cloud.serverless.collection.v1.ListCollectionsResponse
	4,  // 14: qdrant.cloud.serverless.collection.v1.CollectionService.CreateCollection:output_type -> qdrant.cloud.serverless.collection.v1.CreateCollectionResponse
	6,  // 15: qdrant.cloud.serverless.collection.v1.CollectionService.UpgradeCollection:output_type -> qdrant.cloud.serverless.collection.v1.UpgradeCollectionResponse
	8,  // 16: qdrant.cloud.serverless.collection.v1.CollectionService.DeleteCollection:output_type -> qdrant.cloud.serverless.collection.v1.DeleteCollectionResponse
	13, // [13:17] is the sub-list for method output_type
	9,  // [9:13] is the sub-list for method input_type
	9,  // [9:9] is the sub-list for extension type_name
	9,  // [9:9] is the sub-list for extension extendee
	0,  // [0:9] is the sub-list for field type_name
}

func init() { file_qdrant_cloud_serverless_collection_v1_collection_proto_init() }
func file_qdrant_cloud_serverless_collection_v1_collection_proto_init() {
	if File_qdrant_cloud_serverless_collection_v1_collection_proto != nil {
		return
	}
	file_qdrant_cloud_serverless_collection_v1_collection_config_proto_init()
	file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes[9].OneofWrappers = []any{}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDesc), len(file_qdrant_cloud_serverless_collection_v1_collection_proto_rawDesc)),
			NumEnums:      1,
			NumMessages:   11,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_qdrant_cloud_serverless_collection_v1_collection_proto_goTypes,
		DependencyIndexes: file_qdrant_cloud_serverless_collection_v1_collection_proto_depIdxs,
		EnumInfos:         file_qdrant_cloud_serverless_collection_v1_collection_proto_enumTypes,
		MessageInfos:      file_qdrant_cloud_serverless_collection_v1_collection_proto_msgTypes,
	}.Build()
	File_qdrant_cloud_serverless_collection_v1_collection_proto = out.File
	file_qdrant_cloud_serverless_collection_v1_collection_proto_goTypes = nil
	file_qdrant_cloud_serverless_collection_v1_collection_proto_depIdxs = nil
}
