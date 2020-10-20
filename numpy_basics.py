# array creation

import numpy as np

print("using numpy version: {} ".format(np.__version__))
arr= np.array([[1,2,3,4,5,6], [1,2,3,4,5,6]])

print(arr)
print(arr.dtype)

arr= arr.astype('int32')
print('{}: {}'.format(arr.dtype, arr))

# The rank of the array is the number of dimensions. 
# The shape of the array is a tuple of integers giving the size of the array along each
# dimension.
print('type: {}'.format(type(arr)))
print('no. of dimensions: {}'.format(arr.ndim))
print('shape: {}'.format(arr.shape))
print('size: {}'.format(arr.size))

# specifying dtype while creating array:

new_arr= np.array([[1,2,3], [4,5,6]], 'int8')

print(new_arr)
print(new_arr.dtype)

print(np.array(list(range(10)), 'int8').reshape((2,5)))
print()

# Often, the elements of an array are originally unknown, but its size is known.
# Hence, NumPy offers several functions to create arrays with initial placeholder content.
# These minimize the necessity of growing arrays, an expensive operation.
# For example: np.zeros, np.ones, np.full, np.empty, etc.

zeros= np.zeros((3,4), 'int8')
print(zeros)

sixty_nines= np.full((3,3), 69, 'int8')
print(sixty_nines)
ones= np.ones((3,4), 'int8')
print(ones)

# np.arange (start, upper_limit_that_is_not_included, step_size_defaults_to_1)
np_arange= np.arange(1, 31, 5)
print(np_arange)

# np.linspace (start, end_included, no._of_elements)
print(np.linspace(0, 5, 20))

# np.reshape (shape)=> shape is tuple, ie. bracket wali form

reshape_demo= np.array(list(range(10)), 'int8')
print(reshape_demo)
print()
reshape_demo= reshape_demo.reshape((2,5))
print(reshape_demo)
print()
# np.flaten

print(reshape_demo.reshape((10,)))

# OR

print(reshape_demo.flatten())
