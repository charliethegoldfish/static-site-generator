#!/bin/sh

UNAME=$(uname)

if [ "$UNAME" == "Darwin" ] ; then
	python3.14 src/main.py
	cd public && python3.14 -m http.server 8888
else
	python3 src/main.py
	cd public && python3 -m http.server 8888
fi