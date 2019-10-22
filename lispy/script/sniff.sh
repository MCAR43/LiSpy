#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
_postScript="/home/lispy/data/lispy/script/filter.py"
_outFile="/home/lispy/data/lispy/script/pcap.dat"
_cmd=( tshark -S -l -n -i wlan0mon -Y 'wlan.fc.type_subtype eq 4' -T fields -e "wlan.ta" -e "wlan_radio.signal_dbm" -e "frame.time_epoch" -E separator="\$" -a duration:30 )
_post=( /home/lispy/data/lispy/script/./filter.py )
if [ ! -f "$_postScript" ]; then
  echo "$_postScript does not Exist"
  exit 999
fi
if [ "$1" == "" ]; then
  echo "Please supply a valid interface to sniff on"
fi
#main
sudo /bin/monstart
for (( ; ; ))
do
	echo "Beginnung Packet Capture"
	"${_cmd[@]}" > $_outFile
	echo "Finished Packet Capture"
	echo "Posting to Server"
	"${_post[@]}"
done
