from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as _generated_pb2
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as _generated_pb2_1
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as _generated_pb2_1_1
from k8s.io.apimachinery.pkg.util.intstr import generated_pb2 as _generated_pb2_1_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Eviction(_message.Message):
    __slots__ = ("metadata", "deleteOptions")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DELETEOPTIONS_FIELD_NUMBER: _ClassVar[int]
    metadata: _generated_pb2.ObjectMeta
    deleteOptions: _generated_pb2.DeleteOptions
    def __init__(self, metadata: _Optional[_Union[_generated_pb2.ObjectMeta, _Mapping]] = ..., deleteOptions: _Optional[_Union[_generated_pb2.DeleteOptions, _Mapping]] = ...) -> None: ...

class PodDisruptionBudget(_message.Message):
    __slots__ = ("metadata", "spec", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: _generated_pb2.ObjectMeta
    spec: PodDisruptionBudgetSpec
    status: PodDisruptionBudgetStatus
    def __init__(self, metadata: _Optional[_Union[_generated_pb2.ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[PodDisruptionBudgetSpec, _Mapping]] = ..., status: _Optional[_Union[PodDisruptionBudgetStatus, _Mapping]] = ...) -> None: ...

class PodDisruptionBudgetList(_message.Message):
    __slots__ = ("metadata", "items")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    metadata: _generated_pb2.ListMeta
    items: _containers.RepeatedCompositeFieldContainer[PodDisruptionBudget]
    def __init__(self, metadata: _Optional[_Union[_generated_pb2.ListMeta, _Mapping]] = ..., items: _Optional[_Iterable[_Union[PodDisruptionBudget, _Mapping]]] = ...) -> None: ...

class PodDisruptionBudgetSpec(_message.Message):
    __slots__ = ("minAvailable", "selector", "maxUnavailable")
    MINAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    MAXUNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    minAvailable: _generated_pb2_1_1_1.IntOrString
    selector: _generated_pb2.LabelSelector
    maxUnavailable: _generated_pb2_1_1_1.IntOrString
    def __init__(self, minAvailable: _Optional[_Union[_generated_pb2_1_1_1.IntOrString, _Mapping]] = ..., selector: _Optional[_Union[_generated_pb2.LabelSelector, _Mapping]] = ..., maxUnavailable: _Optional[_Union[_generated_pb2_1_1_1.IntOrString, _Mapping]] = ...) -> None: ...

class PodDisruptionBudgetStatus(_message.Message):
    __slots__ = ("observedGeneration", "disruptedPods", "disruptionsAllowed", "currentHealthy", "desiredHealthy", "expectedPods", "conditions")
    class DisruptedPodsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _generated_pb2.Time
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_generated_pb2.Time, _Mapping]] = ...) -> None: ...
    OBSERVEDGENERATION_FIELD_NUMBER: _ClassVar[int]
    DISRUPTEDPODS_FIELD_NUMBER: _ClassVar[int]
    DISRUPTIONSALLOWED_FIELD_NUMBER: _ClassVar[int]
    CURRENTHEALTHY_FIELD_NUMBER: _ClassVar[int]
    DESIREDHEALTHY_FIELD_NUMBER: _ClassVar[int]
    EXPECTEDPODS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    observedGeneration: int
    disruptedPods: _containers.MessageMap[str, _generated_pb2.Time]
    disruptionsAllowed: int
    currentHealthy: int
    desiredHealthy: int
    expectedPods: int
    conditions: _containers.RepeatedCompositeFieldContainer[_generated_pb2.Condition]
    def __init__(self, observedGeneration: _Optional[int] = ..., disruptedPods: _Optional[_Mapping[str, _generated_pb2.Time]] = ..., disruptionsAllowed: _Optional[int] = ..., currentHealthy: _Optional[int] = ..., desiredHealthy: _Optional[int] = ..., expectedPods: _Optional[int] = ..., conditions: _Optional[_Iterable[_Union[_generated_pb2.Condition, _Mapping]]] = ...) -> None: ...
