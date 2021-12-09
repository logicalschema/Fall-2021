#!/bin/bash


for i in `cat zip.txt` 
do
if grep -Fxq $i badzips.txt
then 
  echo ""
else
  echo $i >> goodzips.txt 
fi



done
