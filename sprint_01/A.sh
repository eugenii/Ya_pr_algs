#!/bin/bash

echo "=== test A ==="
echo "-8 -5 -2 7" > test_A.txt 
test_A() {
    echo $result=$(python A.py < test_A.txt)
    echo $result
}