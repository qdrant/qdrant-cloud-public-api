# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from qdrant.cloud.iam.v1 import iam_pb2 as qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2


class IAMServiceStub(object):
    """IAMService is the API used to configure IAM (identity and access management) objects.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAuthenticatedUser = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/GetAuthenticatedUser',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetAuthenticatedUserRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetAuthenticatedUserResponse.FromString,
                _registered_method=True)
        self.UpdateUser = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/UpdateUser',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateUserResponse.FromString,
                _registered_method=True)
        self.GetUserConsent = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/GetUserConsent',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetUserConsentRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetUserConsentResponse.FromString,
                _registered_method=True)
        self.RecordUserConsent = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/RecordUserConsent',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.RecordUserConsentRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.RecordUserConsentResponse.FromString,
                _registered_method=True)
        self.ListPermissions = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/ListPermissions',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListPermissionsRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListPermissionsResponse.FromString,
                _registered_method=True)
        self.ListRoles = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/ListRoles',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListRolesRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListRolesResponse.FromString,
                _registered_method=True)
        self.GetRole = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/GetRole',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetRoleRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetRoleResponse.FromString,
                _registered_method=True)
        self.CreateRole = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/CreateRole',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.CreateRoleRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.CreateRoleResponse.FromString,
                _registered_method=True)
        self.UpdateRole = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/UpdateRole',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateRoleRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateRoleResponse.FromString,
                _registered_method=True)
        self.DeleteRole = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/DeleteRole',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.DeleteRoleRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.DeleteRoleResponse.FromString,
                _registered_method=True)
        self.ListEffectivePermissions = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/ListEffectivePermissions',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListEffectivePermissionsRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListEffectivePermissionsResponse.FromString,
                _registered_method=True)
        self.ListUserRoles = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/ListUserRoles',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListUserRolesRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListUserRolesResponse.FromString,
                _registered_method=True)
        self.AssignUserRoles = channel.unary_unary(
                '/qdrant.cloud.iam.v1.IAMService/AssignUserRoles',
                request_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.AssignUserRolesRequest.SerializeToString,
                response_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.AssignUserRolesResponse.FromString,
                _registered_method=True)


class IAMServiceServicer(object):
    """IAMService is the API used to configure IAM (identity and access management) objects.
    """

    def GetAuthenticatedUser(self, request, context):
        """Gets the authenticated user.
        Required permissions:
        - None (authenticated only)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Updates the user identified by the given ID.
        Required permissions:
        - write:user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserConsent(self, request, context):
        """Gets the authenticated user's consent status for a specific legal document.
        Required permissions:
        - None (authenticated only)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecordUserConsent(self, request, context):
        """Records the authenticated user's consent for a legal document.
        Required permissions:
        - write:user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPermissions(self, request, context):
        """Lists all permissions known in the system for the provided account.
        Note: If you want to get a list of permissions available for you, please use GetEffectivePermissions instead.
        Required permissions:
        - read:roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRoles(self, request, context):
        """Lists all roles in the account identified by the given ID.
        Required permissions:
        - read:roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRole(self, request, context):
        """Gets a role for the account identified by the given ID.
        Required permissions:
        - read:roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRole(self, request, context):
        """Creates a role for the account identified by the given ID.
        Note: The role_type must be ROLE_TYPE_CUSTOM.
        Required permissions:
        - write:roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRole(self, request, context):
        """Updates a role in the account identified by the given ID.
        Note: The role_type must be ROLE_TYPE_CUSTOM.
        Required permissions:
        - write:roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRole(self, request, context):
        """Deletes a role in the account identified by the given ID.
        Note: The role_type must be ROLE_TYPE_CUSTOM.
        Required permissions:
        - delete:roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEffectivePermissions(self, request, context):
        """Lists the effective permissions for the user in the account identified by the given ID.
        Required permissions:
        - read:roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUserRoles(self, request, context):
        """List roles of the user identified by the given ID.
        Required permissions:
        - read:roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssignUserRoles(self, request, context):
        """Assigns the provided roles to the user in the account identified by the given ID.
        Required permissions:
        - write:roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IAMServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAuthenticatedUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAuthenticatedUser,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetAuthenticatedUserRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetAuthenticatedUserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateUserRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateUserResponse.SerializeToString,
            ),
            'GetUserConsent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserConsent,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetUserConsentRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetUserConsentResponse.SerializeToString,
            ),
            'RecordUserConsent': grpc.unary_unary_rpc_method_handler(
                    servicer.RecordUserConsent,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.RecordUserConsentRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.RecordUserConsentResponse.SerializeToString,
            ),
            'ListPermissions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPermissions,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListPermissionsRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListPermissionsResponse.SerializeToString,
            ),
            'ListRoles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRoles,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListRolesRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListRolesResponse.SerializeToString,
            ),
            'GetRole': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRole,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetRoleRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetRoleResponse.SerializeToString,
            ),
            'CreateRole': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRole,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.CreateRoleRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.CreateRoleResponse.SerializeToString,
            ),
            'UpdateRole': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRole,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateRoleRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateRoleResponse.SerializeToString,
            ),
            'DeleteRole': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRole,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.DeleteRoleRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.DeleteRoleResponse.SerializeToString,
            ),
            'ListEffectivePermissions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEffectivePermissions,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListEffectivePermissionsRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListEffectivePermissionsResponse.SerializeToString,
            ),
            'ListUserRoles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUserRoles,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListUserRolesRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListUserRolesResponse.SerializeToString,
            ),
            'AssignUserRoles': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignUserRoles,
                    request_deserializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.AssignUserRolesRequest.FromString,
                    response_serializer=qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.AssignUserRolesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'qdrant.cloud.iam.v1.IAMService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('qdrant.cloud.iam.v1.IAMService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class IAMService(object):
    """IAMService is the API used to configure IAM (identity and access management) objects.
    """

    @staticmethod
    def GetAuthenticatedUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/GetAuthenticatedUser',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetAuthenticatedUserRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetAuthenticatedUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/UpdateUser',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateUserRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUserConsent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/GetUserConsent',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetUserConsentRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetUserConsentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RecordUserConsent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/RecordUserConsent',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.RecordUserConsentRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.RecordUserConsentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListPermissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/ListPermissions',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListPermissionsRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListPermissionsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListRoles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/ListRoles',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListRolesRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListRolesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/GetRole',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetRoleRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.GetRoleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/CreateRole',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.CreateRoleRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.CreateRoleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/UpdateRole',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateRoleRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.UpdateRoleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/DeleteRole',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.DeleteRoleRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.DeleteRoleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListEffectivePermissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/ListEffectivePermissions',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListEffectivePermissionsRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListEffectivePermissionsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListUserRoles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/ListUserRoles',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListUserRolesRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.ListUserRolesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AssignUserRoles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/qdrant.cloud.iam.v1.IAMService/AssignUserRoles',
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.AssignUserRolesRequest.SerializeToString,
            qdrant_dot_cloud_dot_iam_dot_v1_dot_iam__pb2.AssignUserRolesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
