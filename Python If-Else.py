import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1 or n<21 and n>5:
        print("Weird")
    else:
        print("Not Weird")
