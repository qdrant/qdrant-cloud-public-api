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

Authentication is typically handled via API keys passed in the `Authorization` header as a Bearer token (e.g., `Authorization: Bearer YOUR_AUTH0_KEY`) or Programmatic access key (e.g., `Authorization: apikey YOUR_PAK`).

## Interacting with the API

You can interact with the Qdrant Cloud API directly using tools like `grpcurl` (for gRPC) and `curl` (for REST/JSON), or by using the provided client libraries.
The API is used in the [TerraformProvider](https://registry.terraform.io/providers/qdrant/qdrant-cloud/latest) as well, so this can be used to interact as well.
The sources can be found [in Github here](https://github.com/qdrant/terraform-provider-qdrant-cloud).

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
grpcurl -H "Authorization: apikey YOUR_PAK" \
  -d '{"account_id": "<YOUR_ACCOUNT_ID>"}' \
  grpc.cloud.qdrant.io:443 \
  qdrant.cloud.cluster.v1.ClusterService/ListClusters   
```

*Note: Replace `YOUR_PAK` with your actual programatic access key. The specific service and method names can be found in the `.proto` files under the `proto/` directory or by using `grpcurl list` and `grpcurl describe`.*

Assuming you have exported your programatic access key in the environment variable `PAK`, you can replace the first line with:

```sh
grpcurl -H "Authorization: apikey ${PAK}" \
...
``` 

### Using `curl` (for REST/JSON)

The REST/JSON API is available over HTTPS and uses standard HTTP methods.

#### Example: Call a method with REST/JSON (e.g., Listclusters on ClusterService)

```sh
curl -X GET \
  -H "Authorization: apikey YOUR_PAK" \
  "https://api.cloud.qdrant.io/api/cluster/v1/accounts/<YOUR_ACCOUNT_ID>/clusters"
```

*Note: Replace `YOUR_PAK` with your actual programmatic access key. The exact REST path and HTTP method depend on the `google.api.http` annotations in the `.proto` files. You can typically infer these from the gRPC service and method names, or refer to the API documentation. Or check the output of grpcurl like

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

concider using `| jq` to format the output*

*For methods requiring a request body (e.g., POST, PUT), you would use the `-d` option with a JSON payload:*

```sh
curl -X POST \
  -H "Authorization: apikey YOUR_PAK" \
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

See (below)[## Using generated code] for more details.


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