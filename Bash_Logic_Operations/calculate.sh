#!/bin/bash
echo "Enter three numbers"
read number1
read number2
read number3
  
  sum=$(( $number1 + $number2 ))
  product=$(( sum * $number3))

  echo "The sum of $number1 and $number2 is:$sum"
  echo "The product of the sum by $number3 gives:$product"