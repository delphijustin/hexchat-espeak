#!/bin/bash
ps -C espeak>/dev/null
export errorlevel=$?
while [ $errorlevel -eq 0 ]
do
ps -C espeak>/dev/null
export errorlevel=$?
done
espeak -f $1
rm $1
