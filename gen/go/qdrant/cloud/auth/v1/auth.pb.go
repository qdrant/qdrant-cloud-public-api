// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.4
// 	protoc        (unknown)
// source: qdrant/cloud/auth/v1/auth.proto

package authv1

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

// ListManagementKeysRequest is the request for the ListManagementKeys function
type ListManagementKeysRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The identifier of the account (in GUID format).
	// This is a required field.
	AccountId     string `protobuf:"bytes,1,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListManagementKeysRequest) Reset() {
	*x = ListManagementKeysRequest{}
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListManagementKeysRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListManagementKeysRequest) ProtoMessage() {}

func (x *ListManagementKeysRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListManagementKeysRequest.ProtoReflect.Descriptor instead.
func (*ListManagementKeysRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_auth_v1_auth_proto_rawDescGZIP(), []int{0}
}

func (x *ListManagementKeysRequest) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

// ListManagementKeysResponse is the response from the ListManagementKeys function
type ListManagementKeysResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The actual management keys in this list.
	Items         []*ManagementKey `protobuf:"bytes,1,rep,name=items,proto3" json:"items,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListManagementKeysResponse) Reset() {
	*x = ListManagementKeysResponse{}
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListManagementKeysResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListManagementKeysResponse) ProtoMessage() {}

func (x *ListManagementKeysResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListManagementKeysResponse.ProtoReflect.Descriptor instead.
func (*ListManagementKeysResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_auth_v1_auth_proto_rawDescGZIP(), []int{1}
}

func (x *ListManagementKeysResponse) GetItems() []*ManagementKey {
	if x != nil {
		return x.Items
	}
	return nil
}

// CreateManagementKeyRequest is the request for the CreateManagementKey function
type CreateManagementKeyRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The actual management key.
	ManagementKey *ManagementKey `protobuf:"bytes,1,opt,name=management_key,json=managementKey,proto3" json:"management_key,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CreateManagementKeyRequest) Reset() {
	*x = CreateManagementKeyRequest{}
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreateManagementKeyRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateManagementKeyRequest) ProtoMessage() {}

func (x *CreateManagementKeyRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateManagementKeyRequest.ProtoReflect.Descriptor instead.
func (*CreateManagementKeyRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_auth_v1_auth_proto_rawDescGZIP(), []int{2}
}

func (x *CreateManagementKeyRequest) GetManagementKey() *ManagementKey {
	if x != nil {
		return x.ManagementKey
	}
	return nil
}

// CreateManagementKeyResponse is the response from the CreateManagementKey function
type CreateManagementKeyResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The actual management key.
	ManagementKey *ManagementKey `protobuf:"bytes,1,opt,name=management_key,json=managementKey,proto3" json:"management_key,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CreateManagementKeyResponse) Reset() {
	*x = CreateManagementKeyResponse{}
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreateManagementKeyResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateManagementKeyResponse) ProtoMessage() {}

func (x *CreateManagementKeyResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateManagementKeyResponse.ProtoReflect.Descriptor instead.
func (*CreateManagementKeyResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_auth_v1_auth_proto_rawDescGZIP(), []int{3}
}

func (x *CreateManagementKeyResponse) GetManagementKey() *ManagementKey {
	if x != nil {
		return x.ManagementKey
	}
	return nil
}

// DeleteManagementKeyRequest is the request for the DeleteManagementKey function
type DeleteManagementKeyRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// The identifier of the account (in GUID format).
	// This is a required field.
	AccountId string `protobuf:"bytes,1,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	// The identifier of the management key (in GUID format).
	// This is a required field.
	ManagementKeyId string `protobuf:"bytes,2,opt,name=management_key_id,json=managementKeyId,proto3" json:"management_key_id,omitempty"`
	unknownFields   protoimpl.UnknownFields
	sizeCache       protoimpl.SizeCache
}

func (x *DeleteManagementKeyRequest) Reset() {
	*x = DeleteManagementKeyRequest{}
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DeleteManagementKeyRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DeleteManagementKeyRequest) ProtoMessage() {}

func (x *DeleteManagementKeyRequest) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DeleteManagementKeyRequest.ProtoReflect.Descriptor instead.
func (*DeleteManagementKeyRequest) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_auth_v1_auth_proto_rawDescGZIP(), []int{4}
}

func (x *DeleteManagementKeyRequest) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

func (x *DeleteManagementKeyRequest) GetManagementKeyId() string {
	if x != nil {
		return x.ManagementKeyId
	}
	return ""
}

// DeleteManagementKeyResponse is the response from the DeleteManagementKey function
type DeleteManagementKeyResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *DeleteManagementKeyResponse) Reset() {
	*x = DeleteManagementKeyResponse{}
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DeleteManagementKeyResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DeleteManagementKeyResponse) ProtoMessage() {}

func (x *DeleteManagementKeyResponse) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DeleteManagementKeyResponse.ProtoReflect.Descriptor instead.
func (*DeleteManagementKeyResponse) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_auth_v1_auth_proto_rawDescGZIP(), []int{5}
}

// A ManagementKey represents a management key of a Qdrant Cloud account.
// This management key grants access to the Qdrant Cloud API.
type ManagementKey struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// Unique identifier for the management key (in GUID format).
	// This is a read-only field and will be available after a management key is created.
	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// The identifier of the account (in GUID format).
	// This is a required field.
	AccountId string `protobuf:"bytes,2,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	// Timestamp when the management key was created.
	// This is a read-only field and will be available after a management key is created.
	CreatedAt *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	// Prefix for the management key, this represents the first bytes of the key.
	// This is a read-only field and will be available after a management key is created.
	Prefix string `protobuf:"bytes,4,opt,name=prefix,proto3" json:"prefix,omitempty"`
	// The value of the key, to be used to authenticate requests to the Qdrant Cloud API.
	// This is a read-only field and will be available only once in the response of CreateManagementKey.
	// You should securely store this key and it should be handled as a secret.
	Key           string `protobuf:"bytes,5,opt,name=key,proto3" json:"key,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ManagementKey) Reset() {
	*x = ManagementKey{}
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ManagementKey) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ManagementKey) ProtoMessage() {}

func (x *ManagementKey) ProtoReflect() protoreflect.Message {
	mi := &file_qdrant_cloud_auth_v1_auth_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ManagementKey.ProtoReflect.Descriptor instead.
func (*ManagementKey) Descriptor() ([]byte, []int) {
	return file_qdrant_cloud_auth_v1_auth_proto_rawDescGZIP(), []int{6}
}

func (x *ManagementKey) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *ManagementKey) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

func (x *ManagementKey) GetCreatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.CreatedAt
	}
	return nil
}

func (x *ManagementKey) GetPrefix() string {
	if x != nil {
		return x.Prefix
	}
	return ""
}

func (x *ManagementKey) GetKey() string {
	if x != nil {
		return x.Key
	}
	return ""
}

var File_qdrant_cloud_auth_v1_auth_proto protoreflect.FileDescriptor

var file_qdrant_cloud_auth_v1_auth_proto_rawDesc = string([]byte{
	0x0a, 0x1f, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2f, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2f, 0x61,
	0x75, 0x74, 0x68, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x75, 0x74, 0x68, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x12, 0x14, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e,
	0x61, 0x75, 0x74, 0x68, 0x2e, 0x76, 0x31, 0x1a, 0x1b, 0x62, 0x75, 0x66, 0x2f, 0x76, 0x61, 0x6c,
	0x69, 0x64, 0x61, 0x74, 0x65, 0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69,
	0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x1a, 0x23, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2f, 0x63, 0x6c, 0x6f, 0x75,
	0x64, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2f, 0x76, 0x31, 0x2f, 0x63, 0x6f, 0x6d, 0x6d,
	0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x44, 0x0a, 0x19, 0x4c, 0x69, 0x73, 0x74,
	0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x73, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x27, 0x0a, 0x0a, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74,
	0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42, 0x08, 0xba, 0x48, 0x05, 0x72, 0x03,
	0xb0, 0x01, 0x01, 0x52, 0x09, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x49, 0x64, 0x22, 0x57,
	0x0a, 0x1a, 0x4c, 0x69, 0x73, 0x74, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74,
	0x4b, 0x65, 0x79, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x39, 0x0a, 0x05,
	0x69, 0x74, 0x65, 0x6d, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x23, 0x2e, 0x71, 0x64,
	0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x61, 0x75, 0x74, 0x68, 0x2e,
	0x76, 0x31, 0x2e, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79,
	0x52, 0x05, 0x69, 0x74, 0x65, 0x6d, 0x73, 0x22, 0x68, 0x0a, 0x1a, 0x43, 0x72, 0x65, 0x61, 0x74,
	0x65, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x4a, 0x0a, 0x0e, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d,
	0x65, 0x6e, 0x74, 0x5f, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x23, 0x2e,
	0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x61, 0x75, 0x74,
	0x68, 0x2e, 0x76, 0x31, 0x2e, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b,
	0x65, 0x79, 0x52, 0x0d, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65,
	0x79, 0x22, 0x69, 0x0a, 0x1b, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x4d, 0x61, 0x6e, 0x61, 0x67,
	0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65,
	0x12, 0x4a, 0x0a, 0x0e, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x6b,
	0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x23, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e,
	0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x61, 0x75, 0x74, 0x68, 0x2e, 0x76, 0x31, 0x2e,
	0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x52, 0x0d, 0x6d,
	0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x22, 0x7b, 0x0a, 0x1a,
	0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74,
	0x4b, 0x65, 0x79, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x27, 0x0a, 0x0a, 0x61, 0x63,
	0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42, 0x08,
	0xba, 0x48, 0x05, 0x72, 0x03, 0xb0, 0x01, 0x01, 0x52, 0x09, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e,
	0x74, 0x49, 0x64, 0x12, 0x34, 0x0a, 0x11, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e,
	0x74, 0x5f, 0x6b, 0x65, 0x79, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x42, 0x08,
	0xba, 0x48, 0x05, 0x72, 0x03, 0xb0, 0x01, 0x01, 0x52, 0x0f, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65,
	0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x49, 0x64, 0x22, 0x1d, 0x0a, 0x1b, 0x44, 0x65, 0x6c,
	0x65, 0x74, 0x65, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0xda, 0x02, 0x0a, 0x0d, 0x4d, 0x61, 0x6e,
	0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64, 0x12, 0x27, 0x0a, 0x0a, 0x61, 0x63,
	0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x42, 0x08,
	0xba, 0x48, 0x05, 0x72, 0x03, 0xb0, 0x01, 0x01, 0x52, 0x09, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e,
	0x74, 0x49, 0x64, 0x12, 0x39, 0x0a, 0x0a, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x61,
	0x74, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74,
	0x61, 0x6d, 0x70, 0x52, 0x09, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x41, 0x74, 0x12, 0x16,
	0x0a, 0x06, 0x70, 0x72, 0x65, 0x66, 0x69, 0x78, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06,
	0x70, 0x72, 0x65, 0x66, 0x69, 0x78, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x05, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x3a, 0xaa, 0x01, 0xba, 0x48, 0xa6, 0x01, 0x1a,
	0xa3, 0x01, 0x0a, 0x0a, 0x61, 0x70, 0x69, 0x5f, 0x6b, 0x65, 0x79, 0x2e, 0x69, 0x64, 0x12, 0x1a,
	0x76, 0x61, 0x6c, 0x75, 0x65, 0x20, 0x6d, 0x75, 0x73, 0x74, 0x20, 0x62, 0x65, 0x20, 0x61, 0x20,
	0x76, 0x61, 0x6c, 0x69, 0x64, 0x20, 0x55, 0x55, 0x49, 0x44, 0x1a, 0x79, 0x74, 0x68, 0x69, 0x73,
	0x2e, 0x69, 0x64, 0x2e, 0x6d, 0x61, 0x74, 0x63, 0x68, 0x65, 0x73, 0x28, 0x27, 0x5e, 0x5b, 0x30,
	0x2d, 0x39, 0x61, 0x2d, 0x66, 0x41, 0x2d, 0x46, 0x5d, 0x7b, 0x38, 0x7d, 0x2d, 0x5b, 0x30, 0x2d,
	0x39, 0x61, 0x2d, 0x66, 0x41, 0x2d, 0x46, 0x5d, 0x7b, 0x34, 0x7d, 0x2d, 0x5b, 0x30, 0x2d, 0x39,
	0x61, 0x2d, 0x66, 0x41, 0x2d, 0x46, 0x5d, 0x7b, 0x34, 0x7d, 0x2d, 0x5b, 0x30, 0x2d, 0x39, 0x61,
	0x2d, 0x66, 0x41, 0x2d, 0x46, 0x5d, 0x7b, 0x34, 0x7d, 0x2d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d,
	0x66, 0x41, 0x2d, 0x46, 0x5d, 0x7b, 0x31, 0x32, 0x7d, 0x24, 0x27, 0x29, 0x20, 0x7c, 0x7c, 0x20,
	0x21, 0x68, 0x61, 0x73, 0x28, 0x74, 0x68, 0x69, 0x73, 0x2e, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65,
	0x64, 0x5f, 0x61, 0x74, 0x29, 0x32, 0xc4, 0x05, 0x0a, 0x0b, 0x41, 0x75, 0x74, 0x68, 0x53, 0x65,
	0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0xcb, 0x01, 0x0a, 0x12, 0x4c, 0x69, 0x73, 0x74, 0x4d, 0x61,
	0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x73, 0x12, 0x2f, 0x2e, 0x71,
	0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x61, 0x75, 0x74, 0x68,
	0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65,
	0x6e, 0x74, 0x4b, 0x65, 0x79, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x30, 0x2e,
	0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x61, 0x75, 0x74,
	0x68, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d,
	0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22,
	0x52, 0x8a, 0xb5, 0x18, 0x14, 0x72, 0x65, 0x61, 0x64, 0x3a, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65,
	0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x6b, 0x65, 0x79, 0x73, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x34, 0x12,
	0x32, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x61, 0x75, 0x74, 0x68, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x63,
	0x63, 0x6f, 0x75, 0x6e, 0x74, 0x73, 0x2f, 0x7b, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f,
	0x69, 0x64, 0x7d, 0x2f, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x2d, 0x6b,
	0x65, 0x79, 0x73, 0x12, 0xff, 0x01, 0x0a, 0x13, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x4d, 0x61,
	0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x12, 0x30, 0x2e, 0x71, 0x64,
	0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x61, 0x75, 0x74, 0x68, 0x2e,
	0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d,
	0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x31, 0x2e,
	0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x61, 0x75, 0x74,
	0x68, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x4d, 0x61, 0x6e, 0x61, 0x67,
	0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65,
	0x22, 0x82, 0x01, 0x8a, 0xb5, 0x18, 0x15, 0x77, 0x72, 0x69, 0x74, 0x65, 0x3a, 0x6d, 0x61, 0x6e,
	0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x6b, 0x65, 0x79, 0x73, 0x92, 0xb5, 0x18, 0x19,
	0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x6b, 0x65, 0x79, 0x2e, 0x61,
	0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x46, 0x3a,
	0x01, 0x2a, 0x22, 0x41, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x61, 0x75, 0x74, 0x68, 0x2f, 0x76, 0x31,
	0x2f, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x73, 0x2f, 0x7b, 0x6d, 0x61, 0x6e, 0x61, 0x67,
	0x65, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x6b, 0x65, 0x79, 0x2e, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e,
	0x74, 0x5f, 0x69, 0x64, 0x7d, 0x2f, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74,
	0x2d, 0x6b, 0x65, 0x79, 0x73, 0x12, 0xe4, 0x01, 0x0a, 0x13, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65,
	0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x12, 0x30, 0x2e,
	0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x61, 0x75, 0x74,
	0x68, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x4d, 0x61, 0x6e, 0x61, 0x67,
	0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x31, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x61,
	0x75, 0x74, 0x68, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x4d, 0x61, 0x6e,
	0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x4b, 0x65, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x22, 0x68, 0x8a, 0xb5, 0x18, 0x16, 0x64, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x3a, 0x6d,
	0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x6b, 0x65, 0x79, 0x73, 0x82, 0xd3,
	0xe4, 0x93, 0x02, 0x48, 0x2a, 0x46, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x61, 0x75, 0x74, 0x68, 0x2f,
	0x76, 0x31, 0x2f, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x73, 0x2f, 0x7b, 0x61, 0x63, 0x63,
	0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x7d, 0x2f, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d,
	0x65, 0x6e, 0x74, 0x2d, 0x6b, 0x65, 0x79, 0x73, 0x2f, 0x7b, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65,
	0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x6b, 0x65, 0x79, 0x5f, 0x69, 0x64, 0x7d, 0x42, 0xe6, 0x01, 0x0a,
	0x18, 0x63, 0x6f, 0x6d, 0x2e, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2e, 0x63, 0x6c, 0x6f, 0x75,
	0x64, 0x2e, 0x61, 0x75, 0x74, 0x68, 0x2e, 0x76, 0x31, 0x42, 0x09, 0x41, 0x75, 0x74, 0x68, 0x50,
	0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a, 0x4c, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63,
	0x6f, 0x6d, 0x2f, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2f, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74,
	0x2d, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2d, 0x70, 0x75, 0x62, 0x6c, 0x69, 0x63, 0x2d, 0x61, 0x70,
	0x69, 0x2f, 0x67, 0x65, 0x6e, 0x2f, 0x67, 0x6f, 0x2f, 0x71, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x2f,
	0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2f, 0x61, 0x75, 0x74, 0x68, 0x2f, 0x76, 0x31, 0x3b, 0x61, 0x75,
	0x74, 0x68, 0x76, 0x31, 0xa2, 0x02, 0x03, 0x51, 0x43, 0x41, 0xaa, 0x02, 0x14, 0x51, 0x64, 0x72,
	0x61, 0x6e, 0x74, 0x2e, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x41, 0x75, 0x74, 0x68, 0x2e, 0x56,
	0x31, 0xca, 0x02, 0x14, 0x51, 0x64, 0x72, 0x61, 0x6e, 0x74, 0x5c, 0x43, 0x6c, 0x6f, 0x75, 0x64,
	0x5c, 0x41, 0x75, 0x74, 0x68, 0x5c, 0x56, 0x31, 0xe2, 0x02, 0x20, 0x51, 0x64, 0x72, 0x61, 0x6e,
	0x74, 0x5c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x5c, 0x41, 0x75, 0x74, 0x68, 0x5c, 0x56, 0x31, 0x5c,
	0x47, 0x50, 0x42, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0xea, 0x02, 0x17, 0x51, 0x64,
	0x72, 0x61, 0x6e, 0x74, 0x3a, 0x3a, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x3a, 0x3a, 0x41, 0x75, 0x74,
	0x68, 0x3a, 0x3a, 0x56, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
})

var (
	file_qdrant_cloud_auth_v1_auth_proto_rawDescOnce sync.Once
	file_qdrant_cloud_auth_v1_auth_proto_rawDescData []byte
)

func file_qdrant_cloud_auth_v1_auth_proto_rawDescGZIP() []byte {
	file_qdrant_cloud_auth_v1_auth_proto_rawDescOnce.Do(func() {
		file_qdrant_cloud_auth_v1_auth_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_qdrant_cloud_auth_v1_auth_proto_rawDesc), len(file_qdrant_cloud_auth_v1_auth_proto_rawDesc)))
	})
	return file_qdrant_cloud_auth_v1_auth_proto_rawDescData
}

var file_qdrant_cloud_auth_v1_auth_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_qdrant_cloud_auth_v1_auth_proto_goTypes = []any{
	(*ListManagementKeysRequest)(nil),   // 0: qdrant.cloud.auth.v1.ListManagementKeysRequest
	(*ListManagementKeysResponse)(nil),  // 1: qdrant.cloud.auth.v1.ListManagementKeysResponse
	(*CreateManagementKeyRequest)(nil),  // 2: qdrant.cloud.auth.v1.CreateManagementKeyRequest
	(*CreateManagementKeyResponse)(nil), // 3: qdrant.cloud.auth.v1.CreateManagementKeyResponse
	(*DeleteManagementKeyRequest)(nil),  // 4: qdrant.cloud.auth.v1.DeleteManagementKeyRequest
	(*DeleteManagementKeyResponse)(nil), // 5: qdrant.cloud.auth.v1.DeleteManagementKeyResponse
	(*ManagementKey)(nil),               // 6: qdrant.cloud.auth.v1.ManagementKey
	(*timestamppb.Timestamp)(nil),       // 7: google.protobuf.Timestamp
}
var file_qdrant_cloud_auth_v1_auth_proto_depIdxs = []int32{
	6, // 0: qdrant.cloud.auth.v1.ListManagementKeysResponse.items:type_name -> qdrant.cloud.auth.v1.ManagementKey
	6, // 1: qdrant.cloud.auth.v1.CreateManagementKeyRequest.management_key:type_name -> qdrant.cloud.auth.v1.ManagementKey
	6, // 2: qdrant.cloud.auth.v1.CreateManagementKeyResponse.management_key:type_name -> qdrant.cloud.auth.v1.ManagementKey
	7, // 3: qdrant.cloud.auth.v1.ManagementKey.created_at:type_name -> google.protobuf.Timestamp
	0, // 4: qdrant.cloud.auth.v1.AuthService.ListManagementKeys:input_type -> qdrant.cloud.auth.v1.ListManagementKeysRequest
	2, // 5: qdrant.cloud.auth.v1.AuthService.CreateManagementKey:input_type -> qdrant.cloud.auth.v1.CreateManagementKeyRequest
	4, // 6: qdrant.cloud.auth.v1.AuthService.DeleteManagementKey:input_type -> qdrant.cloud.auth.v1.DeleteManagementKeyRequest
	1, // 7: qdrant.cloud.auth.v1.AuthService.ListManagementKeys:output_type -> qdrant.cloud.auth.v1.ListManagementKeysResponse
	3, // 8: qdrant.cloud.auth.v1.AuthService.CreateManagementKey:output_type -> qdrant.cloud.auth.v1.CreateManagementKeyResponse
	5, // 9: qdrant.cloud.auth.v1.AuthService.DeleteManagementKey:output_type -> qdrant.cloud.auth.v1.DeleteManagementKeyResponse
	7, // [7:10] is the sub-list for method output_type
	4, // [4:7] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_qdrant_cloud_auth_v1_auth_proto_init() }
func file_qdrant_cloud_auth_v1_auth_proto_init() {
	if File_qdrant_cloud_auth_v1_auth_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_qdrant_cloud_auth_v1_auth_proto_rawDesc), len(file_qdrant_cloud_auth_v1_auth_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_qdrant_cloud_auth_v1_auth_proto_goTypes,
		DependencyIndexes: file_qdrant_cloud_auth_v1_auth_proto_depIdxs,
		MessageInfos:      file_qdrant_cloud_auth_v1_auth_proto_msgTypes,
	}.Build()
	File_qdrant_cloud_auth_v1_auth_proto = out.File
	file_qdrant_cloud_auth_v1_auth_proto_goTypes = nil
	file_qdrant_cloud_auth_v1_auth_proto_depIdxs = nil
}
