  cube = lambda x: x**3# complete the lambda function 

  def fibonacci(n):
      # return a list of fibonacci numbers
      result_list = []

      for i in range(n):
          if i==0 or i==1:
              result_list.append(i)
          else:
              result_list.append(result_list[i-2]+result_list[i-1])

      return result_list



  if __name__ == '__main__':
      n = int(input())
      print(list(map(cube, fibonacci(n))))
