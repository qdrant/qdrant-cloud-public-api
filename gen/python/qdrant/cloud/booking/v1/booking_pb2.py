# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: qdrant/cloud/booking/v1/booking.proto
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
    'qdrant/cloud/booking/v1/booking.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from qdrant.cloud.common.v1 import common_pb2 as qdrant_dot_cloud_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%qdrant/cloud/booking/v1/booking.proto\x12\x17qdrant.cloud.booking.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1cgoogle/api/annotations.proto\x1a#qdrant/cloud/common/v1/common.proto\"\x92\x02\n\x13ListPackagesRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\x33\n\x11\x63loud_provider_id\x18\x02 \x01(\tB\x07\xbaH\x04r\x02\x10\x03R\x0f\x63loudProviderId\x12<\n\x18\x63loud_provider_region_id\x18\x03 \x01(\tH\x00R\x15\x63loudProviderRegionId\x88\x01\x01\x12\x42\n\x08statuses\x18\x04 \x03(\x0e\x32&.qdrant.cloud.booking.v1.PackageStatusR\x08statusesB\x1b\n\x19_cloud_provider_region_id\"N\n\x14ListPackagesResponse\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32 .qdrant.cloud.booking.v1.PackageR\x05items\"\xab\x01\n\x19ListGlobalPackagesRequest\x12\x33\n\x11\x63loud_provider_id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x03R\x0f\x63loudProviderId\x12<\n\x18\x63loud_provider_region_id\x18\x02 \x01(\tH\x00R\x15\x63loudProviderRegionId\x88\x01\x01\x42\x1b\n\x19_cloud_provider_region_id\"T\n\x1aListGlobalPackagesResponse\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32 .qdrant.cloud.booking.v1.PackageR\x05items\"V\n\x11GetPackageRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\x18\n\x02id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\x02id\"P\n\x12GetPackageResponse\x12:\n\x07package\x18\x01 \x01(\x0b\x32 .qdrant.cloud.booking.v1.PackageR\x07package\"\xea\x03\n\x07Package\x12\x18\n\x02id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x12\x65\n\x16resource_configuration\x18\x04 \x01(\x0b\x32..qdrant.cloud.booking.v1.ResourceConfigurationR\x15resourceConfiguration\x12\x1a\n\x08\x63urrency\x18\x05 \x01(\tR\x08\x63urrency\x12\x34\n\x17unit_int_price_per_hour\x18\x06 \x01(\x05R\x13unitIntPricePerHour\x12>\n\x06status\x18\x07 \x01(\x0e\x32&.qdrant.cloud.booking.v1.PackageStatusR\x06status\x12\x80\x01\n\x1e\x61vailable_additional_resources\x18\x08 \x01(\x0b\x32\x35.qdrant.cloud.booking.v1.AvailableAdditionalResourcesH\x00R\x1c\x61vailableAdditionalResources\x88\x01\x01\x42!\n\x1f_available_additional_resources\"M\n\x1c\x41vailableAdditionalResources\x12-\n\x13\x64isk_price_per_hour\x18\x01 \x01(\rR\x10\x64iskPricePerHour\"O\n\x15ResourceConfiguration\x12\x10\n\x03ram\x18\x01 \x01(\tR\x03ram\x12\x10\n\x03\x63pu\x18\x02 \x01(\tR\x03\x63pu\x12\x12\n\x04\x64isk\x18\x03 \x01(\tR\x04\x64isk*j\n\rPackageStatus\x12\x1e\n\x1aPACKAGE_STATUS_UNSPECIFIED\x10\x00\x12\x19\n\x15PACKAGE_STATUS_ACTIVE\x10\x01\x12\x1e\n\x1aPACKAGE_STATUS_DEACTIVATED\x10\x02\x32\x89\x04\n\x0e\x42ookingService\x12\xa7\x01\n\x0cListPackages\x12,.qdrant.cloud.booking.v1.ListPackagesRequest\x1a-.qdrant.cloud.booking.v1.ListPackagesResponse\":\x8a\xb5\x18\x00\x82\xd3\xe4\x93\x02\x30\x12./api/booking/v1/accounts/{account_id}/packages\x12\xa6\x01\n\nGetPackage\x12*.qdrant.cloud.booking.v1.GetPackageRequest\x1a+.qdrant.cloud.booking.v1.GetPackageResponse\"?\x8a\xb5\x18\x00\x82\xd3\xe4\x93\x02\x35\x12\x33/api/booking/v1/accounts/{account_id}/packages/{id}\x12\xa3\x01\n\x12ListGlobalPackages\x12\x32.qdrant.cloud.booking.v1.ListGlobalPackagesRequest\x1a\x33.qdrant.cloud.booking.v1.ListGlobalPackagesResponse\"$\x98\xb5\x18\x00\x82\xd3\xe4\x93\x02\x1a\x12\x18/api/booking/v1/packagesB\xfe\x01\n\x1b\x63om.qdrant.cloud.booking.v1B\x0c\x42ookingProtoP\x01ZRgithub.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/booking/v1;bookingv1\xa2\x02\x03QCB\xaa\x02\x17Qdrant.Cloud.Booking.V1\xca\x02\x17Qdrant\\Cloud\\Booking\\V1\xe2\x02#Qdrant\\Cloud\\Booking\\V1\\GPBMetadata\xea\x02\x1aQdrant::Cloud::Booking::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qdrant.cloud.booking.v1.booking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.qdrant.cloud.booking.v1B\014BookingProtoP\001ZRgithub.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/booking/v1;bookingv1\242\002\003QCB\252\002\027Qdrant.Cloud.Booking.V1\312\002\027Qdrant\\Cloud\\Booking\\V1\342\002#Qdrant\\Cloud\\Booking\\V1\\GPBMetadata\352\002\032Qdrant::Cloud::Booking::V1'
  _globals['_LISTPACKAGESREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_LISTPACKAGESREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_LISTPACKAGESREQUEST'].fields_by_name['cloud_provider_id']._loaded_options = None
  _globals['_LISTPACKAGESREQUEST'].fields_by_name['cloud_provider_id']._serialized_options = b'\272H\004r\002\020\003'
  _globals['_LISTGLOBALPACKAGESREQUEST'].fields_by_name['cloud_provider_id']._loaded_options = None
  _globals['_LISTGLOBALPACKAGESREQUEST'].fields_by_name['cloud_provider_id']._serialized_options = b'\272H\004r\002\020\003'
  _globals['_GETPACKAGEREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETPACKAGEREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_GETPACKAGEREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_GETPACKAGEREQUEST'].fields_by_name['id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_PACKAGE'].fields_by_name['id']._loaded_options = None
  _globals['_PACKAGE'].fields_by_name['id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_BOOKINGSERVICE'].methods_by_name['ListPackages']._loaded_options = None
  _globals['_BOOKINGSERVICE'].methods_by_name['ListPackages']._serialized_options = b'\212\265\030\000\202\323\344\223\0020\022./api/booking/v1/accounts/{account_id}/packages'
  _globals['_BOOKINGSERVICE'].methods_by_name['GetPackage']._loaded_options = None
  _globals['_BOOKINGSERVICE'].methods_by_name['GetPackage']._serialized_options = b'\212\265\030\000\202\323\344\223\0025\0223/api/booking/v1/accounts/{account_id}/packages/{id}'
  _globals['_BOOKINGSERVICE'].methods_by_name['ListGlobalPackages']._loaded_options = None
  _globals['_BOOKINGSERVICE'].methods_by_name['ListGlobalPackages']._serialized_options = b'\230\265\030\000\202\323\344\223\002\032\022\030/api/booking/v1/packages'
  _globals['_PACKAGESTATUS']._serialized_start=1602
  _globals['_PACKAGESTATUS']._serialized_end=1708
  _globals['_LISTPACKAGESREQUEST']._serialized_start=163
  _globals['_LISTPACKAGESREQUEST']._serialized_end=437
  _globals['_LISTPACKAGESRESPONSE']._serialized_start=439
  _globals['_LISTPACKAGESRESPONSE']._serialized_end=517
  _globals['_LISTGLOBALPACKAGESREQUEST']._serialized_start=520
  _globals['_LISTGLOBALPACKAGESREQUEST']._serialized_end=691
  _globals['_LISTGLOBALPACKAGESRESPONSE']._serialized_start=693
  _globals['_LISTGLOBALPACKAGESRESPONSE']._serialized_end=777
  _globals['_GETPACKAGEREQUEST']._serialized_start=779
  _globals['_GETPACKAGEREQUEST']._serialized_end=865
  _globals['_GETPACKAGERESPONSE']._serialized_start=867
  _globals['_GETPACKAGERESPONSE']._serialized_end=947
  _globals['_PACKAGE']._serialized_start=950
  _globals['_PACKAGE']._serialized_end=1440
  _globals['_AVAILABLEADDITIONALRESOURCES']._serialized_start=1442
  _globals['_AVAILABLEADDITIONALRESOURCES']._serialized_end=1519
  _globals['_RESOURCECONFIGURATION']._serialized_start=1521
  _globals['_RESOURCECONFIGURATION']._serialized_end=1600
  _globals['_BOOKINGSERVICE']._serialized_start=1711
  _globals['_BOOKINGSERVICE']._serialized_end=2232
# @@protoc_insertion_point(module_scope)
