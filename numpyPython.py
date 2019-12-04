import numpy as np

arr = np.array([1, 2, 3])
print(arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr1)
print(arr1[0, 1])
print(arr1.shape)
print(arr1.size)
print(arr1.ndim)


x = np.zeros((2, 3))
print(x)
x1 = np.ones((4, 5))
print(x1)
x2 = np.arange(10)
print(x2)
x3 = np.linspace(1, 4, 6)
print(x3)
x4 = np.full((2, 2), 8)
print(x4)
x5 = np.random.random((4, 5))
print(x5)
