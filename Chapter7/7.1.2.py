import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1.shape)

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2.shape)

arr2[0:0] = 2
print(arr2)
# arr2[1:2] = 22
# arr2[0] = (2, 2, 2, 2, 2)
# print(arr2)
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2.sum())
print(arr2.sum(axis=0))
print(arr2.sum(axis=1))
