# Qdrant Cloud API

Welcome to the Qdrant Cloud API [repository](https://github.com/qdrant/qdrant-cloud-public-api)!

## Introduction

This repository hosts the Protocol Buffer (`.proto`) definitions that define the contract for interacting with Qdrant Cloud platform services.

The Qdrant Cloud API offers two main ways to interact:

* **gRPC:** For high-performance, type-safe communication, ideal for backend services and (newer) clients.
* **REST/JSON:** A conventional HTTP/1.1 (and HTTP/2) based interface with JSON payloads, provided via gRPC Gateway for ease of use with tools.

This repository also contains generated client libraries (SDKs) for Go, Python, and TypeScript (found in the `gen/` directory) to help you get started quickly.

If you plan to contribute, please review the Protobuf guidelines to ensure our API remains consistent and user-friendly.

## API Endpoints

* **gRPC:** `grpc.cloud.qdrant.io:443`
* **REST/JSON:** `https://api.cloud.qdrant.io`

Authentication is typically handled via API keys (so called management keys), which are passed in the `Authorization` header as an apikey (e.g., `Authorization: apikey <YOUR_MANAGEMENT_KEY>`).

## Authentication & Authorization

The Qdrant Cloud API implements both authentication and permission-based authorization to secure access to its methods and resources:

- **Authentication**: Verifies the identity of the caller using API keys or user tokens
- **Authorization**: Controls access to specific operations based on permissions and roles

For detailed information about authentication requirements, actor types, permissions, multiple permissions, and safe permission migration patterns, see [Authentication & Authorization Documentation](docs/auth.md).

## Available Services

The Qdrant Cloud API is organized into several gRPC services, each responsible for a specific domain of functionality. Below is a list of the primary services available:

| Service Name            | Description   |
|-------------------------|---------------|
| [`AccountService`](/proto//qdrant/cloud/account/v1/account.proto) | Manages user accounts and their configurations. |
| [`AuthService`](/proto//qdrant/cloud/auth/v1/auth.proto) | Handles authentication and authorization for accessing cloud resources. |
| [`BackupService`](/proto//qdrant/cloud/cluster/backup/v1/backup.proto) | Manages backup and restore operations for Qdrant clusters. |
| [`BookingService`](/proto//qdrant/cloud/booking/v1/booking.proto) | Service for price listings-related information (called packages). |
| [`ClusterService`](/proto/qdrant/cloud/cluster/v1/cluster.proto) | Provides operations for creating, configuring, and managing Qdrant clusters. |
| [`DatabaseApiKeyService v1`](/proto/qdrant/cloud/cluster/auth/v1/database_api_key.proto) | Deprecated: Manages API keys for accessing data within Qdrant clusters. |
| [`DatabaseApiKeyService v2`](/proto/qdrant/cloud/cluster/auth/v2/database_api_key.proto) | Manages API keys for accessing data within Qdrant clusters. |
| [`HybridCloudService`](/proto/qdrant/cloud/hybrid/v1/hybrid_cloud.proto) | Service for for configuring hybrid cloud environments. |
| [`IAMService`](/proto/qdrant/cloud/iam/v1/iam.proto) | Service to configure IAM (identity and access management) objects. |
| [`MonitoringService`](proto/qdrant/cloud/monitoring/v1/monitoring.proto) | Provides access to monitoring data such as cluster metrics, logs, and events. |
| [`PlatformService`](/proto//qdrant/cloud/platform/v1/platform.proto) | Service to query for cloud provider & regional information. |

*Note: The `Service Name` links point to the respective Protocol Buffer file where that service is formally defined.
You can explore these files for detailed information on methods, request/response messages, and field validations.*

## Interacting with the API

You can interact with the Qdrant Cloud API directly using tools like `grpcurl` (for gRPC) and `curl` (for REST/JSON), or by using the provided client libraries.

The API is used in the [TerraformProvider](https://registry.terraform.io/providers/qdrant/qdrant-cloud/latest) as well, so this can be used to interact as well.
The sources for the TerraformProvider can be found [in Github here](https://github.com/qdrant/terraform-provider-qdrant-cloud).

### Using `grpcurl` (for gRPC)

`grpcurl` is a command-line tool that lets you interact with gRPC servers. It's great for exploring and testing APIs.

#### Example: List available services with `grpcurl`

```sh
grpcurl grpc.cloud.qdrant.io:443 list
```

#### Example: Describe a service (e.g., ClusterService)

```sh
grpcurl grpc.cloud.qdrant.io:443 describe qdrant.cloud.cluster.v1.ClusterService
```

#### Example: Call a method with gRPC (e.g., ListClusters on ClusterService)

```sh
grpcurl -H "Authorization: apikey <YOUR_MANAGEMENT_KEY>" \
  -d '{"account_id": "<YOUR_ACCOUNT_ID>"}' \
  grpc.cloud.qdrant.io:443 \
  qdrant.cloud.cluster.v1.ClusterService/ListClusters   
```

*Note: Replace `<YOUR_MANAGEMENT_KEY>` with your actual management key and `<YOUR_ACCOUNT_ID>` with your account ID. The specific service and method names can be found in the `.proto` files under the `proto/` directory or by using `grpcurl list` and `grpcurl describe`.*

Assuming you have exported your management key in the environment variable `MANAGEMENT_KEY`, you can replace the first line with:

```sh
grpcurl -H "Authorization: apikey ${MANAGEMENT_KEY}" \
...
``` 

### Using `curl` (for REST/JSON)

The REST/JSON API is available over HTTPS and uses standard HTTP methods.

#### Example: Call a method with REST/JSON (e.g., Listclusters on ClusterService)

```sh
curl -X GET \
  -H "Authorization: apikey <YOUR_MANAGEMENT_KEY>" \
  "https://api.cloud.qdrant.io/api/cluster/v1/accounts/<YOUR_ACCOUNT_ID>/clusters"
```

*Note: Replace `<YOUR_MANAGEMENT_KEY>` with your actual management key and `<YOUR_ACCOUNT_ID>` with your account ID. The exact REST path and HTTP method depend on the `google.api.http` annotations in the `.proto` files.*

You can typically infer these from the gRPC service and method names, or refer to the API documentation. Or check the output of grpcurl like:

```
  rpc CreateCluster ( .qdrant.cloud.cluster.v1.CreateClusterRequest ) returns ( .qdrant.cloud.cluster.v1.CreateClusterResponse ) {
    option (.google.api.http) = {
      post: "/api/cluster/v1/accounts/{cluster.account_id}/clusters",
      body: "*"
    };
    option (.qdrant.cloud.common.v1.permissions) = "write:clusters";
  }
  ...
```

Consider using `| jq` to format the output.

*For methods requiring a request body (e.g., POST, PUT), you would use the `-d` option with a JSON payload:*

```sh
curl -X POST \
  -H "Authorization: apikey <YOUR_MANAGEMENT_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"field1": "value1", "field2": "value2"}' \
  "https://api.cloud.qdrant.io/v2/your-service/your-resource"
```

### Using Generated Client Libraries (SDKs)

The `gen/` directory in this repository contains pre-generated client libraries (SDKs) to help you integrate the Qdrant Cloud API into your applications. These libraries provide type-safe methods to call the gRPC services directly.

We currently provide support for:
* **Go:** `gen/go/`
* **Python:** `gen/python/`
* **TypeScript:** `gen/ts/`

See [below](#using-generated-code) for more details.


### Paginated resources

All listing methods (e.g. `ListClusters`) currently return all active resources in a single response. To provide better usability and performance, we are gradually introducing pagination so resources can be retrieved in chunks.

A `ListXXX` method supports pagination if its request message includes the fields:

- `page_size` — maximum number of items per page.
- `page_token` — token to request the next page.

and the response message includes:

- `items` — list of resources.
- `total_size` — total number of matching resources.
- `next_page_token` — token to request the next page (omit if there are no more results).

This is an example of using pagination with the `BackupService.ListBackups` method:

- Request the first 20 backups:

``` sh
grpcurl -H "Authorization: apikey <YOUR_MANAGEMENT_KEY>" \
  -d '{"account_id": "<YOUR_ACCOUNT_ID>", "page_size": 20}' \
  grpc.cloud.qdrant.io:443 \
  qdrant.cloud.cluster.backup.v1.BackupService/ListBackups
```

``` sh
{
  "items": [
    {
      "id": "f7b60c5e-2f7c-450f-926d-4c43948b71a9",
      "createdAt": "2025-05-06T07:53:10.290771Z",
      "accountId": "<REDACTED>",
      "clusterId": "a71f4794-504e-4d19-b994-32450e10e783",
      "name": "qdrant-a71f4794-504e-4d19-b994-32450e10e783-snapshot-1746517990",
      "status": "BACKUP_STATUS_SUCCEEDED",
      "backupDuration": "30s"
    },
    ... 19 more ...
  ],
  "totalSize": 43,
  "nextPageToken": "WyIyMDI1LTA1LTI4VDA4OjI1OjQzLjkxNDg1NyswMDowMCIsICJjYTc3Mzk3YS1jNTRjLTQ3NGQtOGEzOS0xMzZmMGZlMWI3ODUiXQ=="
}
```

- Request the next page, passing `page_token`:

``` sh
grpcurl -H "Authorization: apikey <YOUR_MANAGEMENT_KEY>" \
  -d '{"account_id": "<YOUR_ACCOUNT_ID>", "page_size": 20, "page_token":"WyIyMDI1LTA1LTI4VDA4OjI1OjQzLjkxNDg1NyswMDowMCIsICJjYTc3Mzk3YS1jNTRjLTQ3NGQtOGEzOS0xMzZmMGZlMWI3ODUiXQ=="}' \
  grpc.cloud.qdrant.io:443 \
  qdrant.cloud.cluster.backup.v1.BackupService/ListBackups
```

``` sh
{
  "items": [
    {
      "id": "84deb667-36a0-4d1f-a095-50f9b2a9dec4",
      "createdAt": "2025-06-12T14:14:22.811915Z",
      "accountId": "<REDACTED>",
      "clusterId": "4d9fc7fd-1182-42fd-abce-7c8d4c3f5f32",
      "name": "qdrant-4d9fc7fd-1182-42fd-abce-7c8d4c3f5f32-snapshot-1749737662",
      "status": "BACKUP_STATUS_SUCCEEDED",
      "backupDuration": "1s"
    },
    ... 19 more ...
  ],
  "totalSize": 43,
  "nextPageToken": "WyIyMDI1LTA2LTI2VDE3OjQ4OjIzLjY2NjQ0MSswMDowMCIsICJhYzc1MDc4MC02N2ViLTRjZmItOTI3ZC0zYmZhZTY4OTk5OGUiXQ=="
}
```

## Working with Protocol Buffer definitions

We use [Buf](https://buf.build/) to lint the schemas and to generate language bindings. 

Additionally, there are [these guidelines](CONTRIBUTING.md#protobuf-guidelines) to ensure our API remains consistent and user-friendly. Please follow them when contributing.

This project leverages Make to automate common tasks. To view all available commands, you can run:

``` sh
make help
```

### Adding/updating proto files

The API schema definitions are located under the `proto/` directory. Whenever you add or modify a `.proto` file, make sure that you format and lint it accordingly. You can do that running:

``` sh
make format
make lint
```

### Generating code

After changing a `.proto` file, you should regenerate the different language bindings:

``` sh
make generate
```
## Using generated code

### Go projects

You can import this project and use it in your go project. Ex:

``` go
import (
    ...
    qdrantauthv1 "github.com/qdrant/qdrant-cloud-public-api/gen/go/qdrant/cloud/auth/v1"
)

```

### Python projects

- Make sure you are authorised to gcloud. `gcloud auth application-default login`

- Install the package:

    ``` sh
    # install auth tool
    uv tool install keyring --with keyrings.google-artifactregistry-auth --force
    # install
    uv add qdrant-cloud-public-api --keyring-provider subprocess  --index https://oauth2accesstoken@us-python.pkg.dev/qdrant-cloud/python/simple
    ```


- Now you can import the generated code in your python project. Ex:

    ```python
    from qdrant.cloud.booking.v2.booking_pb2_grpc import BookingServiceServicer
    from qdrant.cloud.booking.v2.booking_pb2 import ListPackagesRequest
    
    
    def main():
        print(BookingServiceServicer)
        print(ListPackagesRequest)
    
    
    if __name__ == "__main__":
        main()
    ```


### Typescript projects

- Make sure you are authorised to gcloud. `gcloud auth application-default login`
- Create `.npmrc` file in the root of your project with the following content:

    ```text
    @qdrant:registry=https://us-npm.pkg.dev/qdrant-cloud/npm/
    //us-npm.pkg.dev/qdrant-cloud/npm/:always-auth=true
    ```

- Add auth script to your package.json file:

    ```json
      "scripts": {
        ...
        "artifactregistry-login": "npx --registry=https://registry.npmjs.org google-artifactregistry-auth"
        ...
      },
    ```

- Run the auth script:

    ```shell
    npm run artifactregistry-login
    ```

- Install the package:
    ``` sh
    npm  install @qdrant/qdrant-cloud-public-api
    ```

- Now you can import the generated code in your typescript project. Ex:

  ```typescript
  import * as grpc from '@qdrant/qdrant-cloud-public-api/qdrant/cloud/cluster/v1/cluster_pb.js';
  import { DatabaseApiKeyService } from "@qdrant/qdrant-cloud-public-api/qdrant/cloud/cluster/auth/v1/database_api_key_pb.js";
  
  console.log('Loaded service definition keys:', Object.keys(grpc));
  console.log(DatabaseApiKeyService);
  ```

## [Release Process](docs/release.md)
