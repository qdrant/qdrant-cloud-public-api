# Qdrant Cloud API

This repository contains the Protocol Buffer definitions for the Qdrant Cloud API, as well as its generated code. 

We use [Buf](https://buf.build/) to lint the schemas and to generate language bindings. 

Additionally, there are [these guidelines](CONTRIBUTING.md#protobuf-guidelines) to ensure our API remains consistent and user-friendly. Please follow them when contributing.

This project leverages Make to automate common tasks. To view all available commands, you can run:

``` sh
make help
```

## Working with Protocol Buffer definitions

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

- Now you can import the generated code in your python project. Ex:

    ```typescript
    import { ClusterService } from '@qdrant/qdrant-cloud-public-api/qdrant/cloud/cluster/v1/cluster_pb'
    
    console.log("Available cluster service:", ClusterService);
    ```

## [Release Process](docs/release.md)