  #!/bin/python3

  import math
  import os
  import random
  import re
  import sys

  # Complete the staircase function below.
  def staircase(n):
      result_array = list()
      string = ''

      for i in range(1,n+1):
          if i<n:
              string = (' '*(n-i))+('#'*i)
              result_array.append(string)
          else:
              string = '#'*i
              result_array.append(string)

      for value in result_array:
          print(value)

  if __name__ == '__main__':
      n = int(input())

      staircase(n)
