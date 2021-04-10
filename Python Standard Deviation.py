  # Enter your code here. Read input from STDIN. Print output to STDOUT
  num = int(input())
  num_array = list(map(int, input().rstrip().split()))
  mean = sum(num_array)/len(num_array)

  first_result = 0
  for value in num_array:
      first_result +=(value-mean)**2

  final_result = round(((first_result/len(num_array))**0.5),1)

  print(final_result)
