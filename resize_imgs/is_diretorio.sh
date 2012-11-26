#!/bin/bash

path=$1

if [ -d $path ]; then 
	echo 1;
else
	echo 0;
fi



