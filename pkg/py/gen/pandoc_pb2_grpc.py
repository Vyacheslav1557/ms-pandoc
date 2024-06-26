# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pkg.py.gen.pandoc_pb2 as pandoc__pb2


class PandocServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConvertText = channel.unary_unary(
                '/pandoc.PandocService/ConvertText',
                request_serializer=pandoc__pb2.ConvertTextRequest.SerializeToString,
                response_deserializer=pandoc__pb2.ConvertTextResponse.FromString,
                )


class PandocServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ConvertText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PandocServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConvertText': grpc.unary_unary_rpc_method_handler(
                    servicer.ConvertText,
                    request_deserializer=pandoc__pb2.ConvertTextRequest.FromString,
                    response_serializer=pandoc__pb2.ConvertTextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pandoc.PandocService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PandocService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ConvertText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pandoc.PandocService/ConvertText',
            pandoc__pb2.ConvertTextRequest.SerializeToString,
            pandoc__pb2.ConvertTextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
