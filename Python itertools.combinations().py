  # Enter your code here. Read input from STDIN. Print output to STDOUT

  from itertools import combinations

  string, num = input().split()
  num = int(num)

  string_array = list(string)
  string_array.sort()
  new_string = ''.join(string_array)

  i=1

  while i<=num:
      result = list(combinations(new_string,i))

      for values in result:
          for value in values:
              print(value,end='')
          print()

      i+=1
