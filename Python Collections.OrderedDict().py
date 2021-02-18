  # Enter your code here. Read input from STDIN. Print output to STDOUT
  from collections import OrderedDict

  ordered_dictionary = OrderedDict()

  num = int(input())

  for i in range(num):
      array = input().split()

      item = ''
      for i in range(len(array)-1):
          item+=(array[i]+' ')

      price = array[len(array)-1]
      price.strip()

      if item not in ordered_dictionary:
          ordered_dictionary[item] = int(price)
      else:
          ordered_dictionary[item] += int(price)




  for key, value in ordered_dictionary.items():
      print(key+str(value))
