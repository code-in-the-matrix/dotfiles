#!/bin/sh

project_dir="$HOME/Documents/oblivion"

x=$(shuf -i 1-7 -n 1)

if [ $x = 0 ]; then
  exit
fi

echo "" > $project_dir/main.txt

for i in $(seq 1 $x);
do
  ts=$(date +%s)
  echo "$ts" >> $project_dir/main.txt
  #echo "print('Hello world')" > $project_dir/hello.py
  
  git -C $project_dir add main.txt
  git -C $project_dir commit -m "feat: modified main file"
  #git -C $project_dir push origin main
done

git -C $project_dir push origin main




