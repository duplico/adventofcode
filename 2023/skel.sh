#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit
fi

day=$1

mkdir $day

touch $day/input.txt
touch $day/sample_input.txt
cp skel.py $day/advent.py
