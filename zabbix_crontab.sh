#!/bin/bash

# function check and example ip and host! not of me
function checkAndSend() {
	var=`cksum $1`
	var=`echo $var | awk '{print $1;}'`
	zabbix_sender -z 172.16.11.215 -p 10051 -s "www.naixo.com" -k change-file-[$1] -o $var
}

input="list_file.txt"
while IFS= read -r line
do
	echo "$line"
	checkAndSend $line
done < "$input"

