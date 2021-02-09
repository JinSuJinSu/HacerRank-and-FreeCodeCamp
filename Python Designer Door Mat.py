Refer the READEME.md

  # Enter your code here. Read input from STDIN. Print output to STDOUT

  num1, num2 = list(map(int,input().split()))

  drawing = '.|.'
  string =  'WELCOME';

  i=1

  while i<num1:
      print((drawing*i).center(num2,'-'))
      i+=2


  print(string.center(num2,'-'))


  j=num1-2


  while j>=1:
      print((drawing*j).center(num2,'-'))
      j-=2
