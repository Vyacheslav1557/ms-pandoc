import grpc

from pkg.py.gen import pandoc_pb2
from pkg.py.gen import pandoc_pb2_grpc
from ..services import Pandoc


class PandocService(pandoc_pb2_grpc.PandocServiceServicer):
    def __init__(self) -> None:
        super().__init__()

    async def ConvertText(
            self,
            request: pandoc_pb2.ConvertTextRequest,
            context: grpc.ServicerContext
    ) -> pandoc_pb2.ConvertTextResponse:
        if request.To != "html":
            return pandoc_pb2.ConvertTextResponse(Message="not implemented")
        if request.From != "latex":
            return pandoc_pb2.ConvertTextResponse(Message="not implemented")
        return pandoc_pb2.ConvertTextResponse(
            Result=Pandoc.convert_text(
                source=request.Source, frm=request.From, to=request.To)
        )
