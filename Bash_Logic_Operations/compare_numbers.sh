#!/bin/bash
echo "Enter two numbers"
read number1
read number2

if [ $number1 -gt $number2 ]; then
echo "$number1 is greater than $number2."
elif [ $number1 -lt $number2]; then
echo "$number1 is less than $number2."
else
echo "$number1 and $number2 are equal."
fi