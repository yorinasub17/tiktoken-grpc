# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service/v1/tiktoken.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19service/v1/tiktoken.proto\x12\x0btiktoken.v1\"X\n\x10NumTokensRequest\x12\x11\n\x07\x62y_name\x18\x01 \x01(\tH\x00\x12\x17\n\rby_model_name\x18\x02 \x01(\tH\x00\x12\x0c\n\x04text\x18\x03 \x01(\tB\n\n\x08\x65ncoding\"\"\n\x11NumTokensResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x32_\n\x0fTiktokenService\x12L\n\tNumTokens\x12\x1d.tiktoken.v1.NumTokensRequest\x1a\x1e.tiktoken.v1.NumTokensResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.v1.tiktoken_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NUMTOKENSREQUEST._serialized_start=42
  _NUMTOKENSREQUEST._serialized_end=130
  _NUMTOKENSRESPONSE._serialized_start=132
  _NUMTOKENSRESPONSE._serialized_end=166
  _TIKTOKENSERVICE._serialized_start=168
  _TIKTOKENSERVICE._serialized_end=263
# @@protoc_insertion_point(module_scope)
