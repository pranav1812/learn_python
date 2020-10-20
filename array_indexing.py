import numpy as np

arr= np.array([[1,2,3,4, 5, 6], [5,6,7,8, 69, 1], [1,3,5,7, 101, 50]], 'int16')

indexed= arr[:2, :2]
print(indexed)

indexed= arr[:2, ::3]
print(indexed)

# changing array

print('%2 of each element: \n{}'.format(arr%2))

# unary operators along axes or the whole array
# axis= 0 => along column
# axis= 1 => along row

print('arr.sum(): {} '.format(arr.sum()))
print('arr.sum(axis=1): {} => sum along rows: length of output array= no. of rows'.format(arr.sum(axis=1)))
print('arr.sum(axis=0): {} => sum along columns: length of output array= no. of columns'.format(arr.sum(axis=0)))

# sorting

a = np.array([[1, 4, 2], [3, 4, 6], [0, -1, 5]], 'int8') 

# in sorting, you can also specify the type of algorithm=> np.sort(a, axis = 1, kind='mergesort')
print ("Array elements in sorted order:\n", np.sort(a, axis = None))
print ("Row-wise sorted array:\n", np.sort(a, axis = 1))
print ("Col-wise sorted array:\n",np.sort(a, axis=0))