#!/bin/bash


echo "Informe um numero:"
read num



if [ $num = "S" ] || [ $num = "s" ]; then
	echo "aceitou"
else
	echo "nao aceitou"
fi

if [ [$num in [0-9] ] ]; then
	echo "é um numero"
else
	echo "nao é um numero"
fi
