import gzip
import random
import time
import json
import requests
import zlib
import sys
from gen_blob import pings

# This script posts 1 ping from 8 macs to 3 pis

uuids = {'217ca3ec-73a5-4da4-8f05-b4bd84e535ec': '9u3aLupvFCthfQX6BqcLqwqsSpEpSSmMeuU4', '6e74a71f-dc3f-4428-8a08-f5a6d231eef7': '0b06ac6b251aff595d89d796ad916ccad21b', 'b163b43e-f95d-4c59-91f7-08499b081ae7': 'Ugr67J9aHjB9DWB6rJLJstE8nWDNxrEwSKwH', 'd68761f6-7d91-4487-a4b2-45ee15ef74dc': '48177253719c3446d948a5050fc9e23e8bae'}

macs = ['61-01-69-19-28-67',
'42-24-22-72-92-72',
'50-46-42-48-33-36',
'25-67-96-14-92-42',
'68-39-02-42-45-94',
'75-40-67-45-89-56',
'47-58-15-68-74-92',
'78-72-85-63-53-76']

def ping(mac, epoc):
    return { "device": mac, "rssi": -random.randint(55,75), "time": int(epoc) }

def pings():
    pings = []
    amt = 0
    for mac in macs:
        amt += 1
        pings.append(ping(mac, int(time.time()) - random.randint(0,60)))
    return pings

# Ref: https://github.com/ksmith97/GzipSimpleHTTPServer/blob/master/GzipSimpleHTTPServer.py#L65
def gzip_encode(content):
    content = json.dumps(content).encode('utf-8')
    gzip_compress = zlib.compressobj(9, zlib.DEFLATED, zlib.MAX_WBITS | 16)
    data = gzip_compress.compress(content) + gzip_compress.flush()
    return data

for _ in range(4):
    for uuid, token in uuids.items():
        # Generate
        data = pings()

        # Data
        data = { "uuid": uuid, "token": token, "blob": data }
        print(data) # dict

        # Compression
        headers = { "content-encoding": "gzip", "content-type": "application/json" }
        r = requests.post('http://localhost/data', data=gzip_encode(data), headers=headers)

        # No compression
        #r = requests.post('http://localhost/data', data=data)

        # Output response
        print(r.text)
        
        time.sleep(.1)