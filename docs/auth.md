# Authentication & Authorization

The Qdrant Cloud API uses both authentication and authorization to control access to resources and operations.

## Authentication

Authentication verifies the identity of the caller. The API supports multiple authentication methods through different actor types.

### Actor Types

The API defines several actor types that represent different ways of authenticating:

- **`ACTOR_TYPE_USER`**: Users authenticated via identity providers (Auth0)
- **`ACTOR_TYPE_MANAGEMENT_KEY`**: Programmatic access keys (API keys) tied to an account, not a specific user
- **`ACTOR_TYPE_SERVICE_ACCOUNT`**: Service accounts for machine-to-machine communication (internal platform use)

### Authentication Requirements

Methods can specify authentication requirements using the `requires_authentication` option:

```protobuf
rpc PublicMethod(PublicRequest) returns (PublicResponse) {
  option (common.v1.requires_authentication) = false; // No authentication required
}
```

- **Default behavior**: Authentication is required (`requires_authentication = true`)
- **Public endpoints**: Set `requires_authentication = false` for endpoints that don't require authentication

### Restricting Actor Types

Methods can restrict which actor types are allowed using the `supported_actor_types` option:

```protobuf
rpc UserOnlyMethod(UserRequest) returns (UserResponse) {
  option (common.v1.supported_actor_types) = ACTOR_TYPE_USER; // Only users allowed
}
```

When `supported_actor_types` is not specified, all authenticated actor types are allowed (subject to authorization checks).

## Authorization

The API uses a permission-based authorization system for RPC methods. Each method defines the required permissions that must be satisfied for access to be granted.

Permissions are granted in the scope of an account, based on the roles that a user has assigned for that account.

## Permissions Option

Methods specify their authorization requirements using the `permissions` option in their Protocol Buffer definitions:

```protobuf
rpc CreateCluster(CreateClusterRequest) returns (CreateClusterResponse) {
  option (common.v1.permissions) = "write:clusters";
}
```

## Multiple Permissions

A method can require multiple permissions by specifying multiple `permissions` options. By default, when multiple permissions are specified, **all** permissions must be satisfied (AND behavior):

```protobuf
rpc ListHybridCloudEnvironments(ListHybridCloudEnvironmentsRequest) returns (ListHybridCloudEnvironmentsResponse) {
  option (common.v1.permissions) = "read:hybrid_cloud_environments";
  option (common.v1.permissions) = "write:clusters";
  // Both permissions are required (AND behavior by default)
}
```

## Empty Permissions

Some methods may have empty permissions (`""`) when the method doesn't require permission checks or when the authorization logic is custom and handled in the implementation:

```protobuf
rpc GetUserInfo(GetUserInfoRequest) returns (GetUserInfoResponse) {
  option (common.v1.permissions) = ""; // no permission check or custom logic in implementation
}
```

**Note**: Empty permissions does not mean no authentication is required. Authentication is still required by default (`requires_authentication = true`) unless explicitly disabled.

## OR Behavior with `requires_all_permissions`

By default, when multiple permissions are specified, **all** permissions must be satisfied (AND behavior). To enable OR behavior where **any** of the specified permissions grants access, set `requires_all_permissions = false`:

```protobuf
rpc ListHybridCloudEnvironments(ListHybridCloudEnvironmentsRequest) returns (ListHybridCloudEnvironmentsResponse) {
  option (common.v1.requires_all_permissions) = false;
  option (common.v1.permissions) = "read:hybrid_cloud_environments";
  option (common.v1.permissions) = "write:clusters";
}
```

## Changing Permissions Safely

To avoid breaking changes when modifying a method's permission requirements, follow this migration pattern:

1. **Add the new permission** alongside the existing one and **enable OR behavior**:
   ```protobuf
   rpc ExampleMethod(ExampleRequest) returns (ExampleResponse) {
     option (common.v1.requires_all_permissions) = false;
     option (common.v1.permissions) = "old:permission";     // existing
     option (common.v1.permissions) = "new:permission";     // new
   }
   ```

2. **Update clients** to use the new permission while the old one is still accepted.

3. **Remove the old permission** and **restore AND behavior** (if multiple permissions remain):
   ```protobuf
   rpc ExampleMethod(ExampleRequest) returns (ExampleResponse) {
     option (common.v1.permissions) = "new:permission";
   }
   ```

This approach ensures backward compatibility during the transition period.
