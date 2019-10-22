# Data Repository
Various scripts to develop and run the project

## Data Folder /data

For development and testing

### gen_blob.py
Generates `fakedata_blob.json` with pings of mac, rssi, and timestamp

### post_blob.py
Uses `gen_blob.py` to send random pings to http://localhost/data

### post_blob_specific.py
More predidable version of `post_blob.py`, sends pings from a device to many Pis (for triangulation)


## Script Folder /script

### startup.sh
Takes the local IP and POSTs it to http://localhost/ip

## Sniffer Folder /sniffer

### sniff.sh
Handles tshark to probe data and invokes `filter.py`

### filter.py
Filters ping data and POSTs to the VPS

## Test Folder /test

### test_mysql.py
Example on how to use MySQL and Python.

## Old - Git History

### tunnel_redis.sh
This tunnels into the VPS so Redis may be accessed on your local machine. Run the script and type the password (given), then leave the window open.

### redis_broadcaster.py
Simulates outgoing Pi traffic by broadcasting data from `fakedata.json` to the Redis "feed" channel every few seconds.

### redis_receiver.py
Listens to the Redis "feed" channel and stores received data into Redis memory. The device's ID is used as the hash key and the x, y, z, and timestamp are stored as values. The record TTL is set for 5 minutes, we assume the device is no longer active after that. Otherwise, the device's data is updated in Redis every time it pings.

![data](https://i.imgur.com/sqv1tsQ.png)

### redis_filter.py
Scrapes the device data from Redis. Currently, there are methods to count devices in radius and to plot devices on a graph. This will soon cache history and location amounts to MySQL.
