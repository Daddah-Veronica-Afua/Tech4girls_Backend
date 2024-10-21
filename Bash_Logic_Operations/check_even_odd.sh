#!/bin/bash
echo "Enter number"
read number
if (( number % 2 == 0 )); then
    echo "The number $number is even."
else
    echo "The number $number is odd."
fi
