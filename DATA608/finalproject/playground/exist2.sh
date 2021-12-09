#!/bin/bash


for i in `cat goodzips2.txt`
do

#  echo "files2/"$i".html"
if grep -Fq "%" "files2/"$i".html"
then
    echo $i","$(grep -m1 "%" "files2/"$i".html") >> poverty2.csv
else
    echo $i", 0" >> poverty2.csv
fi

done
