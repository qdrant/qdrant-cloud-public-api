# Contributing to Qdrant Cloud API

The layout and style of our `.proto` files follow Buf's [style guide](https://docs.buf.build/best-practices/style-guide).

Below there are some additional guidelines to follow for contributing to the Qdrant Cloud API:

## Protobuf guidelines

Review the existing API and services. Do you need a new service, or can you extend an existing one?

When adding a new service:

- Choose a package name that reflects the service/API’s common behavior.
- Use the `qdrant.cloud.` prefix.
- Include an API version.
- Lay out the file of the new service in this order:
  - Package
  - Imports
  - Service
  - Messages
- Organize RPC methods in this order (list, get, create, update, delete, + additional methods). Their respective messages should follow the same structure for clarity.
- Maintain consistency in field names across services.
- Document all types (service, RPC, message, fields) using full sentences. Place comments above the type, not inline.
- Most RPC methods are scoped to accounts. Expect an `account_id` field in the messages and design your API accordingly.
- Indicate the required user permissions for each RPC. Mention them also in the comments of the method. Example:
```proto
service ClusterService {

  // Fetch a cluster in the account identified by the given IDs.
  // Required permissions:
  // - read:clusters
  rpc GetCluster(GetClusterRequest) returns (GetClusterResponse) {
    // permissions
    option (common.v1.permissions) = "read:clusters";
    ...
  }
```
- Use annotations to enforce field formats (e.g. IDs, min/max items, string length). Example:
```proto
message ClusterConfiguration {

  repeated string allowed_ip_source_ranges = 11 [(buf.validate.field).repeated = {
    max_items: 20
    items: {
      string: {max_len: 43}
    }
  }];

}
```
- Use the `google.api.http` annotation to provide the mapping between the RPC method and the REST endpoint. Example:
```proto
service ClusterService {

  rpc CreateCluster(CreateClusterRequest) returns (CreateClusterResponse) {
    ...
    // gRPC Gateway REST call
    option (google.api.http) = {
      post: "/api/cluster/v2/accounts/{cluster.account_id}/clusters"
      body: "*"
    };
  }

}
```
- Use well-known types (e.g., `google.protobuf.Timestamp` instead of string for timestamps).
- Use enum values for static, well-defined sets of options that are unlikely to change.
- Use RPC methods to expose values that may change over time, vary between users or accounts, or include additional metadata (e.g., `qdrant.cloud.platform.v1.PlatformService.ListCloudProviders` for supported cloud providers). Reference them using fields like `cloud_provider_id` instead of hardcoded enums.
- Use strong typing and avoid weak types like maps or key-value lists. Example:

Do:
```proto
// A ClusterConfiguration represents the configuration of a cluster.
message ClusterConfiguration {

  // List of tolerations for this cluster in a hybrid cloud.
  // It is ignored for Managed Cloud clusters. This is an optional field
  repeated Toleration tolerations = 9 [(buf.validate.field).repeated = {max_items: 10}];

}

// The Toleration message represents a toleration object for Kubernetes.
message Toleration {
  // The key to match against the key of a node label.
  string key = 1 [(buf.validate.field).string = {
    // Must be 63 characters or less (excluding the prefix).
    max_len: 63
    // Must be a valid DNS label as per RFC 1123.
    pattern: "^([a-zA-Z0-9]([-a-zA-Z0-9_.]*[a-zA-Z0-9])?)?$"
  }];

  // The operator represents a key's relationship to the value.
  // Valid operators are "Exists" and "Equal".
  // The default is Exists
  optional string operator = 2 [(buf.validate.field).string = {
    in: [
      "Exists",
      "Equal"
    ]
  }];

}

```

Don't:
```proto
// A ClusterConfiguration represents the configuration of a cluster.
message ClusterConfiguration {

  // List of tolerations for this cluster in a hybrid cloud.
  // It is ignored for Managed Cloud clusters. This is an optional field
  repeated map<string, string> tolerations = 9 [(buf.validate.field).repeated = {max_items: 10}];

}
```
