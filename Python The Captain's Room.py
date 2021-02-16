  # Enter your code here. Read input from STDIN. Print output to STDOUT


  K = int(input())
  rooms = input().split()

  rooms.sort()
  capt_room = (set(rooms[0::2]) ^ set(rooms[1::2]))
  print(capt_room.pop())

