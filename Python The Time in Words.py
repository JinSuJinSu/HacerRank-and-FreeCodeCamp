  #!/bin/python3
  import math
  import os
  import random
  import re
  import sys

  # Complete the timeInWords function below.
  def timeInWords(h, m):
      time_list = ["one",
          "two",
          "three",
          "four",
          "five",
          "six",
          "seven",
          "eight",
          "nine",
          "ten",
          "eleven",
          "twelve",
          "thirteen",
          "fourteen",
          "quarter",
          "sixteen",
          "seventeen",
          "eighteen",
          "nineteen",
          "twenty",
          "twenty one",
          "twenty two",
          "twenty three",
          "twenty four",
          "twenty five",
          "twenty six",
          "twenty seven",
          "twenty eight",
          "twenty nine",
          "half"
      ]
      hour = int(h)
      minute = int(m)

      string=''

      # string_calculation
      if minute==0:
          string = "o' clock"

      elif minute>0 and minute<=30:
          string = ' past '

      else:
          string = ' to '


      # minute_calculation
      minute_conditon = ''


      if minute==1 or minute==59:
          minute_conditon = ' minute'

      elif minute==15 or minute==30 or minute==45:
          pass
      else:
          minute_conditon = ' minutes'




      if minute!=0:
          if minute<=30:
              minute_result = time_list[minute-1]
          else:
              minute_result=time_list[60-minute-1]
              hour+=1

      hour_result  = time_list[hour-1]




      final_result = ''

      if minute==0:
          final_result = str(hour_result) + " " + string
      else:
          final_result = str(minute_result) + minute_conditon  +  string + str(hour_result)

      return final_result








  if __name__ == '__main__':
      fptr = open(os.environ['OUTPUT_PATH'], 'w')

      h = int(input())

      m = int(input())

      result = timeInWords(h, m)

      fptr.write(result + '\n')

      fptr.close()
