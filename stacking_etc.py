import numpy as np

# Stacking: Arrays ko Jodna
# np.vstack: To stack arrays along vertical axis.
# np.hstack: To stack arrays along horizontal axis.
# np.column_stack: To stack 1-D arrays as columns into 2-D arrays.
# np.concatenate: To stack arrays along specified axis (axis is passed as argument).

a= np.array([[1,2,3], [4,5,6]], 'int8')
b= a*10

print('vstack((a, b)): \n{} '.format(np.vstack((a, b))))

print('hstack((a, b)): \n{} '.format(np.hstack((a, b))))

c=[1,2]
print('column_stack((a, c)): \n{} '.format(np.column_stack((a, c))))

# concatenate is superset of hstack and vstack: axis= 0: => vstack, axis= 1=> hstack
print('concatenate((a, b)): \n{} '.format(np.concatenate((a, b), 0)))



########################################################################3

# splitting

# np.hsplit: Split array along horizontal axis.
# np.vsplit: Split array along vertical axis.
# np.array_split: Split array along specified axis.

arr= np.hstack((a, b))
arr2= np.vstack((a, b))

print("hsplit(arr, 2)=> 2nd arg is no. of parts: \n{}".format(np.hsplit(arr, 2)))
print("vsplit(arr2, 2)=> 2nd arg is no. of parts: \n{}".format(np.vsplit(arr2, 2)))

print("hsplit(arr, 2) using array_split=> 2nd arg is no. of parts: \n{}".format(np.array_split(arr, 2, axis=1)))

###########################################

# linear algebra
# np.linalg.func()

# The Linear Algebra module of NumPy offers various methods to apply linear algebra on
# any numpy array. You can find:

# 1. rank, determinant, trace, etc. of an array.
# 2. eigen values of matrices
# 3. matrix and vector products (dot, inner, outer,etc. product), matrix exponentiation
# 4. solve linear or tensor equations and much more

demo= np.array([[6, 1, 1], 
              [4, -2, 5], 
              [2, 8, 7]], 'int16')

print("rank of matrix of demo= {}".format(np.linalg.matrix_rank(demo)))

print("trace of demo= {}".format(np.trace(demo)))

print("determinant of demo= {}".format(np.linalg.det(demo)))

# import matplotlib.pyplot as plt

# ##
# # x co-ordinates 
# x = np.arange(0, 9) 
# A = np.array([x, np.ones(9)]) 
  
# # linearly generated sequence 
# y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24] 
# # obtaining the parameters of regression line 
# w = np.linalg.lstsq(A.T, y)[0]  
  
# # plotting the line 
# line = w[0]*x + w[1] # regression line 
# plt.plot(x, line, 'r-') 
# plt.plot(x, y, 'o') 
# plt.show()
# ##