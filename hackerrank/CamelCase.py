import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
