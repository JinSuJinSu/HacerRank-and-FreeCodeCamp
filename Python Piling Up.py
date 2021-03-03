  # Enter your code here. Read input from STDIN. Print output to STDOUT
  import collections

  num = int(input())

  for i in range(num):
      array_num = int(input())
      array = list(map(int,input().split()))

      new_array = sorted(array,reverse=True)
      deq = collections.deque(array)

      for value in new_array:
          if value==deq[0]:
              deq.popleft()
          elif value==deq[-1]:
              deq.pop()




      if deq:
          print('No')

      else:
          print('Yes')



