# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from datetime import datetime
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field

class Order(IntEnum):
    """
     TODO: Do we want to be this a enum (aka number, or string which is user-friendly in JSON)?
 The order of the returned list
    """
    ASC = 0
    DESC = 1

class ListOptions(BaseModel):
    """
     Options for a list request.
    """

# Maximum number of items to return.
# If not specified, a default number items are returned.
# Unless specified otherwise, the default number is DefaultPageSize.
    page_size: int = Field(default=0)
# Page to start with (defaults to 0).
    page: int = Field(default=0)
# Optional field to specify the sorting order.
    order_by: Order = Field(default=0)
# Optional timestamp to get the 'diff' as of a certain point.
# This field can be used to fetch items modified (created/updated/deleted) after this timestamp.
    since: datetime = Field(default_factory=datetime.now)

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

class IDOptions(BaseModel):
    """
     Options for a get-by-id request
    """

# System identifier of the object to fetch.
    id: str = Field(default="")

class YesOrNo(BaseModel):
    """
     Response for single boolean.
    """

# The actual result of the single boolean
    result: bool = Field(default=False)
