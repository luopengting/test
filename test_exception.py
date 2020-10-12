from google.protobuf.message import DecodeError
try:
    raise UnicodeDecodeError("", b'', 10, 1, "11")
except Exception as e:
    print(e)
