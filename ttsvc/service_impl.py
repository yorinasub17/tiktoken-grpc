from typing import List, Coroutine, Optional
from dataclasses import dataclass
import logging

import tiktoken
import grpc.aio
from .pb2.tiktoken.v1 import tiktoken_pb2
from .pb2.tiktoken.v1 import tiktoken_pb2_grpc

# Coroutines to be invoked when the event loop is shutting down.
__cleanup_coroutines: List[Coroutine] = []


class TiktokenService(tiktoken_pb2_grpc.TiktokenServiceServicer):
    async def NumTokens(
        self,
        request: tiktoken_pb2.NumTokensRequest,
        context: grpc.aio.ServicerContext,
    ) -> tiktoken_pb2.NumTokensResponse:
        """
        Use the tiktoken library to return the number of tokens in the given text based on the requested encoding.

        The encoding can be determined by either the model name (if by_model_name is set on the request) or directly by
        the encoding name (if by_name is set on the requst).
        """
        field = request.WhichOneof("encoding")
        fv = getattr(request, request.WhichOneof("encoding"))
        if field == "by_model_name":
            encoding = tiktoken.encoding_for_model(fv)
        elif field == "by_name":
            encoding = tiktoken.get_encoding(fv)
        else:
            raise Exception(f"Unknown encoding field {field}")
        num_tokens = len(encoding.encode(request.text))
        return tiktoken_pb2.NumTokensResponse(count=num_tokens)


@dataclass
class TLSOpts:
    # Contents of the TLS certificate file.
    cert: bytes
    # Contents of the TLS private key file.
    private_key: bytes
    # Contents of the TLS CA cert file.
    cacert: Optional[bytes]
    # Whether client authentication is required. When true, cacert must not be None.
    require_client_auth: bool


@dataclass
class ServerOpts:
    # The port that the server listens on.
    port: int
    # The number of seconds that the server should gracefully wait during a shutdown event.
    shutdown_timeout_seconds: int
    # Options for setting up TLS authentication. Set to None if you do not wish to start the server with TLS auth.
    tls_opts: Optional[TLSOpts]


async def serve(opts: ServerOpts) -> None:
    """
    Main entrypoint for the tiktoken grpc service. This will start the grpc server, listening on the port specified in
    the server opts.
    """
    listen_addr = f"[::]:{opts.port}"

    server = grpc.aio.server()
    tiktoken_pb2_grpc.add_TiktokenServiceServicer_to_server(TiktokenService(), server)

    if opts.tls_opts is None:
        server.add_insecure_port(listen_addr)
    else:
        server_credentials = grpc.ssl_server_credentials(
            [(opts.tls_opts.private_key, opts.tls_opts.cert)],
            opts.tls_opts.cacert,
            opts.tls_opts.require_client_auth,
        )
        server.add_secure_port(listen_addr, server_credentials)

    logging.info("Starting server on %s", listen_addr)
    await server.start()

    async def server_graceful_shutdown():
        """
        Shuts down the server with configured seconds of grace period. During the grace period, the server won't accept
        new connections and allow existing RPCs to continue within the grace period.
        """
        logging.info("Starting graceful shutdown...")
        await server.stop(opts.shutdown_timeout_seconds)

    __cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()


def cleanup(loop) -> None:
    """
    Clean up the server event loop by waiting for the server to gracefully shutdown.
    """
    loop.run_until_complete(*__cleanup_coroutines)
