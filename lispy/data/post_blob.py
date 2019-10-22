import requests
import json
import zlib
import sys
import random
from gen_blob import pings

uuids = {'217ca3ec-73a5-4da4-8f05-b4bd84e535ec': '9u3aLupvFCthfQX6BqcLqwqsSpEpSSmMeuU4', '6e74a71f-dc3f-4428-8a08-f5a6d231eef7': '0b06ac6b251aff595d89d796ad916ccad21b', 'b163b43e-f95d-4c59-91f7-08499b081ae7': 'Ugr67J9aHjB9DWB6rJLJstE8nWDNxrEwSKwH'}

# Ref: https://github.com/ksmith97/GzipSimpleHTTPServer/blob/master/GzipSimpleHTTPServer.py#L65
def gzip_encode(content):
    content = json.dumps(content).encode('utf-8')
    gzip_compress = zlib.compressobj(9, zlib.DEFLATED, zlib.MAX_WBITS | 16)
    data = gzip_compress.compress(content) + gzip_compress.flush()
    return data

# Amount
amount = 3
if len(sys.argv) > 1:
    amount = int(sys.argv[1])

for _ in range(12):
    # Generate
    data = pings(amount)

    # Data
    uuid, token = random.choice(list(uuids.items()))
    data = { "uuid": uuid, "token": token, "blob": data }
    if amount <= 20:
        print(data) # dict

    # Compression
    headers = { "content-encoding": "gzip", "content-type": "application/json" }
    r = requests.post('http://localhost/data', data=gzip_encode(data), headers=headers)

    # No compression
    #r = requests.post('http://localhost/data', data=data)

    # Output response
    print(r.text)