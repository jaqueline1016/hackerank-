#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice_punteo = 0
    bob_punteo = 0
    resultado = []
    for i in range(len(a)):
        if a[i] > b[i]:
            alice_punteo +=1
        elif a[i] < b[i]:
            bob_punteo +=1
    resultado.append(alice_punteo)
    resultado.append(bob_punteo)
    return resultado

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
