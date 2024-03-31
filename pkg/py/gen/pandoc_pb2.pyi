from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConvertTextRequest(_message.Message):
    __slots__ = ("Source", "From", "To")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    Source: str
    From: str
    To: str
    def __init__(self, Source: _Optional[str] = ..., From: _Optional[str] = ..., To: _Optional[str] = ...) -> None: ...

class ConvertTextResponse(_message.Message):
    __slots__ = ("Message", "Result")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    Message: str
    Result: str
    def __init__(self, Message: _Optional[str] = ..., Result: _Optional[str] = ...) -> None: ...
