#!/bin/bash
WLAN_IFACE=${1:-wlan0}
echo -e "[ $WLAN_IFACE ]"
ifconfig $WLAN_IFACE down
if [ $? -eq 0 ]; then
	iwconfig $WLAN_IFACE mode managed 
	ifconfig $WLAN_IFACE up
	echo -e "$WLAN_IFACE brought up on mode managed"
else
	echo -e "$WLAN_IFACE does not exist, or does not support monitor mode, run 'iw list' to determine if your interface supports monitor mode"
	exit 1
fi

