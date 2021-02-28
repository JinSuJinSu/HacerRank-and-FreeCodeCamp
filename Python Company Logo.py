  #!/bin/python3

  import math
  import os
  import random
  import re
  import sys

  array = []

  if __name__ == '__main__':
      s = input()
      s_uniquie = ''.join(set(s))

      for letter in s_uniquie:
          array.append((letter,s.count(letter)))

      result_array  = sorted(array, key=lambda c: (-c[1], c[0]))


      for i in range(3):
          print(result_array[i][0] + ' ' + str(result_array[i][1]))



