from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTOR_TYPE_UNSPECIFIED: _ClassVar[ActorType]
    ACTOR_TYPE_USER: _ClassVar[ActorType]
    ACTOR_TYPE_MANAGEMENT_KEY: _ClassVar[ActorType]
    ACTOR_TYPE_SERVICE_ACCOUNT: _ClassVar[ActorType]
ACTOR_TYPE_UNSPECIFIED: ActorType
ACTOR_TYPE_USER: ActorType
ACTOR_TYPE_MANAGEMENT_KEY: ActorType
ACTOR_TYPE_SERVICE_ACCOUNT: ActorType
PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
permissions: _descriptor.FieldDescriptor
ACCOUNT_ID_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
account_id_expression: _descriptor.FieldDescriptor
REQUIRES_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
requires_authentication: _descriptor.FieldDescriptor
SUPPORTED_ACTOR_TYPES_FIELD_NUMBER: _ClassVar[int]
supported_actor_types: _descriptor.FieldDescriptor
REQUIRES_ALL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
requires_all_permissions: _descriptor.FieldDescriptor
MAX_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
max_message_size: _descriptor.FieldDescriptor
LOG_FIELDS_FIELD_NUMBER: _ClassVar[int]
log_fields: _descriptor.FieldDescriptor

class LogField(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_expression: str
    def __init__(self, name: _Optional[str] = ..., field_expression: _Optional[str] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ()
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    patch: int
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., patch: _Optional[int] = ...) -> None: ...

class SecretKeyRef(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    key: str
    def __init__(self, name: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class KeyValue(_message.Message):
    __slots__ = ()
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class TopologySpreadConstraint(_message.Message):
    __slots__ = ()
    MAX_SKEW_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_KEY_FIELD_NUMBER: _ClassVar[int]
    WHEN_UNSATISFIABLE_FIELD_NUMBER: _ClassVar[int]
    max_skew: int
    topology_key: str
    when_unsatisfiable: str
    def __init__(self, max_skew: _Optional[int] = ..., topology_key: _Optional[str] = ..., when_unsatisfiable: _Optional[str] = ...) -> None: ...

class LabelSelectorRequirement(_message.Message):
    __slots__ = ()
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    operator: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., operator: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class LabelSelector(_message.Message):
    __slots__ = ()
    class MatchLabelsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MATCH_LABELS_FIELD_NUMBER: _ClassVar[int]
    MATCH_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    match_labels: _containers.ScalarMap[str, str]
    match_expressions: _containers.RepeatedCompositeFieldContainer[LabelSelectorRequirement]
    def __init__(self, match_labels: _Optional[_Mapping[str, str]] = ..., match_expressions: _Optional[_Iterable[_Union[LabelSelectorRequirement, _Mapping]]] = ...) -> None: ...

class IPBlock(_message.Message):
    __slots__ = ()
    CIDR_FIELD_NUMBER: _ClassVar[int]
    EXCEPT_FIELD_NUMBER: _ClassVar[int]
    cidr: str
    def __init__(self, cidr: _Optional[str] = ..., **kwargs) -> None: ...

class PeerSelector(_message.Message):
    __slots__ = ()
    POD_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    pod_selector: LabelSelector
    namespace_selector: LabelSelector
    def __init__(self, pod_selector: _Optional[_Union[LabelSelector, _Mapping]] = ..., namespace_selector: _Optional[_Union[LabelSelector, _Mapping]] = ...) -> None: ...

class NetworkPolicyPeer(_message.Message):
    __slots__ = ()
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    IP_BLOCK_FIELD_NUMBER: _ClassVar[int]
    selector: PeerSelector
    ip_block: IPBlock
    def __init__(self, selector: _Optional[_Union[PeerSelector, _Mapping]] = ..., ip_block: _Optional[_Union[IPBlock, _Mapping]] = ...) -> None: ...

class NetworkPolicyPort(_message.Message):
    __slots__ = ()
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PORT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PORT_NAME_FIELD_NUMBER: _ClassVar[int]
    END_PORT_FIELD_NUMBER: _ClassVar[int]
    protocol: str
    port_number: int
    port_name: str
    end_port: int
    def __init__(self, protocol: _Optional[str] = ..., port_number: _Optional[int] = ..., port_name: _Optional[str] = ..., end_port: _Optional[int] = ...) -> None: ...

class NetworkPolicyIngressRule(_message.Message):
    __slots__ = ()
    PORTS_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    ports: _containers.RepeatedCompositeFieldContainer[NetworkPolicyPort]
    def __init__(self, ports: _Optional[_Iterable[_Union[NetworkPolicyPort, _Mapping]]] = ..., **kwargs) -> None: ...

class NetworkPolicyEgressRule(_message.Message):
    __slots__ = ()
    PORTS_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    ports: _containers.RepeatedCompositeFieldContainer[NetworkPolicyPort]
    to: _containers.RepeatedCompositeFieldContainer[NetworkPolicyPeer]
    def __init__(self, ports: _Optional[_Iterable[_Union[NetworkPolicyPort, _Mapping]]] = ..., to: _Optional[_Iterable[_Union[NetworkPolicyPeer, _Mapping]]] = ...) -> None: ...
