from k8s.io.api.core.v1 import generated_pb2 as _generated_pb2
from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as _generated_pb2_1
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as _generated_pb2_1_1
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as _generated_pb2_1_1_1
from k8s.io.apimachinery.pkg.util.intstr import generated_pb2 as _generated_pb2_1_1_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HTTPIngressPath(_message.Message):
    __slots__ = ()
    PATH_FIELD_NUMBER: _ClassVar[int]
    PATHTYPE_FIELD_NUMBER: _ClassVar[int]
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    path: str
    pathType: str
    backend: IngressBackend
    def __init__(self, path: _Optional[str] = ..., pathType: _Optional[str] = ..., backend: _Optional[_Union[IngressBackend, _Mapping]] = ...) -> None: ...

class HTTPIngressRuleValue(_message.Message):
    __slots__ = ()
    PATHS_FIELD_NUMBER: _ClassVar[int]
    paths: _containers.RepeatedCompositeFieldContainer[HTTPIngressPath]
    def __init__(self, paths: _Optional[_Iterable[_Union[HTTPIngressPath, _Mapping]]] = ...) -> None: ...

class IPBlock(_message.Message):
    __slots__ = ()
    CIDR_FIELD_NUMBER: _ClassVar[int]
    EXCEPT_FIELD_NUMBER: _ClassVar[int]
    cidr: str
    def __init__(self, cidr: _Optional[str] = ..., **kwargs) -> None: ...

class Ingress(_message.Message):
    __slots__ = ()
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: _generated_pb2_1.ObjectMeta
    spec: IngressSpec
    status: IngressStatus
    def __init__(self, metadata: _Optional[_Union[_generated_pb2_1.ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[IngressSpec, _Mapping]] = ..., status: _Optional[_Union[IngressStatus, _Mapping]] = ...) -> None: ...

class IngressBackend(_message.Message):
    __slots__ = ()
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    service: IngressServiceBackend
    resource: _generated_pb2.TypedLocalObjectReference
    def __init__(self, service: _Optional[_Union[IngressServiceBackend, _Mapping]] = ..., resource: _Optional[_Union[_generated_pb2.TypedLocalObjectReference, _Mapping]] = ...) -> None: ...

class IngressClass(_message.Message):
    __slots__ = ()
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    metadata: _generated_pb2_1.ObjectMeta
    spec: IngressClassSpec
    def __init__(self, metadata: _Optional[_Union[_generated_pb2_1.ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[IngressClassSpec, _Mapping]] = ...) -> None: ...

class IngressClassList(_message.Message):
    __slots__ = ()
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    metadata: _generated_pb2_1.ListMeta
    items: _containers.RepeatedCompositeFieldContainer[IngressClass]
    def __init__(self, metadata: _Optional[_Union[_generated_pb2_1.ListMeta, _Mapping]] = ..., items: _Optional[_Iterable[_Union[IngressClass, _Mapping]]] = ...) -> None: ...

class IngressClassParametersReference(_message.Message):
    __slots__ = ()
    APIGROUP_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    aPIGroup: str
    kind: str
    name: str
    scope: str
    namespace: str
    def __init__(self, aPIGroup: _Optional[str] = ..., kind: _Optional[str] = ..., name: _Optional[str] = ..., scope: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class IngressClassSpec(_message.Message):
    __slots__ = ()
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    controller: str
    parameters: IngressClassParametersReference
    def __init__(self, controller: _Optional[str] = ..., parameters: _Optional[_Union[IngressClassParametersReference, _Mapping]] = ...) -> None: ...

class IngressList(_message.Message):
    __slots__ = ()
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    metadata: _generated_pb2_1.ListMeta
    items: _containers.RepeatedCompositeFieldContainer[Ingress]
    def __init__(self, metadata: _Optional[_Union[_generated_pb2_1.ListMeta, _Mapping]] = ..., items: _Optional[_Iterable[_Union[Ingress, _Mapping]]] = ...) -> None: ...

class IngressRule(_message.Message):
    __slots__ = ()
    HOST_FIELD_NUMBER: _ClassVar[int]
    INGRESSRULEVALUE_FIELD_NUMBER: _ClassVar[int]
    host: str
    ingressRuleValue: IngressRuleValue
    def __init__(self, host: _Optional[str] = ..., ingressRuleValue: _Optional[_Union[IngressRuleValue, _Mapping]] = ...) -> None: ...

class IngressRuleValue(_message.Message):
    __slots__ = ()
    HTTP_FIELD_NUMBER: _ClassVar[int]
    http: HTTPIngressRuleValue
    def __init__(self, http: _Optional[_Union[HTTPIngressRuleValue, _Mapping]] = ...) -> None: ...

class IngressServiceBackend(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    name: str
    port: ServiceBackendPort
    def __init__(self, name: _Optional[str] = ..., port: _Optional[_Union[ServiceBackendPort, _Mapping]] = ...) -> None: ...

class IngressSpec(_message.Message):
    __slots__ = ()
    INGRESSCLASSNAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULTBACKEND_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    ingressClassName: str
    defaultBackend: IngressBackend
    tls: _containers.RepeatedCompositeFieldContainer[IngressTLS]
    rules: _containers.RepeatedCompositeFieldContainer[IngressRule]
    def __init__(self, ingressClassName: _Optional[str] = ..., defaultBackend: _Optional[_Union[IngressBackend, _Mapping]] = ..., tls: _Optional[_Iterable[_Union[IngressTLS, _Mapping]]] = ..., rules: _Optional[_Iterable[_Union[IngressRule, _Mapping]]] = ...) -> None: ...

class IngressStatus(_message.Message):
    __slots__ = ()
    LOADBALANCER_FIELD_NUMBER: _ClassVar[int]
    loadBalancer: _generated_pb2.LoadBalancerStatus
    def __init__(self, loadBalancer: _Optional[_Union[_generated_pb2.LoadBalancerStatus, _Mapping]] = ...) -> None: ...

class IngressTLS(_message.Message):
    __slots__ = ()
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    SECRETNAME_FIELD_NUMBER: _ClassVar[int]
    hosts: _containers.RepeatedScalarFieldContainer[str]
    secretName: str
    def __init__(self, hosts: _Optional[_Iterable[str]] = ..., secretName: _Optional[str] = ...) -> None: ...

class NetworkPolicy(_message.Message):
    __slots__ = ()
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    metadata: _generated_pb2_1.ObjectMeta
    spec: NetworkPolicySpec
    def __init__(self, metadata: _Optional[_Union[_generated_pb2_1.ObjectMeta, _Mapping]] = ..., spec: _Optional[_Union[NetworkPolicySpec, _Mapping]] = ...) -> None: ...

class NetworkPolicyEgressRule(_message.Message):
    __slots__ = ()
    PORTS_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    ports: _containers.RepeatedCompositeFieldContainer[NetworkPolicyPort]
    to: _containers.RepeatedCompositeFieldContainer[NetworkPolicyPeer]
    def __init__(self, ports: _Optional[_Iterable[_Union[NetworkPolicyPort, _Mapping]]] = ..., to: _Optional[_Iterable[_Union[NetworkPolicyPeer, _Mapping]]] = ...) -> None: ...

class NetworkPolicyIngressRule(_message.Message):
    __slots__ = ()
    PORTS_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    ports: _containers.RepeatedCompositeFieldContainer[NetworkPolicyPort]
    def __init__(self, ports: _Optional[_Iterable[_Union[NetworkPolicyPort, _Mapping]]] = ..., **kwargs) -> None: ...

class NetworkPolicyList(_message.Message):
    __slots__ = ()
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    metadata: _generated_pb2_1.ListMeta
    items: _containers.RepeatedCompositeFieldContainer[NetworkPolicy]
    def __init__(self, metadata: _Optional[_Union[_generated_pb2_1.ListMeta, _Mapping]] = ..., items: _Optional[_Iterable[_Union[NetworkPolicy, _Mapping]]] = ...) -> None: ...

class NetworkPolicyPeer(_message.Message):
    __slots__ = ()
    PODSELECTOR_FIELD_NUMBER: _ClassVar[int]
    NAMESPACESELECTOR_FIELD_NUMBER: _ClassVar[int]
    IPBLOCK_FIELD_NUMBER: _ClassVar[int]
    podSelector: _generated_pb2_1.LabelSelector
    namespaceSelector: _generated_pb2_1.LabelSelector
    ipBlock: IPBlock
    def __init__(self, podSelector: _Optional[_Union[_generated_pb2_1.LabelSelector, _Mapping]] = ..., namespaceSelector: _Optional[_Union[_generated_pb2_1.LabelSelector, _Mapping]] = ..., ipBlock: _Optional[_Union[IPBlock, _Mapping]] = ...) -> None: ...

class NetworkPolicyPort(_message.Message):
    __slots__ = ()
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ENDPORT_FIELD_NUMBER: _ClassVar[int]
    protocol: str
    port: _generated_pb2_1_1_1_1.IntOrString
    endPort: int
    def __init__(self, protocol: _Optional[str] = ..., port: _Optional[_Union[_generated_pb2_1_1_1_1.IntOrString, _Mapping]] = ..., endPort: _Optional[int] = ...) -> None: ...

class NetworkPolicySpec(_message.Message):
    __slots__ = ()
    PODSELECTOR_FIELD_NUMBER: _ClassVar[int]
    INGRESS_FIELD_NUMBER: _ClassVar[int]
    EGRESS_FIELD_NUMBER: _ClassVar[int]
    POLICYTYPES_FIELD_NUMBER: _ClassVar[int]
    podSelector: _generated_pb2_1.LabelSelector
    ingress: _containers.RepeatedCompositeFieldContainer[NetworkPolicyIngressRule]
    egress: _containers.RepeatedCompositeFieldContainer[NetworkPolicyEgressRule]
    policyTypes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, podSelector: _Optional[_Union[_generated_pb2_1.LabelSelector, _Mapping]] = ..., ingress: _Optional[_Iterable[_Union[NetworkPolicyIngressRule, _Mapping]]] = ..., egress: _Optional[_Iterable[_Union[NetworkPolicyEgressRule, _Mapping]]] = ..., policyTypes: _Optional[_Iterable[str]] = ...) -> None: ...

class ServiceBackendPort(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    name: str
    number: int
    def __init__(self, name: _Optional[str] = ..., number: _Optional[int] = ...) -> None: ...
