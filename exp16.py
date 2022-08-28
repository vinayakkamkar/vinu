
import numpy as np

a=np.array([[10,2,3],[4,5,6],[7,8,9]])

print("sorting along the columns:")
print(np.sort(a))

print("sorting along the rows:")
print(np.sort(a,0))

data_type=np.dtype([('name','s10'),('mark',int)])

array=np.array([('Mukesh',200),('John',251)],dtype=data_type)

print("Sorting data orderd by name")

print(np.sort(arr,order='name'))
