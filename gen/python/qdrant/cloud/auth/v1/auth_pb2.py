# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: qdrant/cloud/auth/v1/auth.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'qdrant/cloud/auth/v1/auth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from qdrant.cloud.common.v1 import common_pb2 as qdrant_dot_cloud_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fqdrant/cloud/auth/v1/auth.proto\x12\x14qdrant.cloud.auth.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a#qdrant/cloud/common/v1/common.proto\"D\n\x19ListManagementKeysRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"W\n\x1aListManagementKeysResponse\x12\x39\n\x05items\x18\x01 \x03(\x0b\x32#.qdrant.cloud.auth.v1.ManagementKeyR\x05items\"h\n\x1a\x43reateManagementKeyRequest\x12J\n\x0emanagement_key\x18\x01 \x01(\x0b\x32#.qdrant.cloud.auth.v1.ManagementKeyR\rmanagementKey\"i\n\x1b\x43reateManagementKeyResponse\x12J\n\x0emanagement_key\x18\x01 \x01(\x0b\x32#.qdrant.cloud.auth.v1.ManagementKeyR\rmanagementKey\"{\n\x1a\x44\x65leteManagementKeyRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\x34\n\x11management_key_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\x0fmanagementKeyId\"\x1d\n\x1b\x44\x65leteManagementKeyResponse\"\xda\x02\n\rManagementKey\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\'\n\naccount_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\x39\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x16\n\x06prefix\x18\x04 \x01(\tR\x06prefix\x12\x10\n\x03key\x18\x05 \x01(\tR\x03key:\xaa\x01\xbaH\xa6\x01\x1a\xa3\x01\n\napi_key.id\x12\x1avalue must be a valid UUID\x1aythis.id.matches(\'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$\') || !has(this.created_at)2\xc4\x05\n\x0b\x41uthService\x12\xcb\x01\n\x12ListManagementKeys\x12/.qdrant.cloud.auth.v1.ListManagementKeysRequest\x1a\x30.qdrant.cloud.auth.v1.ListManagementKeysResponse\"R\x8a\xb5\x18\x14read:management_keys\x82\xd3\xe4\x93\x02\x34\x12\x32/api/auth/v1/accounts/{account_id}/management-keys\x12\xff\x01\n\x13\x43reateManagementKey\x12\x30.qdrant.cloud.auth.v1.CreateManagementKeyRequest\x1a\x31.qdrant.cloud.auth.v1.CreateManagementKeyResponse\"\x82\x01\x8a\xb5\x18\x15write:management_keys\x92\xb5\x18\x19management_key.account_id\x82\xd3\xe4\x93\x02\x46\"A/api/auth/v1/accounts/{management_key.account_id}/management-keys:\x01*\x12\xe4\x01\n\x13\x44\x65leteManagementKey\x12\x30.qdrant.cloud.auth.v1.DeleteManagementKeyRequest\x1a\x31.qdrant.cloud.auth.v1.DeleteManagementKeyResponse\"h\x8a\xb5\x18\x16\x64\x65lete:management_keys\x82\xd3\xe4\x93\x02H*F/api/auth/v1/accounts/{account_id}/management-keys/{management_key_id}B\xe6\x01\n\x18\x63om.qdrant.cloud.auth.v1B\tAuthProtoP\x01ZLgithub.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/auth/v1;authv1\xa2\x02\x03QCA\xaa\x02\x14Qdrant.Cloud.Auth.V1\xca\x02\x14Qdrant\\Cloud\\Auth\\V1\xe2\x02 Qdrant\\Cloud\\Auth\\V1\\GPBMetadata\xea\x02\x17Qdrant::Cloud::Auth::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qdrant.cloud.auth.v1.auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.qdrant.cloud.auth.v1B\tAuthProtoP\001ZLgithub.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/auth/v1;authv1\242\002\003QCA\252\002\024Qdrant.Cloud.Auth.V1\312\002\024Qdrant\\Cloud\\Auth\\V1\342\002 Qdrant\\Cloud\\Auth\\V1\\GPBMetadata\352\002\027Qdrant::Cloud::Auth::V1'
  _globals['_LISTMANAGEMENTKEYSREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_LISTMANAGEMENTKEYSREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_DELETEMANAGEMENTKEYREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_DELETEMANAGEMENTKEYREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_DELETEMANAGEMENTKEYREQUEST'].fields_by_name['management_key_id']._loaded_options = None
  _globals['_DELETEMANAGEMENTKEYREQUEST'].fields_by_name['management_key_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_MANAGEMENTKEY'].fields_by_name['account_id']._loaded_options = None
  _globals['_MANAGEMENTKEY'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_MANAGEMENTKEY']._loaded_options = None
  _globals['_MANAGEMENTKEY']._serialized_options = b'\272H\246\001\032\243\001\n\napi_key.id\022\032value must be a valid UUID\032ythis.id.matches(\'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$\') || !has(this.created_at)'
  _globals['_AUTHSERVICE'].methods_by_name['ListManagementKeys']._loaded_options = None
  _globals['_AUTHSERVICE'].methods_by_name['ListManagementKeys']._serialized_options = b'\212\265\030\024read:management_keys\202\323\344\223\0024\0222/api/auth/v1/accounts/{account_id}/management-keys'
  _globals['_AUTHSERVICE'].methods_by_name['CreateManagementKey']._loaded_options = None
  _globals['_AUTHSERVICE'].methods_by_name['CreateManagementKey']._serialized_options = b'\212\265\030\025write:management_keys\222\265\030\031management_key.account_id\202\323\344\223\002F\"A/api/auth/v1/accounts/{management_key.account_id}/management-keys:\001*'
  _globals['_AUTHSERVICE'].methods_by_name['DeleteManagementKey']._loaded_options = None
  _globals['_AUTHSERVICE'].methods_by_name['DeleteManagementKey']._serialized_options = b'\212\265\030\026delete:management_keys\202\323\344\223\002H*F/api/auth/v1/accounts/{account_id}/management-keys/{management_key_id}'
  _globals['_LISTMANAGEMENTKEYSREQUEST']._serialized_start=186
  _globals['_LISTMANAGEMENTKEYSREQUEST']._serialized_end=254
  _globals['_LISTMANAGEMENTKEYSRESPONSE']._serialized_start=256
  _globals['_LISTMANAGEMENTKEYSRESPONSE']._serialized_end=343
  _globals['_CREATEMANAGEMENTKEYREQUEST']._serialized_start=345
  _globals['_CREATEMANAGEMENTKEYREQUEST']._serialized_end=449
  _globals['_CREATEMANAGEMENTKEYRESPONSE']._serialized_start=451
  _globals['_CREATEMANAGEMENTKEYRESPONSE']._serialized_end=556
  _globals['_DELETEMANAGEMENTKEYREQUEST']._serialized_start=558
  _globals['_DELETEMANAGEMENTKEYREQUEST']._serialized_end=681
  _globals['_DELETEMANAGEMENTKEYRESPONSE']._serialized_start=683
  _globals['_DELETEMANAGEMENTKEYRESPONSE']._serialized_end=712
  _globals['_MANAGEMENTKEY']._serialized_start=715
  _globals['_MANAGEMENTKEY']._serialized_end=1061
  _globals['_AUTHSERVICE']._serialized_start=1064
  _globals['_AUTHSERVICE']._serialized_end=1772
# @@protoc_insertion_point(module_scope)
