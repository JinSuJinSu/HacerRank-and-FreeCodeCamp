  # Enter your code here. Read input from STDIN. Print output to STDOUT

  num = int(input())
  map_array = map(int, input().rstrip().split())
  num_array = list(map_array)

  #1. calculate mean
  mean = round((sum(num_array)/len(num_array)),1)

  #2. calculate median
  def getMedian(arg):
      arg.sort()
      arg_len = len(arg)                
      arg_center = int(arg_len / 2)

      if arg_len % 2 == 1:
          return arg[arg_center] 
      else:
          return (arg[arg_center - 1] + arg[arg_center]) /2


  median = round(getMedian(num_array),1)


  #3. calculate mode
  num_list = list(set(num_array))
  count_list = []

  mode = 0
  max_count = 0
  max_count_array = []

  if len(num_list) == len(num_array):
      mode = min(num_list)

  else:
      for value in num_list:
          count_list.append(num_array.count(value))

      max_count = max(count_list)

      for value in num_list:
          if num_array.count(value)==max_count:
              max_count_array.append(value)

          else:
              pass

      mode = min(max_count_array)


  print(mean)
  print(median)
  print(mode)


