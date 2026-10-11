"""Build/inspect EastWest Opus plugin state (as REAPER's vst_chunk base64)."""
import base64, gzip, json, zlib, io, struct

TEMPLATE = "AAEAAAEAAAABAAAAFAAAAAIAAAAAAAAA/////x+LCAAAAAAABBNFTkEKwjAQ/Mueg7TiKeeCCKLexUMMW4km2bLZeLD0726p2NvszOzMjOCjKwUsXJB74uSyRzCQXUIlFTkv4a1YuKKBWpCP5F9gexeLEpG8E+LFK5gGAttum01jQMqpJuRF3s13h5lSyAvTGvhQRu2+3gw8mOow4/G/6JCLlibMsp/FdVWHvatRYNK/PkRB/oUUz2EQsGvG+f5Er87pCwUxIVXpAAAAAAAAAAAAAABKVUNFUHJpdmF0ZURhdGEAAQFCeXBhc3MAAQEDAB0AAAAAAAAASlVDRVByaXZhdGVEYXRhAAAAAAAAAAA="
HDR = 28

def split(b64):
    b = base64.b64decode(b64)
    d = zlib.decompressobj(31)
    js = d.decompress(b[HDR:])
    return b[:HDR], json.loads(js), d.unused_data

def build(perf, b64=TEMPLATE):
    head, _, tail = split(b64)
    gz = gzip.compress(json.dumps(perf, separators=(",", ":")).encode(), compresslevel=6, mtime=0)
    blob = head + gz + tail
    # first u32 = total blob length minus 16 (observed in Opus-written states)
    blob = struct.pack("<I", len(blob) - 16) + blob[4:]
    return base64.b64encode(blob).decode()

def load_oib(path):
    b = open(path, "rb").read()
    return json.loads(zlib.decompressobj(31).decompress(b[20:]))
