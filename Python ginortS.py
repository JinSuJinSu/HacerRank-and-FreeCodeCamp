  # Enter your code here. Read input from STDIN. Print output to STDOUT
  sample = input()

  uppercase_letters = []
  lowercase_letters = []
  odd_numbers = []
  even_numbers = []

  for string in sample:
      if string.isupper():
          uppercase_letters.append(string)

      elif string.islower():
          lowercase_letters.append(string)

      elif string.isdigit() and int(string)%2==1:
          odd_numbers.append(int(string))

      elif string.isdigit() and int(string)%2==0:
          even_numbers.append(int(string))


  uppercase_letters.sort()
  lowercase_letters.sort()

  odd_numbers.sort()
  odd_numbers = list(map(str, odd_numbers))

  even_numbers.sort()
  even_numbers = list(map(str, even_numbers))

  final_result = "".join(lowercase_letters) + "".join(uppercase_letters) + "".join(odd_numbers) + "".join(even_numbers)

  print(final_result)


