  #!/bin/python3

  import math
  import os
  import random
  import re
  import sys

  # Complete the miniMaxSum function below.
  def miniMaxSum(arr):
      result_array = []
      for i in range(len(arr)):
          sub_array = arr[:]
          del sub_array[i]
          sum_result = sum(sub_array)
          result_array.append(sum_result)

      print(str(min(result_array)) +' ' + str(max(result_array)))

  if __name__ == '__main__':
      arr = list(map(int, input().rstrip().split()))

      miniMaxSum(arr)
