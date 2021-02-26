  # Enter your code here. Read input from STDIN. Print output to STDOUT

  sample = list(input())

  array = list(map(int,sample))

  first_tuple = 0
  second_tuple = 0

  result_array = []

  for i in range(len(array)):
      if i==0:
          first_tuple +=1
          second_tuple =array[i]

      elif i<len(array)-1:
          if array[i-1]==array[i]:
              first_tuple +=1
          else:
              result_array.append((first_tuple,second_tuple))
              first_tuple =1
              second_tuple =array[i]
      else:
          if array[i-1]==array[i]:
              first_tuple +=1
              result_array.append((first_tuple,second_tuple))
          else:
              result_array.append((first_tuple,second_tuple))
              result_array.append((1,array[i]))


  if len(array)>1:    
      for value in result_array:
          print(value, end=' ')

  else:
      print((1,1))  


