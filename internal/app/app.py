from abc import ABC, abstractmethod

import grpc.aio
from grpc_interceptor.exception_to_status import AsyncExceptionToStatusInterceptor

from pkg.py.gen import service_pb2_grpc
from ..config import Config
from ..logger import get_logger
from ..transport import SampleService, RequestLoggingInterceptor


class AbstractApp(ABC):
    @abstractmethod
    async def run(self) -> None:
        ...

    @abstractmethod
    async def stop(self) -> None:
        ...


class App(AbstractApp):
    def __init__(self):
        self.server = grpc.aio.server(
            interceptors=[AsyncExceptionToStatusInterceptor(), RequestLoggingInterceptor()]
        )
        service_pb2_grpc.add_SampleServiceServicer_to_server(
            SampleService(), self.server
        )
        address = f"{Config().HOST}:{Config().PORT}"
        logger = get_logger()
        logger.info(f"Listening on {address}")
        self.server.add_insecure_port(address)

    async def run(self) -> None:
        await self.server.start()
        await self.server.wait_for_termination()

    async def stop(self) -> None:
        logger = get_logger()
        logger.info("Shutting down in progress")
