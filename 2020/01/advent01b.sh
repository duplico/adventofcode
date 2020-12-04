#!/usr/bin/env bash

# lol, this is a performance disaster
while read i; do
  while read j; do
     while read k; do
          let tot=$i+$j+$k
          if [ $tot -eq 2020 ]; then
               let product=$i*$j*$k
               echo "$i x $j x $k = $product"
               exit 0
          fi
     done <$1
  done <$1
done <$1
