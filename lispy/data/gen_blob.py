import gzip
import random
import time
import json

macs = ['61-01-69-19-28-67',
'42-24-22-72-92-72',
'50-46-42-48-33-36',
'25-67-96-14-92-42',
#'81-97-59-93-50-74',
#'82-04-61-13-75-38',
#'06-19-77-22-61-95',
#'77-09-90-25-08-44',
#'72-85-91-06-50-40',
#'77-96-40-84-60-16',
'68-39-02-42-45-94',
'75-40-67-45-89-56',
'47-58-15-68-74-92',
'78-72-85-63-53-76']

def mac():
    return macs[random.randint(0,len(macs)-1)]

def mac0():
    mac = ""
    for i in range(12):
        if (i > 0 and i % 2 == 0):
            mac += "-"
        mac += str(random.randint(0,9))
    return mac

def ping():
    return { "device": mac(), "rssi": random.randint(40,60), "time": int(time.time()) - random.randint(40,60) }

def pings(amount):
    pings = []
    for i in range(amount):
        pings.append(ping())
    return pings

if __name__ == '__main__':
    with open('fakedata_blob.json', 'w') as f:
        json.dump(pings(5000), f)