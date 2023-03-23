import unittest
from dataclasses import dataclass

import mock
import grpc
from ddt import ddt, data

from ttsvc import TiktokenService
from ttsvc.pb2.tiktoken.v1 import tiktoken_pb2

@dataclass
class TestData:
    encoding: str
    text: str
    expected: int


def annotated(test_name: str, encoding: str, name: str, expected: int):
    r = TestData(encoding, name, expected)
    setattr(r, '__name__', test_name)
    return r


@ddt
class TestCase(unittest.IsolatedAsyncioTestCase):

    def __init__(self, methodName) -> None:
        super().__init__(methodName)

        self.service = TiktokenService()
        self.mock_context = mock.create_autospec(spec=grpc.aio.ServicerContext)

    @data(annotated("num_tokens_cl100k_simple", "cl100k_base", "tiktoken is great!", 6),
          annotated("num_tokens_gpt2_word_with_many_tokens", "gpt2", "antidisestablishmentarianism", 5),
          annotated("num_tokens_p50k_word_with_many_tokens", "p50k_base", "antidisestablishmentarianism", 5),
          annotated("num_tokens_cl100k_word_with_many_tokens", "cl100k_base", "antidisestablishmentarianism", 6),
          annotated("num_tokens_gpt2_japanese", "gpt2", "お誕生日おめでとう", 14),
          annotated("num_tokens_p50k_japanese", "p50k_base", "お誕生日おめでとう", 14),
          annotated("num_tokens_cl100k_japanese", "cl100k_base", "お誕生日おめでとう", 9),
         )
    async def test_num_tokens(self, data):
        request = tiktoken_pb2.NumTokensRequest(
            by_name=data.encoding,
            text=data.text,
        )
        response = await self.service.NumTokens(request, self.mock_context)
        self.assertEqual(
            response.count, data.expected,
            f'Tiktoken service returned unexpected count for encoding {data.encoding} and text "{data.text}"',
        )

    @data(annotated("num_tokens_davinci", "text-davinci-003", "antidisestablishmentarianism", 5),
          annotated("num_tokens_turbo", "gpt-3.5-turbo", "antidisestablishmentarianism", 6),
         )
    async def test_num_tokens_by_model(self, data):
        request = tiktoken_pb2.NumTokensRequest(
            by_model_name=data.encoding,
            text=data.text,
        )
        response = await self.service.NumTokens(request, self.mock_context)
        self.assertEqual(
            response.count, data.expected,
            f'Tiktoken service returned unexpected count for model {data.encoding} and text "{data.text}"',
        )


if __name__ == '__main__':
    unittest.main()
