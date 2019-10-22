#!/usr/bin/env python3
from hashlib import md5
from util import postData
TSHARK_INFILE = "/home/lispy/data/lispy/script/pcap.dat"
TESTING_MACS = [
    "69:69:69:69:69:69",
    "b4:f1:da:b3:d1:00",
    "08:c5:e1:73:21:45"
]
class Device:
    def __init__(self, hashID, rssi, time):
        self.id = hashID
        self.rssi = rssi
        self.time = time


def getReq():
    hashes = {}
    probes = []
    with open(TSHARK_INFILE, 'r') as f:
        for line in f.readlines():
            line = line.split('$')
            _id, _rssi, _epoch = line
            if _id not in TESTING_MACS:
                _id = md5((_id + "ripRainbowTable").encode()).hexdigest()
            if _id not in hashes.keys():
                hashes[_id] = Device(_id, _rssi, _epoch)
            else:
                hashes[_id].rssi = _rssi
                hashes[_id].time = _epoch
    for key in hashes.keys():
        probes.append({"device":hashes[key].id, "rssi":hashes[key].rssi, "time":hashes[key].time.split('.')[0]})
    return probes

def main():
    postData('data', { "blob": getReq() })

if __name__ == "__main__":
    main()

