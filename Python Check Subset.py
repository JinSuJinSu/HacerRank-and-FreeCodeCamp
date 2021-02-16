  # Enter your code here. Read input from STDIN. Print output to STDOUT

  num = int(input())

  for i in range(num):
      set1_num = int(input())
      set1 = set(map(int,input().split()))

      set2_num = int(input())
      set2 = set(map(int,input().split()))

      print(set1.issubset(set2))



