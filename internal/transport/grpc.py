import grpc

from pkg.py.gen import service_pb2
from pkg.py.gen import service_pb2_grpc
from ..services import Service


class SampleService(service_pb2_grpc.SampleServiceServicer):
    def __init__(self) -> None:
        super().__init__()

    async def Hello(
            self,
            request: service_pb2.HelloRequest,
            context: grpc.ServicerContext
    ) -> service_pb2.HelloResponse:
        return service_pb2.HelloResponse(Greeting=Service.hello(request.Name))
