import logging
import asyncio

import ttsvc

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(ttsvc.serve())
    finally:
        loop.run_until_complete(*ttsvc.cleanup_coroutines)
        loop.close()
