import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qdrant.cloud.common.v1 import common_pb2 as _common_pb2
from qdrant.cloud.event.v1 import events_pb2 as _events_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProjectStatePhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROJECT_STATE_PHASE_UNSPECIFIED: _ClassVar[ProjectStatePhase]
    PROJECT_STATE_PHASE_READY: _ClassVar[ProjectStatePhase]
    PROJECT_STATE_PHASE_PROCESSING: _ClassVar[ProjectStatePhase]
    PROJECT_STATE_PHASE_DISABLED: _ClassVar[ProjectStatePhase]
PROJECT_STATE_PHASE_UNSPECIFIED: ProjectStatePhase
PROJECT_STATE_PHASE_READY: ProjectStatePhase
PROJECT_STATE_PHASE_PROCESSING: ProjectStatePhase
PROJECT_STATE_PHASE_DISABLED: ProjectStatePhase

class ListProjectsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class ListProjectsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Project]
    def __init__(self, items: _Optional[_Iterable[_Union[Project, _Mapping]]] = ...) -> None: ...

class CreateProjectRequest(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class CreateProjectResponse(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class UpdateProjectRequest(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class UpdateProjectResponse(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class DeleteProjectRequest(_message.Message):
    __slots__ = ("account_id", "project_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    project_id: str
    def __init__(self, account_id: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeleteProjectResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Project(_message.Message):
    __slots__ = ("id", "created_at", "account_id", "name", "deleted_at", "cloud_provider_id", "cloud_provider_region_id", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    account_id: str
    name: str
    deleted_at: _timestamp_pb2.Timestamp
    cloud_provider_id: str
    cloud_provider_region_id: str
    state: ProjectState
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., name: _Optional[str] = ..., deleted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cloud_provider_id: _Optional[str] = ..., cloud_provider_region_id: _Optional[str] = ..., state: _Optional[_Union[ProjectState, _Mapping]] = ...) -> None: ...

class ProjectState(_message.Message):
    __slots__ = ("phase", "reason", "endpoint")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    phase: ProjectStatePhase
    reason: str
    endpoint: ProjectEndpoint
    def __init__(self, phase: _Optional[_Union[ProjectStatePhase, str]] = ..., reason: _Optional[str] = ..., endpoint: _Optional[_Union[ProjectEndpoint, _Mapping]] = ...) -> None: ...

class ProjectEndpoint(_message.Message):
    __slots__ = ("url", "rest_port", "grpc_port")
    URL_FIELD_NUMBER: _ClassVar[int]
    REST_PORT_FIELD_NUMBER: _ClassVar[int]
    GRPC_PORT_FIELD_NUMBER: _ClassVar[int]
    url: str
    rest_port: int
    grpc_port: int
    def __init__(self, url: _Optional[str] = ..., rest_port: _Optional[int] = ..., grpc_port: _Optional[int] = ...) -> None: ...
