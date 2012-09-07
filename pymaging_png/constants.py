# -*- coding: utf-8 -*-
import struct
from pymaging.exceptions import PymagingException

# The PNG signature.
# http://www.w3.org/TR/PNG/#5PNG-file-signature
PNG_SIGNATURE = struct.pack('8B', 137, 80, 78, 71, 13, 10, 26, 10)
MAX_CHUNK_LENGTH = 2**31-1
VERIFY_CONSTANT = 2**32 - 1
ALLOWED_BIT_DEPTHS = [1, 2, 4, 8, 16]
ALLOWED_COLOR_TYPES = [0, 2, 3, 4, 6]


class PNGReaderError(PymagingException): pass
class NoChunkLength(PNGReaderError): pass
class NoChunkType(PNGReaderError): pass
class InvalidChunkLength(PNGReaderError): pass
class InvalidChunkType(PNGReaderError): pass
class ChunkError(PNGReaderError): pass
class Adam7Error(PNGReaderError): pass
