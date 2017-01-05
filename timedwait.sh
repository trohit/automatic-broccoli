#!/bin/bash
# checks for the existence of a non empty file 
# $FILE : file to wait for
# $TIMEOUT : seconds before timing out.
#set -x
timed_wait()
{
    FILE=$1
    TIMEOUT=$2
    echo waiting on $FILE for $TIMEOUT seconds
    COUNT=0
    until [ $COUNT -eq $TIMEOUT ];
    do
        if [ -s $FILE ]
        then
            echo Waiting $COUNT
            sleep 0.5
            (( COUNT++ ))
        else
            echo Quitting
            exit 0
        fi
    done
    echo done
}
timed_wait ~/.process_pid_file  10
