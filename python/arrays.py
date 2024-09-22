import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
   arr = numpy.array(arr, float)
   reversed_array = arr[::-1]
   return reversed_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)