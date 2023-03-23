import unittest

import mock
import grpc
from ddt import ddt, data

from ttsvc import TiktokenService
from ttsvc.service.v1 import tiktoken_pb2

@ddt
class TestCase(unittest.IsolatedAsyncioTestCase):

    def __init__(self, methodName) -> None:
        super().__init__(methodName)

        self.service = TiktokenService()
        self.mock_context = mock.create_autospec(spec=grpc.aio.ServicerContext)

    @data(("cl100k_base", "tiktoken is great!", 6),
          ("gpt2", "antidisestablishmentarianism", 5),
          ("p50k_base", "antidisestablishmentarianism", 5),
          ("cl100k_base", "antidisestablishmentarianism", 6),
          ("gpt2", "お誕生日おめでとう", 14),
          ("p50k_base", "お誕生日おめでとう", 14),
          ("cl100k_base", "お誕生日おめでとう", 9),
         )
    async def test_num_tokens(self, data):
        encoding, text, expected = data
        request = tiktoken_pb2.NumTokensRequest(
            by_name=encoding,
            text=text,
        )
        response = await self.service.NumTokens(request, self.mock_context)
        self.assertEqual(
            response.count, expected,
            f'Tiktoken service returned unexpected count for encoding {encoding} and text "{text}"',
        )

    @data(("text-davinci-003", "antidisestablishmentarianism", 5),
          ("gpt-3.5-turbo", "antidisestablishmentarianism", 6),
         )
    async def test_num_tokens_by_model(self, data):
        model, text, expected = data
        request = tiktoken_pb2.NumTokensRequest(
            by_model_name=model,
            text=text,
        )
        response = await self.service.NumTokens(request, self.mock_context)
        self.assertEqual(
            response.count, expected,
            f'Tiktoken service returned unexpected count for model {model} and text "{text}"',
        )


if __name__ == '__main__':
    unittest.main()
