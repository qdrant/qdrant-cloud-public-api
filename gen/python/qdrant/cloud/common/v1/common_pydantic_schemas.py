# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field


class Version(BaseModel):
    """
     Semantic version number.
    """

# Major version (increasing may break APIs)
    major: int = Field(default=0)
# Minor version (increased for new features)
    minor: int = Field(default=0)
# Patch version (increased for fixes)
    patch: int = Field(default=0)

class SecretKeyRef(BaseModel):
    """
     SecretKeyRef is a reference to a Kubernetes secret name and the key inside the secret
    """

# The name of the secret (in the same namespace as the QdrantCluster CRD instance)
# This is a required field
    name: str = Field(default="")
# The key inside the secret
# This is a required field
    key: str = Field(default="")

class KeyValue(BaseModel):
    """
     KeyValue is a key-value tuple (used in e.g. node selectors / annotations)
 The message represents an object for Kubernetes.
    """

# The key part of a key-value pair
    key: str = Field(default="")
# The value part of a key-value pair
    value: str = Field(default="")
