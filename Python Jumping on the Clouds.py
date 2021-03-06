  #!/bin/python3

  import math
  import os
  import random
  import re
  import sys

  # Complete the jumpingOnClouds function below.
  def jumpingOnClouds(c):
      jump=0
      index=0
      while(index<len(c)-3):
          if c[index+1] ==0 and c[index+2]==0:
              jump+=1
              index+=2

          elif c[index+1] ==1 and c[index+2]==0:
              jump+=1
              index+=2 

          elif c[index+1] ==0 and c[index+2]==1:
              jump+=1
              index+=1

          else:
              pass

      jump+=1

      return jump

  if __name__ == '__main__':
      fptr = open(os.environ['OUTPUT_PATH'], 'w')

      n = int(input())

      c = list(map(int, input().rstrip().split()))

      result = jumpingOnClouds(c)

      fptr.write(str(result) + '\n')

      fptr.close()
