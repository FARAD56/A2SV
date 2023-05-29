#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2 != 0):
        print("Weird")
    else:
        if n >= 20 or 2 <= n <= 5:
            print("Not Weird")
        else:
            print("Weird") 