# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='schema.proto',
  package='zs_classification',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cschema.proto\x12\x11zs_classification\"+\n\x0bScoredLabel\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\"@\n\x0f\x43lassifyRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x11\n\tthreshold\x18\x02 \x01(\x02\x12\x0c\n\x04topk\x18\x03 \x01(\x02\"X\n\x10\x43lassifyResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\x35\n\rscored_labels\x18\x02 \x03(\x0b\x32\x1e.zs_classification.ScoredLabel\"5\n\x0f\x41\x64\x64LabelRequest\x12\r\n\x05label\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"!\n\x10\x41\x64\x64LabelResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\"#\n\x12RemoveLabelRequest\x12\r\n\x05label\x18\x01 \x01(\t\"$\n\x13RemoveLabelResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\"\x0e\n\x0cResetRequest\"\x1e\n\rResetResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\tb\x06proto3')
)




_SCOREDLABEL = _descriptor.Descriptor(
  name='ScoredLabel',
  full_name='zs_classification.ScoredLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='zs_classification.ScoredLabel.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='zs_classification.ScoredLabel.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=78,
)


_CLASSIFYREQUEST = _descriptor.Descriptor(
  name='ClassifyRequest',
  full_name='zs_classification.ClassifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='zs_classification.ClassifyRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='zs_classification.ClassifyRequest.threshold', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topk', full_name='zs_classification.ClassifyRequest.topk', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=144,
)


_CLASSIFYRESPONSE = _descriptor.Descriptor(
  name='ClassifyResponse',
  full_name='zs_classification.ClassifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='zs_classification.ClassifyResponse.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scored_labels', full_name='zs_classification.ClassifyResponse.scored_labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=234,
)


_ADDLABELREQUEST = _descriptor.Descriptor(
  name='AddLabelRequest',
  full_name='zs_classification.AddLabelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='zs_classification.AddLabelRequest.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='zs_classification.AddLabelRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=289,
)


_ADDLABELRESPONSE = _descriptor.Descriptor(
  name='AddLabelResponse',
  full_name='zs_classification.AddLabelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='zs_classification.AddLabelResponse.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=324,
)


_REMOVELABELREQUEST = _descriptor.Descriptor(
  name='RemoveLabelRequest',
  full_name='zs_classification.RemoveLabelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='zs_classification.RemoveLabelRequest.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=361,
)


_REMOVELABELRESPONSE = _descriptor.Descriptor(
  name='RemoveLabelResponse',
  full_name='zs_classification.RemoveLabelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='zs_classification.RemoveLabelResponse.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=363,
  serialized_end=399,
)


_RESETREQUEST = _descriptor.Descriptor(
  name='ResetRequest',
  full_name='zs_classification.ResetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=401,
  serialized_end=415,
)


_RESETRESPONSE = _descriptor.Descriptor(
  name='ResetResponse',
  full_name='zs_classification.ResetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='zs_classification.ResetResponse.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=447,
)

_CLASSIFYRESPONSE.fields_by_name['scored_labels'].message_type = _SCOREDLABEL
DESCRIPTOR.message_types_by_name['ScoredLabel'] = _SCOREDLABEL
DESCRIPTOR.message_types_by_name['ClassifyRequest'] = _CLASSIFYREQUEST
DESCRIPTOR.message_types_by_name['ClassifyResponse'] = _CLASSIFYRESPONSE
DESCRIPTOR.message_types_by_name['AddLabelRequest'] = _ADDLABELREQUEST
DESCRIPTOR.message_types_by_name['AddLabelResponse'] = _ADDLABELRESPONSE
DESCRIPTOR.message_types_by_name['RemoveLabelRequest'] = _REMOVELABELREQUEST
DESCRIPTOR.message_types_by_name['RemoveLabelResponse'] = _REMOVELABELRESPONSE
DESCRIPTOR.message_types_by_name['ResetRequest'] = _RESETREQUEST
DESCRIPTOR.message_types_by_name['ResetResponse'] = _RESETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScoredLabel = _reflection.GeneratedProtocolMessageType('ScoredLabel', (_message.Message,), dict(
  DESCRIPTOR = _SCOREDLABEL,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:zs_classification.ScoredLabel)
  ))
_sym_db.RegisterMessage(ScoredLabel)

ClassifyRequest = _reflection.GeneratedProtocolMessageType('ClassifyRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFYREQUEST,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:zs_classification.ClassifyRequest)
  ))
_sym_db.RegisterMessage(ClassifyRequest)

ClassifyResponse = _reflection.GeneratedProtocolMessageType('ClassifyResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFYRESPONSE,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:zs_classification.ClassifyResponse)
  ))
_sym_db.RegisterMessage(ClassifyResponse)

AddLabelRequest = _reflection.GeneratedProtocolMessageType('AddLabelRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDLABELREQUEST,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:zs_classification.AddLabelRequest)
  ))
_sym_db.RegisterMessage(AddLabelRequest)

AddLabelResponse = _reflection.GeneratedProtocolMessageType('AddLabelResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDLABELRESPONSE,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:zs_classification.AddLabelResponse)
  ))
_sym_db.RegisterMessage(AddLabelResponse)

RemoveLabelRequest = _reflection.GeneratedProtocolMessageType('RemoveLabelRequest', (_message.Message,), dict(
  DESCRIPTOR = _REMOVELABELREQUEST,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:zs_classification.RemoveLabelRequest)
  ))
_sym_db.RegisterMessage(RemoveLabelRequest)

RemoveLabelResponse = _reflection.GeneratedProtocolMessageType('RemoveLabelResponse', (_message.Message,), dict(
  DESCRIPTOR = _REMOVELABELRESPONSE,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:zs_classification.RemoveLabelResponse)
  ))
_sym_db.RegisterMessage(RemoveLabelResponse)

ResetRequest = _reflection.GeneratedProtocolMessageType('ResetRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESETREQUEST,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:zs_classification.ResetRequest)
  ))
_sym_db.RegisterMessage(ResetRequest)

ResetResponse = _reflection.GeneratedProtocolMessageType('ResetResponse', (_message.Message,), dict(
  DESCRIPTOR = _RESETRESPONSE,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:zs_classification.ResetResponse)
  ))
_sym_db.RegisterMessage(ResetResponse)


# @@protoc_insertion_point(module_scope)
