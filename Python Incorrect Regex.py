  # Enter your code here. Read input from STDIN. Print output to STDOUT
  import re

  num = int(input())

  for i in range(num):

      regex = input()

      try:
          re.compile(regex)
          print(True)
      except re.error:
          print(False)
