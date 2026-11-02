from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
MCP_TOOL_FIELD_NUMBER: _ClassVar[int]
mcp_tool: _descriptor.FieldDescriptor

class McpToolOptions(_message.Message):
    __slots__ = ("name", "ui_view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UI_VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    ui_view: McpUiView
    def __init__(self, name: _Optional[str] = ..., ui_view: _Optional[_Union[McpUiView, _Mapping]] = ...) -> None: ...

class McpUiView(_message.Message):
    __slots__ = ("timeseries", "health")
    TIMESERIES_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    timeseries: TimeseriesView
    health: HealthView
    def __init__(self, timeseries: _Optional[_Union[TimeseriesView, _Mapping]] = ..., health: _Optional[_Union[HealthView, _Mapping]] = ...) -> None: ...

class TimeseriesView(_message.Message):
    __slots__ = ("title", "series", "group_path", "group_label_field", "chart_type")
    class ChartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHART_TYPE_UNSPECIFIED: _ClassVar[TimeseriesView.ChartType]
        CHART_TYPE_LINE: _ClassVar[TimeseriesView.ChartType]
        CHART_TYPE_AREA: _ClassVar[TimeseriesView.ChartType]
        CHART_TYPE_BAR: _ClassVar[TimeseriesView.ChartType]
    CHART_TYPE_UNSPECIFIED: TimeseriesView.ChartType
    CHART_TYPE_LINE: TimeseriesView.ChartType
    CHART_TYPE_AREA: TimeseriesView.ChartType
    CHART_TYPE_BAR: TimeseriesView.ChartType
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    GROUP_PATH_FIELD_NUMBER: _ClassVar[int]
    GROUP_LABEL_FIELD_FIELD_NUMBER: _ClassVar[int]
    CHART_TYPE_FIELD_NUMBER: _ClassVar[int]
    title: str
    series: _containers.RepeatedCompositeFieldContainer[TimeseriesSeries]
    group_path: str
    group_label_field: str
    chart_type: TimeseriesView.ChartType
    def __init__(self, title: _Optional[str] = ..., series: _Optional[_Iterable[_Union[TimeseriesSeries, _Mapping]]] = ..., group_path: _Optional[str] = ..., group_label_field: _Optional[str] = ..., chart_type: _Optional[_Union[TimeseriesView.ChartType, str]] = ...) -> None: ...

class TimeseriesSeries(_message.Message):
    __slots__ = ("field", "label", "axis")
    class Axis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AXIS_UNSPECIFIED: _ClassVar[TimeseriesSeries.Axis]
        AXIS_LEFT: _ClassVar[TimeseriesSeries.Axis]
        AXIS_RIGHT: _ClassVar[TimeseriesSeries.Axis]
    AXIS_UNSPECIFIED: TimeseriesSeries.Axis
    AXIS_LEFT: TimeseriesSeries.Axis
    AXIS_RIGHT: TimeseriesSeries.Axis
    FIELD_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    AXIS_FIELD_NUMBER: _ClassVar[int]
    field: str
    label: str
    axis: TimeseriesSeries.Axis
    def __init__(self, field: _Optional[str] = ..., label: _Optional[str] = ..., axis: _Optional[_Union[TimeseriesSeries.Axis, str]] = ...) -> None: ...

class HealthView(_message.Message):
    __slots__ = ("subject", "companion_tools")
    class Subject(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUBJECT_UNSPECIFIED: _ClassVar[HealthView.Subject]
        SUBJECT_CLUSTER: _ClassVar[HealthView.Subject]
        SUBJECT_SPACE: _ClassVar[HealthView.Subject]
    SUBJECT_UNSPECIFIED: HealthView.Subject
    SUBJECT_CLUSTER: HealthView.Subject
    SUBJECT_SPACE: HealthView.Subject
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    COMPANION_TOOLS_FIELD_NUMBER: _ClassVar[int]
    subject: HealthView.Subject
    companion_tools: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, subject: _Optional[_Union[HealthView.Subject, str]] = ..., companion_tools: _Optional[_Iterable[str]] = ...) -> None: ...
