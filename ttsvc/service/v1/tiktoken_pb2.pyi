from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NumTokensRequest(_message.Message):
    __slots__ = ["by_model_name", "by_name", "text"]
    BY_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    BY_NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    by_model_name: str
    by_name: str
    text: str
    def __init__(self, by_name: _Optional[str] = ..., by_model_name: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class NumTokensResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...
