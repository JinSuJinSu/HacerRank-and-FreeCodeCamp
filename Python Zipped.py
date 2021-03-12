  # Enter your code here. Read input from STDIN. Print output to STDOUT
  student_num, subject_num= list(map(int,input().split()))

  array = []
  final_array=[]

  for i in range(subject_num):
      array.append(list(map(float,input().split())))

  final_array = list(zip(*array))

  for values in final_array:
      print(sum(values)/len(values))


