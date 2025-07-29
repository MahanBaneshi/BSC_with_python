import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def min_max_scaler(data,min,max):
  before_min = np.min(data)
  before_max = np.max(data)
  x = (data-before_min) / (before_max-before_min)
  newData = x*(max-min) + min
  return newData

data = np.random.randn(50)
a = 14.3
b = 34

x1 = min_max_scaler(data,a,b)

print(f'min value: {np.min(x1)}')
print(f'max value: {np.max(x1)}')

scaler = MinMaxScaler(feature_range=(a,b))
scaler.fit(data.reshape(-1,1))

x2 = scaler.transform(data.reshape(-1,1))

print(f'Min value: {np.min(x2)}')
print(f'Max value: {np.max(x2)}')

np.hstack((x1.reshape(-1,1),x2.reshape(-1,1)))

plt.plot(x1,x2,'ko',markerfacecolor=(.1,.2,.3),markersize=12)
plt.xlabel('My scalar')
plt.ylabel("sklearn's scalar")
plt.grid()
plt.show()