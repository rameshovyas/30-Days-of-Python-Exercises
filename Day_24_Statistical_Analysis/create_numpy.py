# Creating int numpy arrays
import numpy as np

# One dimensional
my_list = [1,2,3,4,5]
numpy_list = np.array(my_list)

print(type(my_list))
print(type(numpy_list))

# Two dimensional
my_2d_list = [[1,2,3],[4,5,6],[7,8,9]]
numpy_2d_list = np.array(my_2d_list)
print(numpy_2d_list)

print(type(my_2d_list))
print(type(numpy_2d_list))

# Creating floating type arrays
np_float_list = np.array(my_list,dtype=float)
print(np_float_list)

# Creating boolean type arrays
np_bool_list = np.array([1,0,-1,0,1],dtype=bool)
print(np_bool_list)

# Creating numpy array from tuple
my_tuple = (1,2,3,4,5)
np_tuple_list = np.array(my_tuple)

print(type(my_tuple))
print(type(np_tuple_list))
print(np_tuple_list)

# shape of numpy array
print(numpy_2d_list.shape)
print(np_bool_list.shape)

# Data type of numpy array
print(numpy_2d_list.dtype)
print(np_bool_list.dtype)

# Size of a numpy array
print(numpy_2d_list.size)
print(np_bool_list.size)



