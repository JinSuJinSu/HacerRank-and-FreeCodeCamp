  # Enter your code here. Read input from STDIN. Print output to STDOUT

  from collections import Counter

  num1 = int(input())

  shoes = list(map(int,(input().split())))

  num2=  int(input())

  customers = []

  i=1

  eraned_money=0

  while i<=num2:
      customers.append(list(map(int,(input().split()))))
      i+=1

  for value in customers:
      size = value[0]
      price = value[1]

      if size in shoes:
          eraned_money+=price
          shoes.remove(size)

      else:
          pass

  print(eraned_money)
