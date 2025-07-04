// @generated by protoc-gen-es v2.5.2 with parameter "target=js+dts,import_extension=js"
// @generated from file qdrant/cloud/monitoring/v1/monitoring.proto (package qdrant.cloud.monitoring.v1, syntax proto3)
/* eslint-disable */

import { enumDesc, fileDesc, messageDesc, serviceDesc, tsEnum } from "@bufbuild/protobuf/codegenv2";
import { file_buf_validate_validate } from "../../../../buf/validate/validate_pb.js";
import { file_google_api_annotations } from "../../../../google/api/annotations_pb.js";
import { file_google_protobuf_duration, file_google_protobuf_timestamp } from "@bufbuild/protobuf/wkt";
import { file_qdrant_cloud_common_v1_common } from "../../common/v1/common_pb.js";

/**
 * Describes the file qdrant/cloud/monitoring/v1/monitoring.proto.
 */
export const file_qdrant_cloud_monitoring_v1_monitoring = /*@__PURE__*/
  fileDesc("CitxZHJhbnQvY2xvdWQvbW9uaXRvcmluZy92MS9tb25pdG9yaW5nLnByb3RvEhpxZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MSJdCh9HZXRDbHVzdGVyU3VtbWFyeU1ldHJpY3NSZXF1ZXN0EhwKCmFjY291bnRfaWQYASABKAlCCLpIBXIDsAEBEhwKCmNsdXN0ZXJfaWQYAiABKAlCCLpIBXIDsAEBImEKIEdldENsdXN0ZXJTdW1tYXJ5TWV0cmljc1Jlc3BvbnNlEj0KBW5vZGVzGAEgAygLMi4ucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuQ2x1c3Rlck5vZGVNZXRyaWNzIp8CCh1HZXRDbHVzdGVyVXNhZ2VNZXRyaWNzUmVxdWVzdBIcCgphY2NvdW50X2lkGAEgASgJQgi6SAVyA7ABARIcCgpjbHVzdGVyX2lkGAIgASgJQgi6SAVyA7ABARIuCgVzaW5jZRgDIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXBIAIgBARIuCgV1bnRpbBgEIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXBIAYgBARI/CgphZ2dyZWdhdG9yGAUgASgOMiYucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuQWdncmVnYXRvckgCiAEBQggKBl9zaW5jZUIICgZfdW50aWxCDQoLX2FnZ3JlZ2F0b3IihgQKHkdldENsdXN0ZXJVc2FnZU1ldHJpY3NSZXNwb25zZRIvCgNjcHUYASADKAsyIi5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5NZXRyaWMSLwoDcmFtGAIgAygLMiIucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuTWV0cmljEjUKCXJhbV9jYWNoZRgDIAMoCzIiLnFkcmFudC5jbG91ZC5tb25pdG9yaW5nLnYxLk1ldHJpYxIzCgdyYW1fcnNzGAQgAygLMiIucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuTWV0cmljEjoKDnJhbV9xZHJhbnRfcnNzGAUgAygLMiIucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuTWV0cmljEjAKBGRpc2sYBiADKAsyIi5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5NZXRyaWMSLwoDcnBzGAcgAygLMiIucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuTWV0cmljEjMKB2xhdGVuY3kYCCADKAsyIi5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5NZXRyaWMSQgoFbm9kZXMYCSADKAsyMy5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5DbHVzdGVyTm9kZVVzYWdlTWV0cmljcyLHAQoVR2V0Q2x1c3RlckxvZ3NSZXF1ZXN0EhwKCmFjY291bnRfaWQYASABKAlCCLpIBXIDsAEBEhwKCmNsdXN0ZXJfaWQYAiABKAlCCLpIBXIDsAEBEi4KBXNpbmNlGAMgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcEgAiAEBEi4KBXVudGlsGAQgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcEgBiAEBQggKBl9zaW5jZUIICgZfdW50aWwiTQoWR2V0Q2x1c3RlckxvZ3NSZXNwb25zZRIzCgVpdGVtcxgBIAMoCzIkLnFkcmFudC5jbG91ZC5tb25pdG9yaW5nLnYxLkxvZ0VudHJ5IskBChdHZXRDbHVzdGVyRXZlbnRzUmVxdWVzdBIcCgphY2NvdW50X2lkGAEgASgJQgi6SAVyA7ABARIcCgpjbHVzdGVyX2lkGAIgASgJQgi6SAVyA7ABARIuCgVzaW5jZRgDIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXBIAIgBARIuCgV1bnRpbBgEIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXBIAYgBAUIICgZfc2luY2VCCAoGX3VudGlsIk8KGEdldENsdXN0ZXJFdmVudHNSZXNwb25zZRIzCgVpdGVtcxgBIAMoCzIkLnFkcmFudC5jbG91ZC5tb25pdG9yaW5nLnYxLkxvZ0VudHJ5IrsDChJDbHVzdGVyTm9kZU1ldHJpY3MSDwoHbm9kZV9pZBgBIAEoCRI+CgNjcHUYAiABKAsyMS5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5DbHVzdGVyTWV0cmljT3ZlcnZpZXcSPgoDcmFtGAMgASgLMjEucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuQ2x1c3Rlck1ldHJpY092ZXJ2aWV3EkQKCXJhbV9jYWNoZRgEIAEoCzIxLnFkcmFudC5jbG91ZC5tb25pdG9yaW5nLnYxLkNsdXN0ZXJNZXRyaWNPdmVydmlldxJCCgdyYW1fcnNzGAUgASgLMjEucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuQ2x1c3Rlck1ldHJpY092ZXJ2aWV3EkkKDnJhbV9xZHJhbnRfcnNzGAYgASgLMjEucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuQ2x1c3Rlck1ldHJpY092ZXJ2aWV3Ej8KBGRpc2sYByABKAsyMS5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5DbHVzdGVyTWV0cmljT3ZlcnZpZXciiwEKFUNsdXN0ZXJNZXRyaWNPdmVydmlldxI4CgNhdmcYASADKAsyKy5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5JbnRlcnZhbEF2ZXJhZ2USOAoFdG90YWwYAiABKAsyKS5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5SZXNvdXJjZVZhbHVlIk0KD0ludGVydmFsQXZlcmFnZRIrCghpbnRlcnZhbBgBIAEoCzIZLmdvb2dsZS5wcm90b2J1Zi5EdXJhdGlvbhINCgV2YWx1ZRgCIAEoASIsCg1SZXNvdXJjZVZhbHVlEg0KBXZhbHVlGAEgASgBEgwKBHVuaXQYAiABKAki5gIKF0NsdXN0ZXJOb2RlVXNhZ2VNZXRyaWNzEg8KB25vZGVfaWQYASABKAkSLwoDY3B1GAIgAygLMiIucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuTWV0cmljEi8KA3JhbRgDIAMoCzIiLnFkcmFudC5jbG91ZC5tb25pdG9yaW5nLnYxLk1ldHJpYxI1CglyYW1fY2FjaGUYBCADKAsyIi5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5NZXRyaWMSMwoHcmFtX3JzcxgFIAMoCzIiLnFkcmFudC5jbG91ZC5tb25pdG9yaW5nLnYxLk1ldHJpYxI6Cg5yYW1fcWRyYW50X3JzcxgGIAMoCzIiLnFkcmFudC5jbG91ZC5tb25pdG9yaW5nLnYxLk1ldHJpYxIwCgRkaXNrGAcgAygLMiIucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuTWV0cmljIkYKBk1ldHJpYxItCgl0aW1lc3RhbXAYASABKAsyGi5nb29nbGUucHJvdG9idWYuVGltZXN0YW1wEg0KBXZhbHVlGAIgASgBIkoKCExvZ0VudHJ5Ei0KCXRpbWVzdGFtcBgBIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXASDwoHbWVzc2FnZRgCIAEoCSp4CgpBZ2dyZWdhdG9yEhoKFkFHR1JFR0FUT1JfVU5TUEVDSUZJRUQQABISCg5BR0dSRUdBVE9SX1NVTRABEhIKDkFHR1JFR0FUT1JfQVZHEAISEgoOQUdHUkVHQVRPUl9NQVgQAxISCg5BR0dSRUdBVE9SX01JThAEMsEHChFNb25pdG9yaW5nU2VydmljZRL9AQoYR2V0Q2x1c3RlclN1bW1hcnlNZXRyaWNzEjsucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuR2V0Q2x1c3RlclN1bW1hcnlNZXRyaWNzUmVxdWVzdBo8LnFkcmFudC5jbG91ZC5tb25pdG9yaW5nLnYxLkdldENsdXN0ZXJTdW1tYXJ5TWV0cmljc1Jlc3BvbnNlImaKtRgNcmVhZDpjbHVzdGVyc4LT5JMCTxJNL2FwaS9tb25pdG9yaW5nL3YxL2FjY291bnRzL3thY2NvdW50X2lkfS9jbHVzdGVyL3tjbHVzdGVyX2lkfS9zdW1tYXJ5LW1ldHJpY3MS9QEKFkdldENsdXN0ZXJVc2FnZU1ldHJpY3MSOS5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5HZXRDbHVzdGVyVXNhZ2VNZXRyaWNzUmVxdWVzdBo6LnFkcmFudC5jbG91ZC5tb25pdG9yaW5nLnYxLkdldENsdXN0ZXJVc2FnZU1ldHJpY3NSZXNwb25zZSJkirUYDXJlYWQ6Y2x1c3RlcnOC0+STAk0SSy9hcGkvbW9uaXRvcmluZy92MS9hY2NvdW50cy97YWNjb3VudF9pZH0vY2x1c3Rlci97Y2x1c3Rlcl9pZH0vdXNhZ2UtbWV0cmljcxLUAQoOR2V0Q2x1c3RlckxvZ3MSMS5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5HZXRDbHVzdGVyTG9nc1JlcXVlc3QaMi5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5HZXRDbHVzdGVyTG9nc1Jlc3BvbnNlIluKtRgNcmVhZDpjbHVzdGVyc4LT5JMCRBJCL2FwaS9tb25pdG9yaW5nL3YxL2FjY291bnRzL3thY2NvdW50X2lkfS9jbHVzdGVyL3tjbHVzdGVyX2lkfS9sb2dzEtwBChBHZXRDbHVzdGVyRXZlbnRzEjMucWRyYW50LmNsb3VkLm1vbml0b3JpbmcudjEuR2V0Q2x1c3RlckV2ZW50c1JlcXVlc3QaNC5xZHJhbnQuY2xvdWQubW9uaXRvcmluZy52MS5HZXRDbHVzdGVyRXZlbnRzUmVzcG9uc2UiXYq1GA1yZWFkOmNsdXN0ZXJzgtPkkwJGEkQvYXBpL21vbml0b3JpbmcvdjEvYWNjb3VudHMve2FjY291bnRfaWR9L2NsdXN0ZXIve2NsdXN0ZXJfaWR9L2V2ZW50c0KWAgoeY29tLnFkcmFudC5jbG91ZC5tb25pdG9yaW5nLnYxQg9Nb25pdG9yaW5nUHJvdG9QAVpYZ2l0aHViLmNvbS9xZHJhbnQvcWRyYW50LWNsb3VkLXB1YmxpYy1hcGkvZ2VuL2dvL3FkcmFudC9jbG91ZC9tb25pdG9yaW5nL3YxO21vbml0b3Jpbmd2MaICA1FDTaoCGlFkcmFudC5DbG91ZC5Nb25pdG9yaW5nLlYxygIaUWRyYW50XENsb3VkXE1vbml0b3JpbmdcVjHiAiZRZHJhbnRcQ2xvdWRcTW9uaXRvcmluZ1xWMVxHUEJNZXRhZGF0YeoCHVFkcmFudDo6Q2xvdWQ6Ok1vbml0b3Jpbmc6OlYxYgZwcm90bzM", [file_buf_validate_validate, file_google_api_annotations, file_google_protobuf_duration, file_google_protobuf_timestamp, file_qdrant_cloud_common_v1_common]);

/**
 * Describes the message qdrant.cloud.monitoring.v1.GetClusterSummaryMetricsRequest.
 * Use `create(GetClusterSummaryMetricsRequestSchema)` to create a new message.
 */
export const GetClusterSummaryMetricsRequestSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 0);

/**
 * Describes the message qdrant.cloud.monitoring.v1.GetClusterSummaryMetricsResponse.
 * Use `create(GetClusterSummaryMetricsResponseSchema)` to create a new message.
 */
export const GetClusterSummaryMetricsResponseSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 1);

/**
 * Describes the message qdrant.cloud.monitoring.v1.GetClusterUsageMetricsRequest.
 * Use `create(GetClusterUsageMetricsRequestSchema)` to create a new message.
 */
export const GetClusterUsageMetricsRequestSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 2);

/**
 * Describes the message qdrant.cloud.monitoring.v1.GetClusterUsageMetricsResponse.
 * Use `create(GetClusterUsageMetricsResponseSchema)` to create a new message.
 */
export const GetClusterUsageMetricsResponseSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 3);

/**
 * Describes the message qdrant.cloud.monitoring.v1.GetClusterLogsRequest.
 * Use `create(GetClusterLogsRequestSchema)` to create a new message.
 */
export const GetClusterLogsRequestSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 4);

/**
 * Describes the message qdrant.cloud.monitoring.v1.GetClusterLogsResponse.
 * Use `create(GetClusterLogsResponseSchema)` to create a new message.
 */
export const GetClusterLogsResponseSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 5);

/**
 * Describes the message qdrant.cloud.monitoring.v1.GetClusterEventsRequest.
 * Use `create(GetClusterEventsRequestSchema)` to create a new message.
 */
export const GetClusterEventsRequestSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 6);

/**
 * Describes the message qdrant.cloud.monitoring.v1.GetClusterEventsResponse.
 * Use `create(GetClusterEventsResponseSchema)` to create a new message.
 */
export const GetClusterEventsResponseSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 7);

/**
 * Describes the message qdrant.cloud.monitoring.v1.ClusterNodeMetrics.
 * Use `create(ClusterNodeMetricsSchema)` to create a new message.
 */
export const ClusterNodeMetricsSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 8);

/**
 * Describes the message qdrant.cloud.monitoring.v1.ClusterMetricOverview.
 * Use `create(ClusterMetricOverviewSchema)` to create a new message.
 */
export const ClusterMetricOverviewSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 9);

/**
 * Describes the message qdrant.cloud.monitoring.v1.IntervalAverage.
 * Use `create(IntervalAverageSchema)` to create a new message.
 */
export const IntervalAverageSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 10);

/**
 * Describes the message qdrant.cloud.monitoring.v1.ResourceValue.
 * Use `create(ResourceValueSchema)` to create a new message.
 */
export const ResourceValueSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 11);

/**
 * Describes the message qdrant.cloud.monitoring.v1.ClusterNodeUsageMetrics.
 * Use `create(ClusterNodeUsageMetricsSchema)` to create a new message.
 */
export const ClusterNodeUsageMetricsSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 12);

/**
 * Describes the message qdrant.cloud.monitoring.v1.Metric.
 * Use `create(MetricSchema)` to create a new message.
 */
export const MetricSchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 13);

/**
 * Describes the message qdrant.cloud.monitoring.v1.LogEntry.
 * Use `create(LogEntrySchema)` to create a new message.
 */
export const LogEntrySchema = /*@__PURE__*/
  messageDesc(file_qdrant_cloud_monitoring_v1_monitoring, 14);

/**
 * Describes the enum qdrant.cloud.monitoring.v1.Aggregator.
 */
export const AggregatorSchema = /*@__PURE__*/
  enumDesc(file_qdrant_cloud_monitoring_v1_monitoring, 0);

/**
 * Aggregator defines how metrics should be aggregated over time.
 *
 * @generated from enum qdrant.cloud.monitoring.v1.Aggregator
 */
export const Aggregator = /*@__PURE__*/
  tsEnum(AggregatorSchema);

/**
 * MonitoringService provides access to monitoring data such as cluster metrics, logs, and events.
 *
 * @generated from service qdrant.cloud.monitoring.v1.MonitoringService
 */
export const MonitoringService = /*@__PURE__*/
  serviceDesc(file_qdrant_cloud_monitoring_v1_monitoring, 0);

