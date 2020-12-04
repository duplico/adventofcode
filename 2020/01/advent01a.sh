#!/usr/bin/env bash

# god, this is a disaster, performance-wise...
while read i; do
  while read j; do
     let tot=$i+$j
     if [ $tot -eq 2020 ]; then
          let product=$i*$j
          echo "$i x $j = $product"
          exit 0
     fi
  done <$1
done <$1
