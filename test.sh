#!/bin/sh

UNAME=$(uname)

if [ "$UNAME" == "Darwin" ] ; then
	python3.14 -m unittest discover -s src
else
	python3 -m unittest discover -s src
fi
