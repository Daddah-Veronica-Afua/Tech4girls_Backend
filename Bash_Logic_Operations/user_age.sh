#!/bin/bash
 echo "Please enter age"
read age
 if [ $age -lt 18 ]; then 
  echo "You are a minor."
 elif [ $age -ge 18 ] && [ $age -le 64 ]; then
   echo "You are an adult."
 else 
   echo "You are a senior."
fi