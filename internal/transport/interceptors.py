import time
from typing import Callable, Any

import grpc
from grpc_interceptor.server import AsyncServerInterceptor

from ..logger import get_logger


class RequestLoggingInterceptor(AsyncServerInterceptor):
    async def intercept(
            self,
            method: Callable,
            request: Any,
            context: grpc.ServicerContext,
            method_name: str,
    ) -> Any:
        start_time = time.time_ns()

        try:
            return await method(request, context)
        finally:
            request_time = time.time_ns() - start_time
            get_logger().info(
                f"{method_name} - {request_time / 1e6}ms"
            )
