from typing import Optional
import argparse
import logging
import asyncio

import ttsvc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='tiktoken-grpc',
        description='tiktoken-grpc is a gRPC service that wraps the tiktoken Python library offered by OpenAI.',
    )

    parser.add_argument(
        '-p', '--port', type=int, default=50051,
        help='The port number that the service should listen on.',
    )
    parser.add_argument(
        '--no-tls', action='store_true',
        help='When passed in, the server will be started in insecure mode without TLS configured.',
    )
    parser.add_argument(
        '--tls-cert', type=argparse.FileType('rb'),
        help='Path to a local file containing the TLS certificate to use. Required unless --no-tls is passed in.',
    )
    parser.add_argument(
        '--tls-key', type=argparse.FileType('rb'),
        help='Path to a local file containing the TLS private key to use. Required unless --no-tls is passed in.',
    )
    parser.add_argument(
        '--tls-cacert', type=argparse.FileType('rb'),
        help='Path to a local file containing the TLS root CA certificate to use. Required if --tls-require-client-auth is passed in.',
    )
    parser.add_argument(
        '--tls-require-client-auth', action='store_true',
        help='Whether to require client authentication for connections. When passed in, --tls-cacert must also be set.',
    )
    parser.add_argument(
        '--shutdown-timeout', type=int, default=15,
        help='The number of seconds to wait during graceful shutdown.',
    )

    return parser.parse_args()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    args = parse_args()

    tls_opts: Optional[ttsvc.TLSOpts] = None
    if not args.no_tls:
        cacert: Optional[bytes] = None
        if args.tls_cacert:
            cacert = args.tls_cacert.read()
        tls_opts = ttsvc.TLSOpts(
            cert=args.tls_cert.read(),
            private_key=args.tls_key.read(),
            cacert=cacert,
            require_client_auth=args.tls_require_client_auth,
        )
    opts = ttsvc.ServerOpts(
        port=args.port,
        tls_opts=tls_opts,
        shutdown_timeout_seconds=args.shutdown_timeout,
    )

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(ttsvc.serve(opts))
    finally:
        ttsvc.cleanup(loop)
        loop.close()
