  # Enter your code here. Read input from STDIN. Print output to STDOUT
  from itertools import permutations

  string, num = input().split()

  string_array = list(string)
  string_array.sort()
  new_string = ''.join(string_array)

  result = list(permutations(new_string,int(num)))


  for values in result:
      for value in values:
          print(value,end='')
      print()
