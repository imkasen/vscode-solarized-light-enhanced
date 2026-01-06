#!/bin/bash

# demo.sh - Shell script syntax showcase

# Variables
name="John Doe"
age=30

# String manipulation
greeting="Hello, $name!"
echo "$greeting"
echo "Your name is ${name} and your age is ${age}."

# Arithmetic operations
a=1
b=2
result=$((a + b))
echo "Result of addition: $result"

# Command substitution
current_date=$(date)
echo "Current date: $current_date"

# Conditional statements
if [ $a -gt $b ]; then
  echo "a is greater than b"
elif [ $a -lt $b ]; then
  echo "a is less than b"
else
  echo "a is equal to b"
fi

# Loops
for i in {1..5}; do
  echo "$i"
done

j=0
while [ $j -lt 5 ]; do
  echo $j
  j=$((j + 1))
done

# Case statement
case $name in
  "John Doe")
    echo "Your name is John Doe"
    ;;
  "Jane Doe")
    echo "Your name is Jane Doe"
    ;;
  *)
    echo "Your name is unknown"
    ;;
esac

# Functions
greet() {
  local name=$1
  echo "Hello, $name!"
}

greet "John"

# Arrays
fruits=("apple" "banana" "orange")
echo "First fruit: ${fruits[0]}"
echo "All fruits: ${fruits[*]}"

# Input/Output
read -rp "Enter your name: " user_name
echo "Hello, $user_name!"

# File operations
if [ -f "myfile.txt" ]; then
  echo "File exists"
else
  echo "File does not exist"
fi

# Redirection
ls -l > file_list.txt
wc -l < file_list.txt

# Piping
echo "Hello, World!" | grep "World"

# Here document
cat << EOF > myfile.txt
This is some text.
This is another line.
EOF

# Process management
sleep 5 &
process_id=$!
echo "Process ID: $process_id"

# Signals
kill -s SIGINT $process_id

# Exit status
exit 0
