import math
import os
import sys
import random

n=int(input())

'''if n%2 == 0:
  print('not weird')
  if n in range(6,21):
     print('weird')
else:
  print('weird') '''

if n%2 == 0 and n in range(2,6):
  print('not weird')
elif n%2 == 0 and n in range(6,21):
  print('weird')
elif n%2 == 0 and n > 20:
  print('not weird')
else:
  print('weird')