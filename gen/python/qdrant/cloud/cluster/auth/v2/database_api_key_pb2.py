# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: qdrant/cloud/cluster/auth/v2/database_api_key.proto
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
    'qdrant/cloud/cluster/auth/v2/database_api_key.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from qdrant.cloud.common.v1 import common_pb2 as qdrant_dot_cloud_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3qdrant/cloud/cluster/auth/v2/database_api_key.proto\x12\x1cqdrant.cloud.cluster.auth.v2\x1a\x1b\x62uf/validate/validate.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a#qdrant/cloud/common/v1/common.proto\"n\n\x1aListDatabaseApiKeysRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\'\n\ncluster_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\tclusterId\"a\n\x1bListDatabaseApiKeysResponse\x12\x42\n\x05items\x18\x01 \x03(\x0b\x32,.qdrant.cloud.cluster.auth.v2.DatabaseApiKeyR\x05items\"u\n\x1b\x43reateDatabaseApiKeyRequest\x12V\n\x10\x64\x61tabase_api_key\x18\x01 \x01(\x0b\x32,.qdrant.cloud.cluster.auth.v2.DatabaseApiKeyR\x0e\x64\x61tabaseApiKey\"v\n\x1c\x43reateDatabaseApiKeyResponse\x12V\n\x10\x64\x61tabase_api_key\x18\x01 \x01(\x0b\x32,.qdrant.cloud.cluster.auth.v2.DatabaseApiKeyR\x0e\x64\x61tabaseApiKey\"\xa8\x01\n\x1b\x44\x65leteDatabaseApiKeyRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\'\n\ncluster_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\tclusterId\x12\x37\n\x13\x64\x61tabase_api_key_id\x18\x03 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\x10\x64\x61tabaseApiKeyId\"\x1e\n\x1c\x44\x65leteDatabaseApiKeyResponse\"\x8e\x08\n\x0e\x44\x61tabaseApiKey\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\'\n\naccount_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\x39\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\'\n\ncluster_id\x18\x04 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\tclusterId\x12*\n\x04name\x18\x05 \x01(\tB\x16\xbaH\x13r\x11\x10\x04\x18\x80\x01\x32\n^[\\w\\s-]+$R\x04name\x12>\n\nexpires_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\texpiresAt\x88\x01\x01\x12U\n\x0c\x61\x63\x63\x65ss_rules\x18\x07 \x03(\x0b\x32(.qdrant.cloud.cluster.auth.v2.AccessRuleB\x08\xbaH\x05\x92\x01\x02\x10\x14R\x0b\x61\x63\x63\x65ssRules\x12(\n\x10\x63reated_by_email\x18\x08 \x01(\tR\x0e\x63reatedByEmail\x12\x18\n\x07postfix\x18\t \x01(\tR\x07postfix\x12\x10\n\x03key\x18\n \x01(\tR\x03key:\xb6\x04\xbaH\xb2\x04\x1a\xac\x01\n\x13\x64\x61tabase_api_key.id\x12\x1avalue must be a valid UUID\x1aythis.id.matches(\'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$\') || !has(this.created_at)\x1a\xe0\x01\n\x1eno_mixed_global_and_collection\x12OThere can\'t be global and collection access rules in the same database api key.\x1am!(this.access_rules.exists(r, has(r.global_access)) && this.access_rules.exists(r, has(r.collection_access)))\x1a\x9d\x01\n\x16only_one_global_access\x12\x45There can\'t be more than one global access rule in the configuration.\x1a<size(this.access_rules.filter(r, has(r.global_access))) <= 1B\r\n\x0b_expires_at\"\xcf\x01\n\nAccessRule\x12U\n\rglobal_access\x18\x01 \x01(\x0b\x32..qdrant.cloud.cluster.auth.v2.GlobalAccessRuleH\x00R\x0cglobalAccess\x12\x61\n\x11\x63ollection_access\x18\x02 \x01(\x0b\x32\x32.qdrant.cloud.cluster.auth.v2.CollectionAccessRuleH\x00R\x10\x63ollectionAccessB\x07\n\x05scope\"m\n\x10GlobalAccessRule\x12Y\n\x0b\x61\x63\x63\x65ss_type\x18\x01 \x01(\x0e\x32\x38.qdrant.cloud.cluster.auth.v2.GlobalAccessRuleAccessTypeR\naccessType\"\xd2\x02\n\x14\x43ollectionAccessRule\x12\x44\n\x0f\x63ollection_name\x18\x01 \x01(\tB\x1b\xbaH\x18r\x16\x10\x04\x18@2\x10^[a-zA-Z0-9-_]+$R\x0e\x63ollectionName\x12]\n\x0b\x61\x63\x63\x65ss_type\x18\x02 \x01(\x0e\x32<.qdrant.cloud.cluster.auth.v2.CollectionAccessRuleAccessTypeR\naccessType\x12Y\n\x07payload\x18\x03 \x03(\x0b\x32?.qdrant.cloud.cluster.auth.v2.CollectionAccessRule.PayloadEntryR\x07payload\x1a:\n\x0cPayloadEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01*\xa5\x01\n\x1aGlobalAccessRuleAccessType\x12.\n*GLOBAL_ACCESS_RULE_ACCESS_TYPE_UNSPECIFIED\x10\x00\x12,\n(GLOBAL_ACCESS_RULE_ACCESS_TYPE_READ_ONLY\x10\x01\x12)\n%GLOBAL_ACCESS_RULE_ACCESS_TYPE_MANAGE\x10\x02*\xb9\x01\n\x1e\x43ollectionAccessRuleAccessType\x12\x32\n.COLLECTION_ACCESS_RULE_ACCESS_TYPE_UNSPECIFIED\x10\x00\x12\x30\n,COLLECTION_ACCESS_RULE_ACCESS_TYPE_READ_ONLY\x10\x01\x12\x31\n-COLLECTION_ACCESS_RULE_ACCESS_TYPE_READ_WRITE\x10\x02\x32\x96\x06\n\x15\x44\x61tabaseApiKeyService\x12\xe1\x01\n\x13ListDatabaseApiKeys\x12\x38.qdrant.cloud.cluster.auth.v2.ListDatabaseApiKeysRequest\x1a\x39.qdrant.cloud.cluster.auth.v2.ListDatabaseApiKeysResponse\"U\x8a\xb5\x18\rread:api_keys\x82\xd3\xe4\x93\x02>\x12</api/cluster/auth/v2/accounts/{account_id}/database-api-keys\x12\x99\x02\n\x14\x43reateDatabaseApiKey\x12\x39.qdrant.cloud.cluster.auth.v2.CreateDatabaseApiKeyRequest\x1a:.qdrant.cloud.cluster.auth.v2.CreateDatabaseApiKeyResponse\"\x89\x01\x8a\xb5\x18\x0ewrite:api_keys\x92\xb5\x18\x1b\x64\x61tabase_api_key.account_id\x82\xd3\xe4\x93\x02R\"M/api/cluster/auth/v2/accounts/{database_api_key.account_id}/database-api-keys:\x01*\x12\xfc\x01\n\x14\x44\x65leteDatabaseApiKey\x12\x39.qdrant.cloud.cluster.auth.v2.DeleteDatabaseApiKeyRequest\x1a:.qdrant.cloud.cluster.auth.v2.DeleteDatabaseApiKeyResponse\"m\x8a\xb5\x18\x0f\x64\x65lete:api_keys\x82\xd3\xe4\x93\x02T*R/api/cluster/auth/v2/accounts/{account_id}/database-api-keys/{database_api_key_id}B\xa2\x02\n com.qdrant.cloud.cluster.auth.v2B\x13\x44\x61tabaseApiKeyProtoP\x01ZTgithub.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/cluster/auth/v2;authv2\xa2\x02\x04QCCA\xaa\x02\x1cQdrant.Cloud.Cluster.Auth.V2\xca\x02\x1cQdrant\\Cloud\\Cluster\\Auth\\V2\xe2\x02(Qdrant\\Cloud\\Cluster\\Auth\\V2\\GPBMetadata\xea\x02 Qdrant::Cloud::Cluster::Auth::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qdrant.cloud.cluster.auth.v2.database_api_key_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.qdrant.cloud.cluster.auth.v2B\023DatabaseApiKeyProtoP\001ZTgithub.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/cluster/auth/v2;authv2\242\002\004QCCA\252\002\034Qdrant.Cloud.Cluster.Auth.V2\312\002\034Qdrant\\Cloud\\Cluster\\Auth\\V2\342\002(Qdrant\\Cloud\\Cluster\\Auth\\V2\\GPBMetadata\352\002 Qdrant::Cloud::Cluster::Auth::V2'
  _globals['_LISTDATABASEAPIKEYSREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_LISTDATABASEAPIKEYSREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_LISTDATABASEAPIKEYSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTDATABASEAPIKEYSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_DELETEDATABASEAPIKEYREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_DELETEDATABASEAPIKEYREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_DELETEDATABASEAPIKEYREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETEDATABASEAPIKEYREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_DELETEDATABASEAPIKEYREQUEST'].fields_by_name['database_api_key_id']._loaded_options = None
  _globals['_DELETEDATABASEAPIKEYREQUEST'].fields_by_name['database_api_key_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_DATABASEAPIKEY'].fields_by_name['account_id']._loaded_options = None
  _globals['_DATABASEAPIKEY'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_DATABASEAPIKEY'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DATABASEAPIKEY'].fields_by_name['cluster_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_DATABASEAPIKEY'].fields_by_name['name']._loaded_options = None
  _globals['_DATABASEAPIKEY'].fields_by_name['name']._serialized_options = b'\272H\023r\021\020\004\030\200\0012\n^[\\w\\s-]+$'
  _globals['_DATABASEAPIKEY'].fields_by_name['access_rules']._loaded_options = None
  _globals['_DATABASEAPIKEY'].fields_by_name['access_rules']._serialized_options = b'\272H\005\222\001\002\020\024'
  _globals['_DATABASEAPIKEY']._loaded_options = None
  _globals['_DATABASEAPIKEY']._serialized_options = b'\272H\262\004\032\254\001\n\023database_api_key.id\022\032value must be a valid UUID\032ythis.id.matches(\'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$\') || !has(this.created_at)\032\340\001\n\036no_mixed_global_and_collection\022OThere can\'t be global and collection access rules in the same database api key.\032m!(this.access_rules.exists(r, has(r.global_access)) && this.access_rules.exists(r, has(r.collection_access)))\032\235\001\n\026only_one_global_access\022EThere can\'t be more than one global access rule in the configuration.\032<size(this.access_rules.filter(r, has(r.global_access))) <= 1'
  _globals['_COLLECTIONACCESSRULE_PAYLOADENTRY']._loaded_options = None
  _globals['_COLLECTIONACCESSRULE_PAYLOADENTRY']._serialized_options = b'8\001'
  _globals['_COLLECTIONACCESSRULE'].fields_by_name['collection_name']._loaded_options = None
  _globals['_COLLECTIONACCESSRULE'].fields_by_name['collection_name']._serialized_options = b'\272H\030r\026\020\004\030@2\020^[a-zA-Z0-9-_]+$'
  _globals['_DATABASEAPIKEYSERVICE'].methods_by_name['ListDatabaseApiKeys']._loaded_options = None
  _globals['_DATABASEAPIKEYSERVICE'].methods_by_name['ListDatabaseApiKeys']._serialized_options = b'\212\265\030\rread:api_keys\202\323\344\223\002>\022</api/cluster/auth/v2/accounts/{account_id}/database-api-keys'
  _globals['_DATABASEAPIKEYSERVICE'].methods_by_name['CreateDatabaseApiKey']._loaded_options = None
  _globals['_DATABASEAPIKEYSERVICE'].methods_by_name['CreateDatabaseApiKey']._serialized_options = b'\212\265\030\016write:api_keys\222\265\030\033database_api_key.account_id\202\323\344\223\002R\"M/api/cluster/auth/v2/accounts/{database_api_key.account_id}/database-api-keys:\001*'
  _globals['_DATABASEAPIKEYSERVICE'].methods_by_name['DeleteDatabaseApiKey']._loaded_options = None
  _globals['_DATABASEAPIKEYSERVICE'].methods_by_name['DeleteDatabaseApiKey']._serialized_options = b'\212\265\030\017delete:api_keys\202\323\344\223\002T*R/api/cluster/auth/v2/accounts/{account_id}/database-api-keys/{database_api_key_id}'
  _globals['_GLOBALACCESSRULEACCESSTYPE']._serialized_start=2571
  _globals['_GLOBALACCESSRULEACCESSTYPE']._serialized_end=2736
  _globals['_COLLECTIONACCESSRULEACCESSTYPE']._serialized_start=2739
  _globals['_COLLECTIONACCESSRULEACCESSTYPE']._serialized_end=2924
  _globals['_LISTDATABASEAPIKEYSREQUEST']._serialized_start=214
  _globals['_LISTDATABASEAPIKEYSREQUEST']._serialized_end=324
  _globals['_LISTDATABASEAPIKEYSRESPONSE']._serialized_start=326
  _globals['_LISTDATABASEAPIKEYSRESPONSE']._serialized_end=423
  _globals['_CREATEDATABASEAPIKEYREQUEST']._serialized_start=425
  _globals['_CREATEDATABASEAPIKEYREQUEST']._serialized_end=542
  _globals['_CREATEDATABASEAPIKEYRESPONSE']._serialized_start=544
  _globals['_CREATEDATABASEAPIKEYRESPONSE']._serialized_end=662
  _globals['_DELETEDATABASEAPIKEYREQUEST']._serialized_start=665
  _globals['_DELETEDATABASEAPIKEYREQUEST']._serialized_end=833
  _globals['_DELETEDATABASEAPIKEYRESPONSE']._serialized_start=835
  _globals['_DELETEDATABASEAPIKEYRESPONSE']._serialized_end=865
  _globals['_DATABASEAPIKEY']._serialized_start=868
  _globals['_DATABASEAPIKEY']._serialized_end=1906
  _globals['_ACCESSRULE']._serialized_start=1909
  _globals['_ACCESSRULE']._serialized_end=2116
  _globals['_GLOBALACCESSRULE']._serialized_start=2118
  _globals['_GLOBALACCESSRULE']._serialized_end=2227
  _globals['_COLLECTIONACCESSRULE']._serialized_start=2230
  _globals['_COLLECTIONACCESSRULE']._serialized_end=2568
  _globals['_COLLECTIONACCESSRULE_PAYLOADENTRY']._serialized_start=2510
  _globals['_COLLECTIONACCESSRULE_PAYLOADENTRY']._serialized_end=2568
  _globals['_DATABASEAPIKEYSERVICE']._serialized_start=2927
  _globals['_DATABASEAPIKEYSERVICE']._serialized_end=3717
# @@protoc_insertion_point(module_scope)
