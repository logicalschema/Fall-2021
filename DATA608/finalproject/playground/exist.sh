#!/bin/bash


for i in `cat goodzips.txt`
do

#  echo "files/"$i".html"
if grep -Fq "%" "files/"$i".html"
then
    echo $i","$(grep -m1 "%" "files/"$i".html") >> poverty.csv
else
    echo $i", 0" >> poverty.csv
fi

done
