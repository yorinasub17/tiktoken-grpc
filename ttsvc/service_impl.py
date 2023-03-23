from typing import List, Coroutine
import logging

import tiktoken
import grpc
from .service.v1 import tiktoken_pb2
from .service.v1 import tiktoken_pb2_grpc

# Coroutines to be invoked when the event loop is shutting down.
cleanup_coroutines: List[Coroutine] = []


class TiktokenService(tiktoken_pb2_grpc.TiktokenServiceServicer):
    async def NumTokens(
                self, request: tiktoken_pb2.NumTokensRequest, context: grpc.aio.ServicerContext,
            ) -> tiktoken_pb2.NumTokensResponse:
        field = request.WhichOneof('encoding')
        fv = getattr(request, request.WhichOneof('encoding'))
        if field == 'by_model_name':
            encoding = tiktoken.encoding_for_model(fv)
        else:
            encoding = tiktoken.get_encoding(fv)
        num_tokens = len(encoding.encode(request.text))
        return tiktoken_pb2.NumTokensResponse(count=num_tokens)


async def serve() -> None:
    server = grpc.aio.server()
    tiktoken_pb2_grpc.add_TiktokenServiceServicer_to_server(TiktokenService(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()

    async def server_graceful_shutdown():
        logging.info("Starting graceful shutdown...")
        # Shuts down the server with 5 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(5)

    cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()
