  # Enter your code here. Read input from STDIN. Print output to STDOUT
  condition_num, set_num = list(map(int,input().split()))

  num_array= input().split()

  set_A = set(input().split())
  set_B = set(input().split())



  happiness = 0

  for value in num_array:
      if value in set_A:
          happiness+=1

      elif value in set_B:
          happiness-=1

  print(happiness)
