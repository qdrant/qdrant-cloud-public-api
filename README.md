# Qdrant Cloud API

This repository contains the Protocol Buffer definitions for the Qdrant Cloud API, as well as its generated code. 

We use [Buf](https://buf.build/) to lint the schemas and to generate language bindings. The layout and style of our `.proto` files follow their [style guide](https://docs.buf.build/best-practices/style-guide).

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
