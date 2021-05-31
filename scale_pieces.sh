#!/bin/bash

cd resources
for pic in $(ls)
do 
  echo $pic
  ffmpeg -i $pic -vf scale=52:52 "$pic.new.png" 
done
