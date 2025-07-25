# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: qdrant/cloud/cluster/v1/cluster.proto
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
    'qdrant/cloud/cluster/v1/cluster.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from qdrant.cloud.common.v1 import common_pb2 as qdrant_dot_cloud_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%qdrant/cloud/cluster/v1/cluster.proto\x12\x17qdrant.cloud.cluster.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a#qdrant/cloud/common/v1/common.proto\"\xfd\x03\n\x13ListClustersRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\x38\n\x11\x63loud_provider_id\x18\n \x01(\tB\x07\xbaH\x04r\x02\x10\x03H\x00R\x0f\x63loudProviderId\x88\x01\x01\x12<\n\x18\x63loud_provider_region_id\x18\x0b \x01(\tH\x01R\x15\x63loudProviderRegionId\x88\x01\x01:\x91\x02\xbaH\x8d\x02\x1a\x8a\x02\n cluster.cloud_provider_region_id\x12Hcloud_provider_region_id must be a UUID if cloud_provider_id is \'hybrid\'\x1a\x9b\x01this.cloud_provider_region_id.matches(\'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$\') || this.cloud_provider_id!= \'hybrid\'B\x14\n\x12_cloud_provider_idB\x1b\n\x19_cloud_provider_region_id\"N\n\x14ListClustersResponse\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32 .qdrant.cloud.cluster.v1.ClusterR\x05items\"e\n\x11GetClusterRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\'\n\ncluster_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\tclusterId\"P\n\x12GetClusterResponse\x12:\n\x07\x63luster\x18\x01 \x01(\x0b\x32 .qdrant.cloud.cluster.v1.ClusterR\x07\x63luster\"R\n\x14\x43reateClusterRequest\x12:\n\x07\x63luster\x18\x01 \x01(\x0b\x32 .qdrant.cloud.cluster.v1.ClusterR\x07\x63luster\"S\n\x15\x43reateClusterResponse\x12:\n\x07\x63luster\x18\x01 \x01(\x0b\x32 .qdrant.cloud.cluster.v1.ClusterR\x07\x63luster\"R\n\x14UpdateClusterRequest\x12:\n\x07\x63luster\x18\x01 \x01(\x0b\x32 .qdrant.cloud.cluster.v1.ClusterR\x07\x63luster\"S\n\x15UpdateClusterResponse\x12:\n\x07\x63luster\x18\x01 \x01(\x0b\x32 .qdrant.cloud.cluster.v1.ClusterR\x07\x63luster\"\xa7\x01\n\x14\x44\x65leteClusterRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\'\n\ncluster_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\tclusterId\x12*\n\x0e\x64\x65lete_backups\x18\x03 \x01(\x08H\x00R\rdeleteBackups\x88\x01\x01\x42\x11\n\x0f_delete_backups\"\x17\n\x15\x44\x65leteClusterResponse\"i\n\x15RestartClusterRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\'\n\ncluster_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\tclusterId\"\x18\n\x16RestartClusterResponse\"i\n\x15SuspendClusterRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\'\n\ncluster_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\tclusterId\"\x18\n\x16SuspendClusterResponse\"D\n\x19SuggestClusterNameRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"0\n\x1aSuggestClusterNameResponse\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"\x81\x01\n\x19ListQdrantReleasesRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12,\n\ncluster_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01H\x00R\tclusterId\x88\x01\x01\x42\r\n\x0b_cluster_id\"Z\n\x1aListQdrantReleasesResponse\x12<\n\x05items\x18\x01 \x03(\x0b\x32&.qdrant.cloud.cluster.v1.QdrantReleaseR\x05items\"\xa3\x07\n\x07\x43luster\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x39\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\'\n\naccount_id\x18\x03 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12/\n\x04name\x18\x04 \x01(\tB\x1b\xbaH\x18r\x16\x10\x04\x18@2\x10^[a-zA-Z0-9-_]+$R\x04name\x12\x39\n\ndeleted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tdeletedAt\x12\x33\n\x11\x63loud_provider_id\x18\n \x01(\tB\x07\xbaH\x04r\x02\x10\x03R\x0f\x63loudProviderId\x12\x37\n\x18\x63loud_provider_region_id\x18\x0b \x01(\tR\x15\x63loudProviderRegionId\x12S\n\rconfiguration\x18\x14 \x01(\x0b\x32-.qdrant.cloud.cluster.v1.ClusterConfigurationR\rconfiguration\x12;\n\x05state\x18\x64 \x01(\x0b\x32%.qdrant.cloud.cluster.v1.ClusterStateR\x05state:\xb7\x03\xbaH\xb3\x03\x1a\xa3\x01\n\ncluster.id\x12\x1avalue must be a valid UUID\x1aythis.id.matches(\'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$\') || !has(this.created_at)\x1a\x8a\x02\n cluster.cloud_provider_region_id\x12Hcloud_provider_region_id must be a UUID if cloud_provider_id is \'hybrid\'\x1a\x9b\x01this.cloud_provider_region_id.matches(\'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$\') || this.cloud_provider_id!= \'hybrid\'\"\xc0\n\n\x14\x43lusterConfiguration\x12\x44\n\x10last_modified_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0elastModifiedAt\x12\x31\n\x0fnumber_of_nodes\x18\x02 \x01(\rB\t\xbaH\x06*\x04\x18\x14(\x01R\rnumberOfNodes\x12\x45\n\x07version\x18\x03 \x01(\tB&\xbaH#r!2\x1f^(v(\\d+)\\.(\\d+)\\.(\\d+)|latest)$H\x00R\x07version\x88\x01\x01\x12\'\n\npackage_id\x18\x04 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\tpackageId\x12\x64\n\x14\x61\x64\x64itional_resources\x18\x05 \x01(\x0b\x32,.qdrant.cloud.cluster.v1.AdditionalResourcesH\x01R\x13\x61\x64\x64itionalResources\x88\x01\x01\x12j\n\x16\x64\x61tabase_configuration\x18\x07 \x01(\x0b\x32..qdrant.cloud.cluster.v1.DatabaseConfigurationH\x02R\x15\x64\x61tabaseConfiguration\x88\x01\x01\x12O\n\rnode_selector\x18\x08 \x03(\x0b\x32 .qdrant.cloud.common.v1.KeyValueB\x08\xbaH\x05\x92\x01\x02\x10\nR\x0cnodeSelector\x12O\n\x0btolerations\x18\t \x03(\x0b\x32#.qdrant.cloud.cluster.v1.TolerationB\x08\xbaH\x05\x92\x01\x02\x10\nR\x0btolerations\x12L\n\x0b\x61nnotations\x18\n \x03(\x0b\x32 .qdrant.cloud.common.v1.KeyValueB\x08\xbaH\x05\x92\x01\x02\x10\nR\x0b\x61nnotations\x12H\n\x18\x61llowed_ip_source_ranges\x18\x0b \x03(\tB\x0f\xbaH\x0c\x92\x01\t\x10\x14\"\x05r\x03\xf0\x01\x01R\x15\x61llowedIpSourceRanges\x12\x41\n\x17reserved_cpu_percentage\x18\x14 \x01(\rB\t\xbaH\x06*\x04\x18P(\x00R\x15reservedCpuPercentage\x12G\n\x1areserved_memory_percentage\x18\x15 \x01(\rB\t\xbaH\x06*\x04\x18P(\x00R\x18reservedMemoryPercentage\x12T\n\x08gpu_type\x18\x16 \x01(\x0e\x32\x34.qdrant.cloud.cluster.v1.ClusterConfigurationGpuTypeH\x03R\x07gpuType\x88\x01\x01\x12\x66\n\x0erestart_policy\x18\x17 \x01(\x0e\x32:.qdrant.cloud.cluster.v1.ClusterConfigurationRestartPolicyH\x04R\rrestartPolicy\x88\x01\x01\x12r\n\x12rebalance_strategy\x18\x18 \x01(\x0e\x32>.qdrant.cloud.cluster.v1.ClusterConfigurationRebalanceStrategyH\x05R\x11rebalanceStrategy\x88\x01\x01\x42\n\n\x08_versionB\x17\n\x15_additional_resourcesB\x19\n\x17_database_configurationB\x0b\n\t_gpu_typeB\x11\n\x0f_restart_policyB\x15\n\x13_rebalance_strategy\"\xed\x04\n\x15\x44\x61tabaseConfiguration\x12]\n\ncollection\x18\x01 \x01(\x0b\x32\x38.qdrant.cloud.cluster.v1.DatabaseConfigurationCollectionH\x00R\ncollection\x88\x01\x01\x12T\n\x07storage\x18\x02 \x01(\x0b\x32\x35.qdrant.cloud.cluster.v1.DatabaseConfigurationStorageH\x01R\x07storage\x88\x01\x01\x12T\n\x07service\x18\x03 \x01(\x0b\x32\x35.qdrant.cloud.cluster.v1.DatabaseConfigurationServiceH\x02R\x07service\x88\x01\x01\x12X\n\tlog_level\x18\x04 \x01(\x0e\x32\x36.qdrant.cloud.cluster.v1.DatabaseConfigurationLogLevelH\x03R\x08logLevel\x88\x01\x01\x12H\n\x03tls\x18\x05 \x01(\x0b\x32\x31.qdrant.cloud.cluster.v1.DatabaseConfigurationTlsH\x04R\x03tls\x88\x01\x01\x12Z\n\tinference\x18\x06 \x01(\x0b\x32\x37.qdrant.cloud.cluster.v1.DatabaseConfigurationInferenceH\x05R\tinference\x88\x01\x01\x42\r\n\x0b_collectionB\n\n\x08_storageB\n\n\x08_serviceB\x0c\n\n_log_levelB\x06\n\x04_tlsB\x0c\n\n_inference\"\x81\x02\n\x1f\x44\x61tabaseConfigurationCollection\x12\x32\n\x12replication_factor\x18\x01 \x01(\rH\x00R\x11replicationFactor\x88\x01\x01\x12\x38\n\x18write_consistency_factor\x18\x02 \x01(\x05R\x16writeConsistencyFactor\x12Y\n\x07vectors\x18\x03 \x01(\x0b\x32?.qdrant.cloud.cluster.v1.DatabaseConfigurationCollectionVectorsR\x07vectorsB\x15\n\x13_replication_factor\"R\n&DatabaseConfigurationCollectionVectors\x12\x1c\n\x07on_disk\x18\x01 \x01(\x08H\x00R\x06onDisk\x88\x01\x01\x42\n\n\x08_on_disk\"\x82\x01\n\x1c\x44\x61tabaseConfigurationStorage\x12\x62\n\x0bperformance\x18\x01 \x01(\x0b\x32@.qdrant.cloud.cluster.v1.DatabaseConfigurationStoragePerformanceR\x0bperformance\"~\n\'DatabaseConfigurationStoragePerformance\x12\x30\n\x14optimizer_cpu_budget\x18\x01 \x01(\x05R\x12optimizerCpuBudget\x12!\n\x0c\x61sync_scorer\x18\x02 \x01(\x08R\x0b\x61syncScorer\"\x94\x02\n\x1c\x44\x61tabaseConfigurationService\x12\x42\n\x07\x61pi_key\x18\x01 \x01(\x0b\x32$.qdrant.cloud.common.v1.SecretKeyRefH\x00R\x06\x61piKey\x88\x01\x01\x12T\n\x11read_only_api_key\x18\x02 \x01(\x0b\x32$.qdrant.cloud.common.v1.SecretKeyRefH\x01R\x0ereadOnlyApiKey\x88\x01\x01\x12\x19\n\x08jwt_rbac\x18\x03 \x01(\x08R\x07jwtRbac\x12\x1d\n\nenable_tls\x18\x04 \x01(\x08R\tenableTlsB\n\n\x08_api_keyB\x14\n\x12_read_only_api_key\"\x8c\x01\n\x18\x44\x61tabaseConfigurationTls\x12\x38\n\x04\x63\x65rt\x18\x01 \x01(\x0b\x32$.qdrant.cloud.common.v1.SecretKeyRefR\x04\x63\x65rt\x12\x36\n\x03key\x18\x02 \x01(\x0b\x32$.qdrant.cloud.common.v1.SecretKeyRefR\x03key\":\n\x1e\x44\x61tabaseConfigurationInference\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\")\n\x13\x41\x64\x64itionalResources\x12\x12\n\x04\x64isk\x18\x03 \x01(\rR\x04\x64isk\"\xee\x02\n\nToleration\x12H\n\x03key\x18\x01 \x01(\tB6\xbaH3r1\x18?2-^([a-zA-Z0-9]([-a-zA-Z0-9_.]*[a-zA-Z0-9])?)?$R\x03key\x12L\n\x08operator\x18\x02 \x01(\x0e\x32+.qdrant.cloud.cluster.v1.TolerationOperatorH\x00R\x08operator\x88\x01\x01\x12\x14\n\x05value\x18\x03 \x01(\tR\x05value\x12\x46\n\x06\x65\x66\x66\x65\x63t\x18\x04 \x01(\x0e\x32).qdrant.cloud.cluster.v1.TolerationEffectH\x01R\x06\x65\x66\x66\x65\x63t\x88\x01\x01\x12;\n\x12toleration_seconds\x18\x05 \x01(\x04\x42\x07\xbaH\x04\x32\x02(\x00H\x02R\x11tolerationSeconds\x88\x01\x01\x42\x0b\n\t_operatorB\t\n\x07_effectB\x15\n\x13_toleration_seconds\"\xcd\x03\n\x0c\x43lusterState\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12\x19\n\x08nodes_up\x18\x02 \x01(\rR\x07nodesUp\x12=\n\x0crestarted_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0brestartedAt\x12;\n\x05phase\x18\x04 \x01(\x0e\x32%.qdrant.cloud.cluster.v1.ClusterPhaseR\x05phase\x12\x16\n\x06reason\x18\x05 \x01(\tR\x06reason\x12\x44\n\x08\x65ndpoint\x18\x06 \x01(\x0b\x32(.qdrant.cloud.cluster.v1.ClusterEndpointR\x08\x65ndpoint\x12R\n\tresources\x18\x07 \x01(\x0b\x32\x34.qdrant.cloud.cluster.v1.ClusterNodeResourcesSummaryR\tresources\x12Z\n\x10scalability_info\x18\x08 \x01(\x0b\x32/.qdrant.cloud.cluster.v1.ClusterScalabilityInfoR\x0fscalabilityInfo\"g\n\x0f\x43lusterEndpoint\x12\x1a\n\x03url\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xa8\x01\x01R\x03url\x12\x1b\n\trest_port\x18\x02 \x01(\x05R\x08restPort\x12\x1b\n\tgrpc_port\x18\x03 \x01(\x05R\x08grpcPort\"\xe2\x01\n\x1b\x43lusterNodeResourcesSummary\x12\x41\n\x04\x64isk\x18\x01 \x01(\x0b\x32-.qdrant.cloud.cluster.v1.ClusterNodeResourcesR\x04\x64isk\x12?\n\x03ram\x18\x02 \x01(\x0b\x32-.qdrant.cloud.cluster.v1.ClusterNodeResourcesR\x03ram\x12?\n\x03\x63pu\x18\x03 \x01(\x0b\x32-.qdrant.cloud.cluster.v1.ClusterNodeResourcesR\x03\x63pu\"\xaa\x01\n\x14\x43lusterNodeResources\x12\x12\n\x04\x62\x61se\x18\x01 \x01(\x01R\x04\x62\x61se\x12$\n\rcomplimentary\x18\x02 \x01(\x01R\rcomplimentary\x12\x1e\n\nadditional\x18\x03 \x01(\x01R\nadditional\x12\x1a\n\x08reserved\x18\x04 \x01(\x01R\x08reserved\x12\x1c\n\tavailable\x18\x05 \x01(\x01R\tavailable\"\x8b\x01\n\x16\x43lusterScalabilityInfo\x12I\n\x06status\x18\x01 \x01(\x0e\x32\x31.qdrant.cloud.cluster.v1.ClusterScalabilityStatusR\x06status\x12\x1b\n\x06reason\x18\x02 \x01(\tH\x00R\x06reason\x88\x01\x01\x42\t\n\x07_reason\"\xf7\x01\n\rQdrantRelease\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12\x18\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\x08R\x07\x64\x65\x66\x61ult\x12/\n\x11release_notes_url\x18\x03 \x01(\tH\x00R\x0freleaseNotesUrl\x88\x01\x01\x12\x1d\n\x07remarks\x18\x04 \x01(\tH\x01R\x07remarks\x88\x01\x01\x12\x1e\n\x0b\x65nd_of_life\x18\x05 \x01(\x08R\tendOfLife\x12 \n\x0bunavailable\x18\x06 \x01(\x08R\x0bunavailableB\x14\n\x12_release_notes_urlB\n\n\x08_remarks*\xa0\x01\n\x1b\x43lusterConfigurationGpuType\x12.\n*CLUSTER_CONFIGURATION_GPU_TYPE_UNSPECIFIED\x10\x00\x12)\n%CLUSTER_CONFIGURATION_GPU_TYPE_NVIDIA\x10\x01\x12&\n\"CLUSTER_CONFIGURATION_GPU_TYPE_AMD\x10\x02*\xf2\x01\n!ClusterConfigurationRestartPolicy\x12\x34\n0CLUSTER_CONFIGURATION_RESTART_POLICY_UNSPECIFIED\x10\x00\x12\x30\n,CLUSTER_CONFIGURATION_RESTART_POLICY_ROLLING\x10\x01\x12\x31\n-CLUSTER_CONFIGURATION_RESTART_POLICY_PARALLEL\x10\x02\x12\x32\n.CLUSTER_CONFIGURATION_RESTART_POLICY_AUTOMATIC\x10\x03*\x8e\x02\n%ClusterConfigurationRebalanceStrategy\x12\x38\n4CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_UNSPECIFIED\x10\x00\x12\x35\n1CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_BY_COUNT\x10\x01\x12\x34\n0CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_BY_SIZE\x10\x02\x12>\n:CLUSTER_CONFIGURATION_REBALANCE_STRATEGY_BY_COUNT_AND_SIZE\x10\x03*\xd5\x02\n\x1d\x44\x61tabaseConfigurationLogLevel\x12\x30\n,DATABASE_CONFIGURATION_LOG_LEVEL_UNSPECIFIED\x10\x00\x12*\n&DATABASE_CONFIGURATION_LOG_LEVEL_TRACE\x10\x01\x12*\n&DATABASE_CONFIGURATION_LOG_LEVEL_DEBUG\x10\x02\x12)\n%DATABASE_CONFIGURATION_LOG_LEVEL_INFO\x10\x03\x12)\n%DATABASE_CONFIGURATION_LOG_LEVEL_WARN\x10\x04\x12*\n&DATABASE_CONFIGURATION_LOG_LEVEL_ERROR\x10\x05\x12(\n$DATABASE_CONFIGURATION_LOG_LEVEL_OFF\x10\x06*x\n\x12TolerationOperator\x12#\n\x1fTOLERATION_OPERATOR_UNSPECIFIED\x10\x00\x12\x1e\n\x1aTOLERATION_OPERATOR_EXISTS\x10\x01\x12\x1d\n\x19TOLERATION_OPERATOR_EQUAL\x10\x02*\xa4\x01\n\x10TolerationEffect\x12!\n\x1dTOLERATION_EFFECT_UNSPECIFIED\x10\x00\x12!\n\x1dTOLERATION_EFFECT_NO_SCHEDULE\x10\x01\x12(\n$TOLERATION_EFFECT_PREFER_NO_SCHEDULE\x10\x02\x12 \n\x1cTOLERATION_EFFECT_NO_EXECUTE\x10\x03*\xc3\x04\n\x0c\x43lusterPhase\x12\x1d\n\x19\x43LUSTER_PHASE_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x43LUSTER_PHASE_CREATING\x10\x01\x12\"\n\x1e\x43LUSTER_PHASE_FAILED_TO_CREATE\x10\x02\x12\x1a\n\x16\x43LUSTER_PHASE_UPDATING\x10\x03\x12\"\n\x1e\x43LUSTER_PHASE_FAILED_TO_UPDATE\x10\x04\x12\x19\n\x15\x43LUSTER_PHASE_SCALING\x10\x05\x12\x1b\n\x17\x43LUSTER_PHASE_UPGRADING\x10\x06\x12\x1c\n\x18\x43LUSTER_PHASE_SUSPENDING\x10\x07\x12\x1b\n\x17\x43LUSTER_PHASE_SUSPENDED\x10\x08\x12#\n\x1f\x43LUSTER_PHASE_FAILED_TO_SUSPEND\x10\t\x12\x1a\n\x16\x43LUSTER_PHASE_RESUMING\x10\n\x12\"\n\x1e\x43LUSTER_PHASE_FAILED_TO_RESUME\x10\x0b\x12\x19\n\x15\x43LUSTER_PHASE_HEALTHY\x10\x0c\x12\x1b\n\x17\x43LUSTER_PHASE_NOT_READY\x10\r\x12\x1f\n\x1b\x43LUSTER_PHASE_RECOVERY_MODE\x10\x0e\x12$\n CLUSTER_PHASE_MANUAL_MAINTENANCE\x10\x0f\x12 \n\x1c\x43LUSTER_PHASE_FAILED_TO_SYNC\x10\x10\x12\x1b\n\x17\x43LUSTER_PHASE_NOT_FOUND\x10\x11*\x9c\x01\n\x18\x43lusterScalabilityStatus\x12*\n&CLUSTER_SCALABILITY_STATUS_UNSPECIFIED\x10\x00\x12+\n\'CLUSTER_SCALABILITY_STATUS_NOT_SCALABLE\x10\x01\x12\'\n#CLUSTER_SCALABILITY_STATUS_SCALABLE\x10\x02\x32\xcb\x0e\n\x0e\x43lusterService\x12\xb4\x01\n\x0cListClusters\x12,.qdrant.cloud.cluster.v1.ListClustersRequest\x1a-.qdrant.cloud.cluster.v1.ListClustersResponse\"G\x8a\xb5\x18\rread:clusters\x82\xd3\xe4\x93\x02\x30\x12./api/cluster/v1/accounts/{account_id}/clusters\x12\xbb\x01\n\nGetCluster\x12*.qdrant.cloud.cluster.v1.GetClusterRequest\x1a+.qdrant.cloud.cluster.v1.GetClusterResponse\"T\x8a\xb5\x18\rread:clusters\x82\xd3\xe4\x93\x02=\x12;/api/cluster/v1/accounts/{account_id}/clusters/{cluster_id}\x12\xd9\x01\n\rCreateCluster\x12-.qdrant.cloud.cluster.v1.CreateClusterRequest\x1a..qdrant.cloud.cluster.v1.CreateClusterResponse\"i\x8a\xb5\x18\x0ewrite:clusters\x92\xb5\x18\x12\x63luster.account_id\x82\xd3\xe4\x93\x02;\"6/api/cluster/v1/accounts/{cluster.account_id}/clusters:\x01*\x12\xe6\x01\n\rUpdateCluster\x12-.qdrant.cloud.cluster.v1.UpdateClusterRequest\x1a..qdrant.cloud.cluster.v1.UpdateClusterResponse\"v\x8a\xb5\x18\x0ewrite:clusters\x92\xb5\x18\x12\x63luster.account_id\x82\xd3\xe4\x93\x02H\x1a\x43/api/cluster/v1/accounts/{cluster.account_id}/clusters/{cluster.id}:\x01*\x12\xc6\x01\n\rDeleteCluster\x12-.qdrant.cloud.cluster.v1.DeleteClusterRequest\x1a..qdrant.cloud.cluster.v1.DeleteClusterResponse\"V\x8a\xb5\x18\x0f\x64\x65lete:clusters\x82\xd3\xe4\x93\x02=*;/api/cluster/v1/accounts/{account_id}/clusters/{cluster_id}\x12\xd0\x01\n\x0eRestartCluster\x12..qdrant.cloud.cluster.v1.RestartClusterRequest\x1a/.qdrant.cloud.cluster.v1.RestartClusterResponse\"]\x8a\xb5\x18\x0ewrite:clusters\x82\xd3\xe4\x93\x02\x45\"C/api/cluster/v1/accounts/{account_id}/clusters/{cluster_id}/restart\x12\xd0\x01\n\x0eSuspendCluster\x12..qdrant.cloud.cluster.v1.SuspendClusterRequest\x1a/.qdrant.cloud.cluster.v1.SuspendClusterResponse\"]\x8a\xb5\x18\x0ewrite:clusters\x82\xd3\xe4\x93\x02\x45\"C/api/cluster/v1/accounts/{account_id}/clusters/{cluster_id}/suspend\x12\xc6\x01\n\x12SuggestClusterName\x12\x32.qdrant.cloud.cluster.v1.SuggestClusterNameRequest\x1a\x33.qdrant.cloud.cluster.v1.SuggestClusterNameResponse\"G\x8a\xb5\x18\x00\x82\xd3\xe4\x93\x02=\x12;/api/cluster/v1/accounts/{account_id}/clusters/suggest-name\x12\xc6\x01\n\x12ListQdrantReleases\x12\x32.qdrant.cloud.cluster.v1.ListQdrantReleasesRequest\x1a\x33.qdrant.cloud.cluster.v1.ListQdrantReleasesResponse\"G\x8a\xb5\x18\rread:clusters\x82\xd3\xe4\x93\x02\x30\x12./api/cluster/v1/accounts/{account_id}/releasesB\xfe\x01\n\x1b\x63om.qdrant.cloud.cluster.v1B\x0c\x43lusterProtoP\x01ZRgithub.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/cluster/v1;clusterv1\xa2\x02\x03QCC\xaa\x02\x17Qdrant.Cloud.Cluster.V1\xca\x02\x17Qdrant\\Cloud\\Cluster\\V1\xe2\x02#Qdrant\\Cloud\\Cluster\\V1\\GPBMetadata\xea\x02\x1aQdrant::Cloud::Cluster::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qdrant.cloud.cluster.v1.cluster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.qdrant.cloud.cluster.v1B\014ClusterProtoP\001ZRgithub.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/cluster/v1;clusterv1\242\002\003QCC\252\002\027Qdrant.Cloud.Cluster.V1\312\002\027Qdrant\\Cloud\\Cluster\\V1\342\002#Qdrant\\Cloud\\Cluster\\V1\\GPBMetadata\352\002\032Qdrant::Cloud::Cluster::V1'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['cloud_provider_id']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['cloud_provider_id']._serialized_options = b'\272H\004r\002\020\003'
  _globals['_LISTCLUSTERSREQUEST']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST']._serialized_options = b'\272H\215\002\032\212\002\n cluster.cloud_provider_region_id\022Hcloud_provider_region_id must be a UUID if cloud_provider_id is \'hybrid\'\032\233\001this.cloud_provider_region_id.matches(\'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$\') || this.cloud_provider_id!= \'hybrid\''
  _globals['_GETCLUSTERREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETCLUSTERREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_GETCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GETCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_RESTARTCLUSTERREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_RESTARTCLUSTERREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_RESTARTCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_RESTARTCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_SUSPENDCLUSTERREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_SUSPENDCLUSTERREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_SUSPENDCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_SUSPENDCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_SUGGESTCLUSTERNAMEREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_SUGGESTCLUSTERNAMEREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_LISTQDRANTRELEASESREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_LISTQDRANTRELEASESREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_LISTQDRANTRELEASESREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTQDRANTRELEASESREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_CLUSTER'].fields_by_name['account_id']._loaded_options = None
  _globals['_CLUSTER'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_CLUSTER'].fields_by_name['name']._loaded_options = None
  _globals['_CLUSTER'].fields_by_name['name']._serialized_options = b'\272H\030r\026\020\004\030@2\020^[a-zA-Z0-9-_]+$'
  _globals['_CLUSTER'].fields_by_name['cloud_provider_id']._loaded_options = None
  _globals['_CLUSTER'].fields_by_name['cloud_provider_id']._serialized_options = b'\272H\004r\002\020\003'
  _globals['_CLUSTER']._loaded_options = None
  _globals['_CLUSTER']._serialized_options = b'\272H\263\003\032\243\001\n\ncluster.id\022\032value must be a valid UUID\032ythis.id.matches(\'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$\') || !has(this.created_at)\032\212\002\n cluster.cloud_provider_region_id\022Hcloud_provider_region_id must be a UUID if cloud_provider_id is \'hybrid\'\032\233\001this.cloud_provider_region_id.matches(\'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$\') || this.cloud_provider_id!= \'hybrid\''
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['number_of_nodes']._loaded_options = None
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['number_of_nodes']._serialized_options = b'\272H\006*\004\030\024(\001'
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['version']._loaded_options = None
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['version']._serialized_options = b'\272H#r!2\037^(v(\\d+)\\.(\\d+)\\.(\\d+)|latest)$'
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['package_id']._loaded_options = None
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['package_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['node_selector']._loaded_options = None
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['node_selector']._serialized_options = b'\272H\005\222\001\002\020\n'
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['tolerations']._loaded_options = None
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['tolerations']._serialized_options = b'\272H\005\222\001\002\020\n'
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['annotations']._loaded_options = None
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['annotations']._serialized_options = b'\272H\005\222\001\002\020\n'
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['allowed_ip_source_ranges']._loaded_options = None
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['allowed_ip_source_ranges']._serialized_options = b'\272H\014\222\001\t\020\024\"\005r\003\360\001\001'
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['reserved_cpu_percentage']._loaded_options = None
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['reserved_cpu_percentage']._serialized_options = b'\272H\006*\004\030P(\000'
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['reserved_memory_percentage']._loaded_options = None
  _globals['_CLUSTERCONFIGURATION'].fields_by_name['reserved_memory_percentage']._serialized_options = b'\272H\006*\004\030P(\000'
  _globals['_TOLERATION'].fields_by_name['key']._loaded_options = None
  _globals['_TOLERATION'].fields_by_name['key']._serialized_options = b'\272H3r1\030?2-^([a-zA-Z0-9]([-a-zA-Z0-9_.]*[a-zA-Z0-9])?)?$'
  _globals['_TOLERATION'].fields_by_name['toleration_seconds']._loaded_options = None
  _globals['_TOLERATION'].fields_by_name['toleration_seconds']._serialized_options = b'\272H\0042\002(\000'
  _globals['_CLUSTERENDPOINT'].fields_by_name['url']._loaded_options = None
  _globals['_CLUSTERENDPOINT'].fields_by_name['url']._serialized_options = b'\272H\005r\003\250\001\001'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListClusters']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListClusters']._serialized_options = b'\212\265\030\rread:clusters\202\323\344\223\0020\022./api/cluster/v1/accounts/{account_id}/clusters'
  _globals['_CLUSTERSERVICE'].methods_by_name['GetCluster']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['GetCluster']._serialized_options = b'\212\265\030\rread:clusters\202\323\344\223\002=\022;/api/cluster/v1/accounts/{account_id}/clusters/{cluster_id}'
  _globals['_CLUSTERSERVICE'].methods_by_name['CreateCluster']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['CreateCluster']._serialized_options = b'\212\265\030\016write:clusters\222\265\030\022cluster.account_id\202\323\344\223\002;\"6/api/cluster/v1/accounts/{cluster.account_id}/clusters:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['UpdateCluster']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['UpdateCluster']._serialized_options = b'\212\265\030\016write:clusters\222\265\030\022cluster.account_id\202\323\344\223\002H\032C/api/cluster/v1/accounts/{cluster.account_id}/clusters/{cluster.id}:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['DeleteCluster']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['DeleteCluster']._serialized_options = b'\212\265\030\017delete:clusters\202\323\344\223\002=*;/api/cluster/v1/accounts/{account_id}/clusters/{cluster_id}'
  _globals['_CLUSTERSERVICE'].methods_by_name['RestartCluster']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['RestartCluster']._serialized_options = b'\212\265\030\016write:clusters\202\323\344\223\002E\"C/api/cluster/v1/accounts/{account_id}/clusters/{cluster_id}/restart'
  _globals['_CLUSTERSERVICE'].methods_by_name['SuspendCluster']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['SuspendCluster']._serialized_options = b'\212\265\030\016write:clusters\202\323\344\223\002E\"C/api/cluster/v1/accounts/{account_id}/clusters/{cluster_id}/suspend'
  _globals['_CLUSTERSERVICE'].methods_by_name['SuggestClusterName']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['SuggestClusterName']._serialized_options = b'\212\265\030\000\202\323\344\223\002=\022;/api/cluster/v1/accounts/{account_id}/clusters/suggest-name'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListQdrantReleases']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListQdrantReleases']._serialized_options = b'\212\265\030\rread:clusters\202\323\344\223\0020\022./api/cluster/v1/accounts/{account_id}/releases'
  _globals['_CLUSTERCONFIGURATIONGPUTYPE']._serialized_start=7883
  _globals['_CLUSTERCONFIGURATIONGPUTYPE']._serialized_end=8043
  _globals['_CLUSTERCONFIGURATIONRESTARTPOLICY']._serialized_start=8046
  _globals['_CLUSTERCONFIGURATIONRESTARTPOLICY']._serialized_end=8288
  _globals['_CLUSTERCONFIGURATIONREBALANCESTRATEGY']._serialized_start=8291
  _globals['_CLUSTERCONFIGURATIONREBALANCESTRATEGY']._serialized_end=8561
  _globals['_DATABASECONFIGURATIONLOGLEVEL']._serialized_start=8564
  _globals['_DATABASECONFIGURATIONLOGLEVEL']._serialized_end=8905
  _globals['_TOLERATIONOPERATOR']._serialized_start=8907
  _globals['_TOLERATIONOPERATOR']._serialized_end=9027
  _globals['_TOLERATIONEFFECT']._serialized_start=9030
  _globals['_TOLERATIONEFFECT']._serialized_end=9194
  _globals['_CLUSTERPHASE']._serialized_start=9197
  _globals['_CLUSTERPHASE']._serialized_end=9776
  _globals['_CLUSTERSCALABILITYSTATUS']._serialized_start=9779
  _globals['_CLUSTERSCALABILITYSTATUS']._serialized_end=9935
  _globals['_LISTCLUSTERSREQUEST']._serialized_start=196
  _globals['_LISTCLUSTERSREQUEST']._serialized_end=705
  _globals['_LISTCLUSTERSRESPONSE']._serialized_start=707
  _globals['_LISTCLUSTERSRESPONSE']._serialized_end=785
  _globals['_GETCLUSTERREQUEST']._serialized_start=787
  _globals['_GETCLUSTERREQUEST']._serialized_end=888
  _globals['_GETCLUSTERRESPONSE']._serialized_start=890
  _globals['_GETCLUSTERRESPONSE']._serialized_end=970
  _globals['_CREATECLUSTERREQUEST']._serialized_start=972
  _globals['_CREATECLUSTERREQUEST']._serialized_end=1054
  _globals['_CREATECLUSTERRESPONSE']._serialized_start=1056
  _globals['_CREATECLUSTERRESPONSE']._serialized_end=1139
  _globals['_UPDATECLUSTERREQUEST']._serialized_start=1141
  _globals['_UPDATECLUSTERREQUEST']._serialized_end=1223
  _globals['_UPDATECLUSTERRESPONSE']._serialized_start=1225
  _globals['_UPDATECLUSTERRESPONSE']._serialized_end=1308
  _globals['_DELETECLUSTERREQUEST']._serialized_start=1311
  _globals['_DELETECLUSTERREQUEST']._serialized_end=1478
  _globals['_DELETECLUSTERRESPONSE']._serialized_start=1480
  _globals['_DELETECLUSTERRESPONSE']._serialized_end=1503
  _globals['_RESTARTCLUSTERREQUEST']._serialized_start=1505
  _globals['_RESTARTCLUSTERREQUEST']._serialized_end=1610
  _globals['_RESTARTCLUSTERRESPONSE']._serialized_start=1612
  _globals['_RESTARTCLUSTERRESPONSE']._serialized_end=1636
  _globals['_SUSPENDCLUSTERREQUEST']._serialized_start=1638
  _globals['_SUSPENDCLUSTERREQUEST']._serialized_end=1743
  _globals['_SUSPENDCLUSTERRESPONSE']._serialized_start=1745
  _globals['_SUSPENDCLUSTERRESPONSE']._serialized_end=1769
  _globals['_SUGGESTCLUSTERNAMEREQUEST']._serialized_start=1771
  _globals['_SUGGESTCLUSTERNAMEREQUEST']._serialized_end=1839
  _globals['_SUGGESTCLUSTERNAMERESPONSE']._serialized_start=1841
  _globals['_SUGGESTCLUSTERNAMERESPONSE']._serialized_end=1889
  _globals['_LISTQDRANTRELEASESREQUEST']._serialized_start=1892
  _globals['_LISTQDRANTRELEASESREQUEST']._serialized_end=2021
  _globals['_LISTQDRANTRELEASESRESPONSE']._serialized_start=2023
  _globals['_LISTQDRANTRELEASESRESPONSE']._serialized_end=2113
  _globals['_CLUSTER']._serialized_start=2116
  _globals['_CLUSTER']._serialized_end=3047
  _globals['_CLUSTERCONFIGURATION']._serialized_start=3050
  _globals['_CLUSTERCONFIGURATION']._serialized_end=4394
  _globals['_DATABASECONFIGURATION']._serialized_start=4397
  _globals['_DATABASECONFIGURATION']._serialized_end=5018
  _globals['_DATABASECONFIGURATIONCOLLECTION']._serialized_start=5021
  _globals['_DATABASECONFIGURATIONCOLLECTION']._serialized_end=5278
  _globals['_DATABASECONFIGURATIONCOLLECTIONVECTORS']._serialized_start=5280
  _globals['_DATABASECONFIGURATIONCOLLECTIONVECTORS']._serialized_end=5362
  _globals['_DATABASECONFIGURATIONSTORAGE']._serialized_start=5365
  _globals['_DATABASECONFIGURATIONSTORAGE']._serialized_end=5495
  _globals['_DATABASECONFIGURATIONSTORAGEPERFORMANCE']._serialized_start=5497
  _globals['_DATABASECONFIGURATIONSTORAGEPERFORMANCE']._serialized_end=5623
  _globals['_DATABASECONFIGURATIONSERVICE']._serialized_start=5626
  _globals['_DATABASECONFIGURATIONSERVICE']._serialized_end=5902
  _globals['_DATABASECONFIGURATIONTLS']._serialized_start=5905
  _globals['_DATABASECONFIGURATIONTLS']._serialized_end=6045
  _globals['_DATABASECONFIGURATIONINFERENCE']._serialized_start=6047
  _globals['_DATABASECONFIGURATIONINFERENCE']._serialized_end=6105
  _globals['_ADDITIONALRESOURCES']._serialized_start=6107
  _globals['_ADDITIONALRESOURCES']._serialized_end=6148
  _globals['_TOLERATION']._serialized_start=6151
  _globals['_TOLERATION']._serialized_end=6517
  _globals['_CLUSTERSTATE']._serialized_start=6520
  _globals['_CLUSTERSTATE']._serialized_end=6981
  _globals['_CLUSTERENDPOINT']._serialized_start=6983
  _globals['_CLUSTERENDPOINT']._serialized_end=7086
  _globals['_CLUSTERNODERESOURCESSUMMARY']._serialized_start=7089
  _globals['_CLUSTERNODERESOURCESSUMMARY']._serialized_end=7315
  _globals['_CLUSTERNODERESOURCES']._serialized_start=7318
  _globals['_CLUSTERNODERESOURCES']._serialized_end=7488
  _globals['_CLUSTERSCALABILITYINFO']._serialized_start=7491
  _globals['_CLUSTERSCALABILITYINFO']._serialized_end=7630
  _globals['_QDRANTRELEASE']._serialized_start=7633
  _globals['_QDRANTRELEASE']._serialized_end=7880
  _globals['_CLUSTERSERVICE']._serialized_start=9938
  _globals['_CLUSTERSERVICE']._serialized_end=11805
# @@protoc_insertion_point(module_scope)
