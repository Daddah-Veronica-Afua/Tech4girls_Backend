#!/bin/bash
echo "Enter two number"
read number1
read number2

if ! [ $number1 -gt 10 ] && [ $number2 -gt 10 ];
then
echo "Both numbers are greater than 10."
elif [ $number1 -gt 10 ] || [ $number2 -gt 10 ];
then
echo "At least one number is greater than 10."
else
echo "Neither number is greater than 10."
fi