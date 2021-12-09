#!/bin/bash

for i in `cat zip.txt`
do
  echo "wget --output-document=files/"$i".html --no-check-certificate https://censusreporter.org/profiles/86000US"$i"-"$i"; sleep 5"
done
