#!/bin/bash
CNT=0
while true;do
	if [ ${CNT} -lt "100" ];then
		python ./socketclient.py >> ./client.log
		CNT=$((CNT+1))
		echo "${CNT}"
	else
		echo "Finish iteration"
		exit 	
	fi
done
