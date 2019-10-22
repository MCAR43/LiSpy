#!/usr/bin/env python3
import json
import zlib
import requests
from hashlib import md5
from config import auth

headers = { "content-encoding": "gzip", "content-type": "application/json" }

def gzip_encode(content):
    content = json.dumps(content).encode('utf-8')
    gzip_compress = zlib.compressobj(9, zlib.DEFLATED, zlib.MAX_WBITS | 16)
    data = gzip_compress.compress(content) + gzip_compress.flush()
    return data

def postData(endpoint, data):
    id, tok = auth
    send = {"uuid": id, "token": tok, **data}
    r = requests.post('https://studytime.live/' + endpoint, data=gzip_encode(send), headers=headers)
    print(r.text)
