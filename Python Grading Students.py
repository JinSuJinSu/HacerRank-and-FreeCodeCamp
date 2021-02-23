  #!/bin/python3

  import math
  import os
  import random
  import re
  import sys

  #
  # Complete the 'gradingStudents' function below.
  #
  # The function is expected to return an INTEGER_ARRAY.
  # The function accepts INTEGER_ARRAY grades as parameter.
  #

  def gradingStudents(grades):
      # Write your code here
      final_result = []
      for grade in grades:
          real_grade = grade
          while real_grade%5!=0 and real_grade>=38:
              real_grade+=1
          if real_grade - grade<3:
              grade = real_grade
          elif real_grade - grade>=3:
              grade = grade
          elif grade<38:
              grade = grade

          final_result.append(grade)

      return final_result





  if __name__ == '__main__':
      fptr = open(os.environ['OUTPUT_PATH'], 'w')

      grades_count = int(input().strip())

      grades = []

      for _ in range(grades_count):
          grades_item = int(input().strip())
          grades.append(grades_item)

      result = gradingStudents(grades)

      fptr.write('\n'.join(map(str, result)))
      fptr.write('\n')

      fptr.close()
