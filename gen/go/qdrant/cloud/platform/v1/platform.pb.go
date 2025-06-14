// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.4
// 	protoc        (unknown)
// source: qdrant/cloud/platform/v1/platform.proto

package platformv1

import (
	_ "buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate"
	_ "github.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/common/v1"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
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

// ListCloudProvidersRequest is the request for the ListCloudProviders function.
type ListCloudProvidersRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The identifier of the account (in GUID format).
	// This is a required field.
	AccountId     string `protobuf:"bytes,1,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListCloudProvidersRequest) Reset() {
	*x = ListCloudProvidersRequest{}
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListCloudProvidersRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListCloudProvidersRequest) ProtoMessage() {}

func (x *ListCloudProvidersRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListCloudProvidersRequest.ProtoReflect.Descriptor instead.
func (*ListCloudProvidersRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP(), []int{0}
}

func (x *ListCloudProvidersRequest) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

// ListCloudProvidersResponse is the response from the ListCloudProviders function.
type ListCloudProvidersResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The cloud providers
	Items         []*CloudProvider `protobuf:"bytes,1,rep,name=items,proto3" json:"items,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListCloudProvidersResponse) Reset() {
	*x = ListCloudProvidersResponse{}
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListCloudProvidersResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListCloudProvidersResponse) ProtoMessage() {}

func (x *ListCloudProvidersResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListCloudProvidersResponse.ProtoReflect.Descriptor instead.
func (*ListCloudProvidersResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP(), []int{1}
}

func (x *ListCloudProvidersResponse) GetItems() []*CloudProvider {
	if x != nil {
		return x.Items
	}
	return nil
}

// ListGlobalCloudProvidersRequest is the request from the ListGlobalCloudProviders function.
type ListGlobalCloudProvidersRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListGlobalCloudProvidersRequest) Reset() {
	*x = ListGlobalCloudProvidersRequest{}
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListGlobalCloudProvidersRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListGlobalCloudProvidersRequest) ProtoMessage() {}

func (x *ListGlobalCloudProvidersRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListGlobalCloudProvidersRequest.ProtoReflect.Descriptor instead.
func (*ListGlobalCloudProvidersRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP(), []int{2}
}

// ListGlobalCloudProvidersResponse is the response from the ListGlobalCloudProviders function.
type ListGlobalCloudProvidersResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The cloud providers
	Items         []*CloudProvider `protobuf:"bytes,1,rep,name=items,proto3" json:"items,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListGlobalCloudProvidersResponse) Reset() {
	*x = ListGlobalCloudProvidersResponse{}
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListGlobalCloudProvidersResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListGlobalCloudProvidersResponse) ProtoMessage() {}

func (x *ListGlobalCloudProvidersResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListGlobalCloudProvidersResponse.ProtoReflect.Descriptor instead.
func (*ListGlobalCloudProvidersResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP(), []int{3}
}

func (x *ListGlobalCloudProvidersResponse) GetItems() []*CloudProvider {
	if x != nil {
		return x.Items
	}
	return nil
}

// ListGlobalCloudProviderRegionsRequest is the request for the ListGlobalCloudProviderRegions function.
type ListGlobalCloudProviderRegionsRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The identifier for the cloud provider. One of the providers from response of the ListCloudProviders function.
	// This is a required field.
	CloudProviderId string `protobuf:"bytes,1,opt,name=cloud_provider_id,json=cloudProviderId,proto3" json:"cloud_provider_id,omitempty"`
	unknownFields   protoimpl.UnknownFields
	sizeCache       protoimpl.SizeCache
}

func (x *ListGlobalCloudProviderRegionsRequest) Reset() {
	*x = ListGlobalCloudProviderRegionsRequest{}
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListGlobalCloudProviderRegionsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListGlobalCloudProviderRegionsRequest) ProtoMessage() {}

func (x *ListGlobalCloudProviderRegionsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListGlobalCloudProviderRegionsRequest.ProtoReflect.Descriptor instead.
func (*ListGlobalCloudProviderRegionsRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP(), []int{4}
}

func (x *ListGlobalCloudProviderRegionsRequest) GetCloudProviderId() string {
	if x != nil {
		return x.CloudProviderId
	}
	return ""
}

// ListGlobalCloudProviderRegionsResponse is the response from the ListGlobalCloudProviderRegions function.
type ListGlobalCloudProviderRegionsResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The cloud provider regions.
	Items         []*CloudProviderRegion `protobuf:"bytes,1,rep,name=items,proto3" json:"items,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListGlobalCloudProviderRegionsResponse) Reset() {
	*x = ListGlobalCloudProviderRegionsResponse{}
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListGlobalCloudProviderRegionsResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListGlobalCloudProviderRegionsResponse) ProtoMessage() {}

func (x *ListGlobalCloudProviderRegionsResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListGlobalCloudProviderRegionsResponse.ProtoReflect.Descriptor instead.
func (*ListGlobalCloudProviderRegionsResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP(), []int{5}
}

func (x *ListGlobalCloudProviderRegionsResponse) GetItems() []*CloudProviderRegion {
	if x != nil {
		return x.Items
	}
	return nil
}

// ListCloudProviderRegionsRequest is the request for the ListCloudProviderRegions function.
type ListCloudProviderRegionsRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The identifier of the account (in GUID format).
	// This is a required field.
	AccountId string `protobuf:"bytes,1,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	// The identifier for the cloud provider. One of the providers from response of the ListCloudProviders function.
	// This is a required field.
	CloudProviderId string `protobuf:"bytes,2,opt,name=cloud_provider_id,json=cloudProviderId,proto3" json:"cloud_provider_id,omitempty"`
	unknownFields   protoimpl.UnknownFields
	sizeCache       protoimpl.SizeCache
}

func (x *ListCloudProviderRegionsRequest) Reset() {
	*x = ListCloudProviderRegionsRequest{}
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListCloudProviderRegionsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListCloudProviderRegionsRequest) ProtoMessage() {}

func (x *ListCloudProviderRegionsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListCloudProviderRegionsRequest.ProtoReflect.Descriptor instead.
func (*ListCloudProviderRegionsRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP(), []int{6}
}

func (x *ListCloudProviderRegionsRequest) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

func (x *ListCloudProviderRegionsRequest) GetCloudProviderId() string {
	if x != nil {
		return x.CloudProviderId
	}
	return ""
}

// ListCloudProviderRegionsResponse is the response from the ListCloudProviderRegions function.
type ListCloudProviderRegionsResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The cloud provider regions.
	Items         []*CloudProviderRegion `protobuf:"bytes,1,rep,name=items,proto3" json:"items,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListCloudProviderRegionsResponse) Reset() {
	*x = ListCloudProviderRegionsResponse{}
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[7]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListCloudProviderRegionsResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListCloudProviderRegionsResponse) ProtoMessage() {}

func (x *ListCloudProviderRegionsResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[7]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListCloudProviderRegionsResponse.ProtoReflect.Descriptor instead.
func (*ListCloudProviderRegionsResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP(), []int{7}
}

func (x *ListCloudProviderRegionsResponse) GetItems() []*CloudProviderRegion {
	if x != nil {
		return x.Items
	}
	return nil
}

// CloudProvider represents a cloud provider identifier and name.
type CloudProvider struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The identifier for the cloud provider.
	// e.g. "aws", "gcp", "azure", "hybrid".
	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// The human-readable name of the cloud provider.
	// e.g. "Amazon Web Services", "Google Cloud", "Microsoft Azure", "Hybrid Cloud".
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	// Whether the cloud provider is part of the free-tier offering.
	FreeTier bool `protobuf:"varint,3,opt,name=free_tier,json=freeTier,proto3" json:"free_tier,omitempty"`
	// Indicates whether the cloud provider is available for the use case.
	Available     bool `protobuf:"varint,4,opt,name=available,proto3" json:"available,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CloudProvider) Reset() {
	*x = CloudProvider{}
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[8]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CloudProvider) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CloudProvider) ProtoMessage() {}

func (x *CloudProvider) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[8]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CloudProvider.ProtoReflect.Descriptor instead.
func (*CloudProvider) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP(), []int{8}
}

func (x *CloudProvider) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *CloudProvider) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *CloudProvider) GetFreeTier() bool {
	if x != nil {
		return x.FreeTier
	}
	return false
}

func (x *CloudProvider) GetAvailable() bool {
	if x != nil {
		return x.Available
	}
	return false
}

// CloudProviderRegion represents a cloud provider region.
type CloudProviderRegion struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The identifier for the cloud provider region.
	// e.g. "us-west-1", "europe-west1", "eastus", "{UUID in case of hybrid cloud}".
	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// The human-readable name of the cloud provider region.
	// e.g. "Frankfurt", "Tokyo", etc.
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	// Whether the cloud region is part of the free-tier offering.
	FreeTier bool `protobuf:"varint,3,opt,name=free_tier,json=freeTier,proto3" json:"free_tier,omitempty"`
	// Indicates whether the cloud region is available or the hybrid cloud region is ready for clusters.
	Available bool `protobuf:"varint,4,opt,name=available,proto3" json:"available,omitempty"`
	// The identifier for the cloud provider.
	// e.g. "aws", "gcp", "azure", "openshift", "linode", "unknown".
	Provider string `protobuf:"bytes,5,opt,name=provider,proto3" json:"provider,omitempty"`
	// ISO 3166-1 alpha-2 country codes for different countries to display for each region.
	CountryIsoCode *string `protobuf:"bytes,6,opt,name=country_iso_code,json=countryIsoCode,proto3,oneof" json:"country_iso_code,omitempty"`
	// Geographic location grouping of the region.
	// e.g. "Europe", "Asia", "North America", etc.
	GeographicalSubRegion *string `protobuf:"bytes,7,opt,name=geographical_sub_region,json=geographicalSubRegion,proto3,oneof" json:"geographical_sub_region,omitempty"`
	unknownFields         protoimpl.UnknownFields
	sizeCache             protoimpl.SizeCache
}

func (x *CloudProviderRegion) Reset() {
	*x = CloudProviderRegion{}
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[9]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CloudProviderRegion) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CloudProviderRegion) ProtoMessage() {}

func (x *CloudProviderRegion) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_platform_v1_platform_proto_msgTypes[9]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CloudProviderRegion.ProtoReflect.Descriptor instead.
func (*CloudProviderRegion) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP(), []int{9}
}

func (x *CloudProviderRegion) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *CloudProviderRegion) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *CloudProviderRegion) GetFreeTier() bool {
	if x != nil {
		return x.FreeTier
	}
	return false
}

func (x *CloudProviderRegion) GetAvailable() bool {
	if x != nil {
		return x.Available
	}
	return false
}

func (x *CloudProviderRegion) GetProvider() string {
	if x != nil {
		return x.Provider
	}
	return ""
}

func (x *CloudProviderRegion) GetCountryIsoCode() string {
	if x != nil && x.CountryIsoCode != nil {
		return *x.CountryIsoCode
	}
	return ""
}

func (x *CloudProviderRegion) GetGeographicalSubRegion() string {
	if x != nil && x.GeographicalSubRegion != nil {
		return *x.GeographicalSubRegion
	}
	return ""
}

var File_qdrant_cloud_platform_v1_platform_proto protoreflect.FileDescriptor

var file_qdrant_cloud_platform_v1_platform_proto_rawDesc = string([]byte{
	0x0a, 0x27, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2f, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2f, 0x70,
	0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2f, 0x76, 0x31, 0x2f, 0x70, 0x6c, 0x61, 0x74, 0x66,
	0x6f, 0x72, 0x6d, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x18, 0x71, 0x64, 0x72, 0x61, 0x6e,
	0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d,
	0x2e, 0x76, 0x31, 0x1a, 0x1b, 0x62, 0x75, 0x66, 0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74,
	0x65, 0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e,
	0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x23,
	0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2f, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2f, 0x63, 0x6f, 0x6d,
	0x6d, 0x6f, 0x6e, 0x2f, 0x76, 0x31, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x22, 0x44, 0x0a, 0x19, 0x4c, 0x69, 0x73, 0x74, 0x43, 0x6c, 0x6f, 0x75, 0x64,
	0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x12, 0x27, 0x0a, 0x0a, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x09, 0x42, 0x08, 0xba, 0x48, 0x05, 0x72, 0x03, 0xb0, 0x01, 0x01, 0x52, 0x09,
	0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x49, 0x64, 0x22, 0x5b, 0x0a, 0x1a, 0x4c, 0x69, 0x73,
	0x74, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x73, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x3d, 0x0a, 0x05, 0x69, 0x74, 0x65, 0x6d, 0x73,
	0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x27, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e,
	0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76,
	0x31, 0x2e, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x52,
	0x05, 0x69, 0x74, 0x65, 0x6d, 0x73, 0x22, 0x21, 0x0a, 0x1f, 0x4c, 0x69, 0x73, 0x74, 0x47, 0x6c,
	0x6f, 0x62, 0x61, 0x6c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65,
	0x72, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x22, 0x61, 0x0a, 0x20, 0x4c, 0x69, 0x73,
	0x74, 0x47, 0x6c, 0x6f, 0x62, 0x61, 0x6c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76,
	0x69, 0x64, 0x65, 0x72, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x3d, 0x0a,
	0x05, 0x69, 0x74, 0x65, 0x6d, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x27, 0x2e, 0x71,
	0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74,
	0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f,
	0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x05, 0x69, 0x74, 0x65, 0x6d, 0x73, 0x22, 0x5c, 0x0a, 0x25,
	0x4c, 0x69, 0x73, 0x74, 0x47, 0x6c, 0x6f, 0x62, 0x61, 0x6c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50,
	0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x73, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x33, 0x0a, 0x11, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x5f, 0x70,
	0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x42, 0x07, 0xba, 0x48, 0x04, 0x72, 0x02, 0x10, 0x03, 0x52, 0x0f, 0x63, 0x6c, 0x6f, 0x75, 0x64,
	0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x49, 0x64, 0x22, 0x6d, 0x0a, 0x26, 0x4c, 0x69,
	0x73, 0x74, 0x47, 0x6c, 0x6f, 0x62, 0x61, 0x6c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f,
	0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x73, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x43, 0x0a, 0x05, 0x69, 0x74, 0x65, 0x6d, 0x73, 0x18, 0x01, 0x20,
	0x03, 0x28, 0x0b, 0x32, 0x2d, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f,
	0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76, 0x31, 0x2e, 0x43,
	0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69,
	0x6f, 0x6e, 0x52, 0x05, 0x69, 0x74, 0x65, 0x6d, 0x73, 0x22, 0x7f, 0x0a, 0x1f, 0x4c, 0x69, 0x73,
	0x74, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65,
	0x67, 0x69, 0x6f, 0x6e, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x27, 0x0a, 0x0a,
	0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x42, 0x08, 0xba, 0x48, 0x05, 0x72, 0x03, 0xb0, 0x01, 0x01, 0x52, 0x09, 0x61, 0x63, 0x63, 0x6f,
	0x75, 0x6e, 0x74, 0x49, 0x64, 0x12, 0x33, 0x0a, 0x11, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x5f, 0x70,
	0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09,
	0x42, 0x07, 0xba, 0x48, 0x04, 0x72, 0x02, 0x10, 0x03, 0x52, 0x0f, 0x63, 0x6c, 0x6f, 0x75, 0x64,
	0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x49, 0x64, 0x22, 0x67, 0x0a, 0x20, 0x4c, 0x69,
	0x73, 0x74, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x52,
	0x65, 0x67, 0x69, 0x6f, 0x6e, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x43,
	0x0a, 0x05, 0x69, 0x74, 0x65, 0x6d, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x2d, 0x2e,
	0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61,
	0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72,
	0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x52, 0x05, 0x69, 0x74,
	0x65, 0x6d, 0x73, 0x22, 0x6e, 0x0a, 0x0d, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76,
	0x69, 0x64, 0x65, 0x72, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x02, 0x69, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x1b, 0x0a, 0x09, 0x66, 0x72, 0x65, 0x65,
	0x5f, 0x74, 0x69, 0x65, 0x72, 0x18, 0x03, 0x20, 0x01, 0x28, 0x08, 0x52, 0x08, 0x66, 0x72, 0x65,
	0x65, 0x54, 0x69, 0x65, 0x72, 0x12, 0x1c, 0x0a, 0x09, 0x61, 0x76, 0x61, 0x69, 0x6c, 0x61, 0x62,
	0x6c, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x08, 0x52, 0x09, 0x61, 0x76, 0x61, 0x69, 0x6c, 0x61,
	0x62, 0x6c, 0x65, 0x22, 0xad, 0x02, 0x0a, 0x13, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f,
	0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x12, 0x0e, 0x0a, 0x02, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e,
	0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12,
	0x1b, 0x0a, 0x09, 0x66, 0x72, 0x65, 0x65, 0x5f, 0x74, 0x69, 0x65, 0x72, 0x18, 0x03, 0x20, 0x01,
	0x28, 0x08, 0x52, 0x08, 0x66, 0x72, 0x65, 0x65, 0x54, 0x69, 0x65, 0x72, 0x12, 0x1c, 0x0a, 0x09,
	0x61, 0x76, 0x61, 0x69, 0x6c, 0x61, 0x62, 0x6c, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x08, 0x52,
	0x09, 0x61, 0x76, 0x61, 0x69, 0x6c, 0x61, 0x62, 0x6c, 0x65, 0x12, 0x1a, 0x0a, 0x08, 0x70, 0x72,
	0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x70, 0x72,
	0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x12, 0x2d, 0x0a, 0x10, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x72,
	0x79, 0x5f, 0x69, 0x73, 0x6f, 0x5f, 0x63, 0x6f, 0x64, 0x65, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09,
	0x48, 0x00, 0x52, 0x0e, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x72, 0x79, 0x49, 0x73, 0x6f, 0x43, 0x6f,
	0x64, 0x65, 0x88, 0x01, 0x01, 0x12, 0x3b, 0x0a, 0x17, 0x67, 0x65, 0x6f, 0x67, 0x72, 0x61, 0x70,
	0x68, 0x69, 0x63, 0x61, 0x6c, 0x5f, 0x73, 0x75, 0x62, 0x5f, 0x72, 0x65, 0x67, 0x69, 0x6f, 0x6e,
	0x18, 0x07, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x15, 0x67, 0x65, 0x6f, 0x67, 0x72, 0x61,
	0x70, 0x68, 0x69, 0x63, 0x61, 0x6c, 0x53, 0x75, 0x62, 0x52, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x88,
	0x01, 0x01, 0x42, 0x13, 0x0a, 0x11, 0x5f, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x72, 0x79, 0x5f, 0x69,
	0x73, 0x6f, 0x5f, 0x63, 0x6f, 0x64, 0x65, 0x42, 0x1a, 0x0a, 0x18, 0x5f, 0x67, 0x65, 0x6f, 0x67,
	0x72, 0x61, 0x70, 0x68, 0x69, 0x63, 0x61, 0x6c, 0x5f, 0x73, 0x75, 0x62, 0x5f, 0x72, 0x65, 0x67,
	0x69, 0x6f, 0x6e, 0x32, 0xfd, 0x06, 0x0a, 0x0f, 0x50, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d,
	0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0xbf, 0x01, 0x0a, 0x18, 0x4c, 0x69, 0x73, 0x74,
	0x47, 0x6c, 0x6f, 0x62, 0x61, 0x6c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69,
	0x64, 0x65, 0x72, 0x73, 0x12, 0x39, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c,
	0x6f, 0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76, 0x31, 0x2e,
	0x4c, 0x69, 0x73, 0x74, 0x47, 0x6c, 0x6f, 0x62, 0x61, 0x6c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50,
	0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x3a, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x70,
	0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x47,
	0x6c, 0x6f, 0x62, 0x61, 0x6c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64,
	0x65, 0x72, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x2c, 0x98, 0xb5, 0x18,
	0x00, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x22, 0x12, 0x20, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x70, 0x6c,
	0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2f, 0x76, 0x31, 0x2f, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2d,
	0x70, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x73, 0x12, 0xc3, 0x01, 0x0a, 0x12, 0x4c, 0x69,
	0x73, 0x74, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x73,
	0x12, 0x33, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e,
	0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69, 0x73, 0x74,
	0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x73, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x34, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63,
	0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76, 0x31,
	0x2e, 0x4c, 0x69, 0x73, 0x74, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64,
	0x65, 0x72, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x42, 0x8a, 0xb5, 0x18,
	0x00, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x38, 0x12, 0x36, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x70, 0x6c,
	0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e,
	0x74, 0x73, 0x2f, 0x7b, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x7d, 0x2f,
	0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2d, 0x70, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x73, 0x12,
	0xed, 0x01, 0x0a, 0x1e, 0x4c, 0x69, 0x73, 0x74, 0x47, 0x6c, 0x6f, 0x62, 0x61, 0x6c, 0x43, 0x6c,
	0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69, 0x6f,
	0x6e, 0x73, 0x12, 0x3f, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75,
	0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69,
	0x73, 0x74, 0x47, 0x6c, 0x6f, 0x62, 0x61, 0x6c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f,
	0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x73, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x1a, 0x40, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f,
	0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76, 0x31, 0x2e, 0x4c,
	0x69, 0x73, 0x74, 0x47, 0x6c, 0x6f, 0x62, 0x61, 0x6c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72,
	0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x73, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x48, 0x98, 0xb5, 0x18, 0x00, 0x82, 0xd3, 0xe4, 0x93, 0x02,
	0x3e, 0x12, 0x3c, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d,
	0x2f, 0x76, 0x31, 0x2f, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2d, 0x70, 0x72, 0x6f, 0x76, 0x69, 0x64,
	0x65, 0x72, 0x73, 0x2f, 0x7b, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x5f, 0x70, 0x72, 0x6f, 0x76, 0x69,
	0x64, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x7d, 0x2f, 0x72, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x73, 0x12,
	0xf1, 0x01, 0x0a, 0x18, 0x4c, 0x69, 0x73, 0x74, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f,
	0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x39, 0x2e, 0x71,
	0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74,
	0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x43, 0x6c, 0x6f, 0x75,
	0x64, 0x50, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x73,
	0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x3a, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74,
	0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e,
	0x76, 0x31, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x50, 0x72, 0x6f, 0x76,
	0x69, 0x64, 0x65, 0x72, 0x52, 0x65, 0x67, 0x69, 0x6f, 0x6e, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x22, 0x5e, 0x8a, 0xb5, 0x18, 0x00, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x54, 0x12,
	0x52, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2f, 0x76,
	0x31, 0x2f, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x73, 0x2f, 0x7b, 0x61, 0x63, 0x63, 0x6f,
	0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x7d, 0x2f, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2d, 0x70, 0x72,
	0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x73, 0x2f, 0x7b, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x5f, 0x70,
	0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x7d, 0x2f, 0x72, 0x65, 0x67, 0x69,
	0x6f, 0x6e, 0x73, 0x42, 0x86, 0x02, 0x0a, 0x1c, 0x63, 0x6f, 0x6d, 0x2e, 0x71, 0x64, 0x72, 0x61,
	0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72,
	0x6d, 0x2e, 0x76, 0x31, 0x42, 0x0d, 0x50, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x50, 0x72,
	0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a, 0x54, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f,
	0x6d, 0x2f, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2f, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2d,
	0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2d, 0x70, 0x75, 0x62, 0x6c, 0x69, 0x63, 0x2d, 0x61, 0x70, 0x69,
	0x2f, 0x67, 0x65, 0x6e, 0x2f, 0x67, 0x6f, 0x2f, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2f, 0x63,
	0x6c, 0x6f, 0x75, 0x64, 0x2f, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2f, 0x76, 0x31,
	0x3b, 0x70, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x76, 0x31, 0xa2, 0x02, 0x03, 0x51, 0x43,
	0x50, 0xaa, 0x02, 0x18, 0x51, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x43, 0x6c, 0x6f, 0x75, 0x64,
	0x2e, 0x50, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x2e, 0x56, 0x31, 0xca, 0x02, 0x18, 0x51,
	0x64, 0x72, 0x61, 0x6e, 0x74, 0x5c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x5c, 0x50, 0x6c, 0x61, 0x74,
	0x66, 0x6f, 0x72, 0x6d, 0x5c, 0x56, 0x31, 0xe2, 0x02, 0x24, 0x51, 0x64, 0x72, 0x61, 0x6e, 0x74,
	0x5c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x5c, 0x50, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x5c,
	0x56, 0x31, 0x5c, 0x47, 0x50, 0x42, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0xea, 0x02,
	0x1b, 0x51, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x3a, 0x3a, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x3a, 0x3a,
	0x50, 0x6c, 0x61, 0x74, 0x66, 0x6f, 0x72, 0x6d, 0x3a, 0x3a, 0x56, 0x31, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
})

var (
	file_qdrant_cloud_platform_v1_platform_proto_rawDescOnce sync.Once
	file_qdrant_cloud_platform_v1_platform_proto_rawDescData []byte
)

func file_qdrant_cloud_platform_v1_platform_proto_rawDescGZIP() []byte {
	file_qdrant_cloud_platform_v1_platform_proto_rawDescOnce.Do(func() {
		file_qdrant_cloud_platform_v1_platform_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_qdrant_cloud_platform_v1_platform_proto_rawDesc), len(file_qdrant_cloud_platform_v1_platform_proto_rawDesc)))
	})
	return file_qdrant_cloud_platform_v1_platform_proto_rawDescData
}

var file_qdrant_cloud_platform_v1_platform_proto_msgTypes = make([]protoimpl.MessageInfo, 10)
var file_qdrant_cloud_platform_v1_platform_proto_goTypes = []any{
	(*ListCloudProvidersRequest)(nil),              // 0: qdrant.cloud.platform.v1.ListCloudProvidersRequest
	(*ListCloudProvidersResponse)(nil),             // 1: qdrant.cloud.platform.v1.ListCloudProvidersResponse
	(*ListGlobalCloudProvidersRequest)(nil),        // 2: qdrant.cloud.platform.v1.ListGlobalCloudProvidersRequest
	(*ListGlobalCloudProvidersResponse)(nil),       // 3: qdrant.cloud.platform.v1.ListGlobalCloudProvidersResponse
	(*ListGlobalCloudProviderRegionsRequest)(nil),  // 4: qdrant.cloud.platform.v1.ListGlobalCloudProviderRegionsRequest
	(*ListGlobalCloudProviderRegionsResponse)(nil), // 5: qdrant.cloud.platform.v1.ListGlobalCloudProviderRegionsResponse
	(*ListCloudProviderRegionsRequest)(nil),        // 6: qdrant.cloud.platform.v1.ListCloudProviderRegionsRequest
	(*ListCloudProviderRegionsResponse)(nil),       // 7: qdrant.cloud.platform.v1.ListCloudProviderRegionsResponse
	(*CloudProvider)(nil),                          // 8: qdrant.cloud.platform.v1.CloudProvider
	(*CloudProviderRegion)(nil),                    // 9: qdrant.cloud.platform.v1.CloudProviderRegion
}
var file_qdrant_cloud_platform_v1_platform_proto_depIdxs = []int32{
	8, // 0: qdrant.cloud.platform.v1.ListCloudProvidersResponse.items:type_name -> qdrant.cloud.platform.v1.CloudProvider
	8, // 1: qdrant.cloud.platform.v1.ListGlobalCloudProvidersResponse.items:type_name -> qdrant.cloud.platform.v1.CloudProvider
	9, // 2: qdrant.cloud.platform.v1.ListGlobalCloudProviderRegionsResponse.items:type_name -> qdrant.cloud.platform.v1.CloudProviderRegion
	9, // 3: qdrant.cloud.platform.v1.ListCloudProviderRegionsResponse.items:type_name -> qdrant.cloud.platform.v1.CloudProviderRegion
	2, // 4: qdrant.cloud.platform.v1.PlatformService.ListGlobalCloudProviders:input_type -> qdrant.cloud.platform.v1.ListGlobalCloudProvidersRequest
	0, // 5: qdrant.cloud.platform.v1.PlatformService.ListCloudProviders:input_type -> qdrant.cloud.platform.v1.ListCloudProvidersRequest
	4, // 6: qdrant.cloud.platform.v1.PlatformService.ListGlobalCloudProviderRegions:input_type -> qdrant.cloud.platform.v1.ListGlobalCloudProviderRegionsRequest
	6, // 7: qdrant.cloud.platform.v1.PlatformService.ListCloudProviderRegions:input_type -> qdrant.cloud.platform.v1.ListCloudProviderRegionsRequest
	3, // 8: qdrant.cloud.platform.v1.PlatformService.ListGlobalCloudProviders:output_type -> qdrant.cloud.platform.v1.ListGlobalCloudProvidersResponse
	1, // 9: qdrant.cloud.platform.v1.PlatformService.ListCloudProviders:output_type -> qdrant.cloud.platform.v1.ListCloudProvidersResponse
	5, // 10: qdrant.cloud.platform.v1.PlatformService.ListGlobalCloudProviderRegions:output_type -> qdrant.cloud.platform.v1.ListGlobalCloudProviderRegionsResponse
	7, // 11: qdrant.cloud.platform.v1.PlatformService.ListCloudProviderRegions:output_type -> qdrant.cloud.platform.v1.ListCloudProviderRegionsResponse
	8, // [8:12] is the sub-list for method output_type
	4, // [4:8] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_qdrant_cloud_platform_v1_platform_proto_init() }
func file_qdrant_cloud_platform_v1_platform_proto_init() {
	if File_qdrant_cloud_platform_v1_platform_proto != nil {
		return
	}
	file_qdrant_cloud_platform_v1_platform_proto_msgTypes[9].OneofWrappers = []any{}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_qdrant_cloud_platform_v1_platform_proto_rawDesc), len(file_qdrant_cloud_platform_v1_platform_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   10,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_qdrant_cloud_platform_v1_platform_proto_goTypes,
		DependencyIndexes: file_qdrant_cloud_platform_v1_platform_proto_depIdxs,
		MessageInfos:      file_qdrant_cloud_platform_v1_platform_proto_msgTypes,
	}.Build()
	File_qdrant_cloud_platform_v1_platform_proto = out.File
	file_qdrant_cloud_platform_v1_platform_proto_goTypes = nil
	file_qdrant_cloud_platform_v1_platform_proto_depIdxs = nil
}
