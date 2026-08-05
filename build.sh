#!/bin/sh

UNAME=$(uname)

if [ "$UNAME" == "Darwin" ] ; then
	python3.14 src/main.py "/static-site-generator/"
else
	python3 src/main.py "/static-site-generator/"
fi