#!/bin/sh

# This bash script has been deprecated, the python version of date_range should
# be used instead

date1=$1
date2=$2

# Set second values based on the length of the dates given
if [[ ${#date1} == 6 && ${#date2} == 6 ]]
then
	date1_secs=`date +%s -d "${date1}01"`
	date2_secs=`date +%s -d "${date2}01"`
	time=month;
elif [[ ${#date1} == 8 && ${#date2} == 8 ]]
then
	date1_secs=`date +%s -d "${date1}"`
	date2_secs=`date +%s -d "${date2}"`
	time=day;
else
	exit 1;
fi

# While loop to print out the given date range
while [ "$date1_secs" -le "$date2_secs" ]
do
	echo $date1
	if [[ $time == "month" ]]
	then
		date1=`date +%Y%m -d "${date1}01 1 ${time}"`
		date1_secs=`date +%s -d "${date1}01"`
	elif [[ $time == "day" ]]
	then
		date1=`date +%Y%m%d -d "${date1} 1 ${time}"`
		date1_secs=`date +%s -d "${date1}"`
	fi
done

