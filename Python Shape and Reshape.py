  import numpy

  array = list(map(int,input().split()))

  numpy_array = numpy.array(array)
  print(numpy.reshape(numpy_array,(3,3)))
