import numpy as np
from scipy import stats

data = np.arange(3,10)
data_z_me = (data-np.mean(data)) / np.std(data,ddof=1)
data_z_sp = stats.zscore(data,ddof=1)

print(data_z_me)
print(data_z_sp)

data = np.arange(0,12).reshape(4,3)**2
data_z_col = stats.zscore(data,ddof=1,axis=0) 
data_z_mat = stats.zscore(data,ddof=1,axis=None) 

print('Original data matrix:')
print(data)

print(' ')
print('Column-wise z-scoring:')
print(data_z_col)

print(' ')
print('Matrix-wise z-scoring:')
print(data_z_mat)