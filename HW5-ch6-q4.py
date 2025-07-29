import numpy as np
from matplotlib import pyplot as plt

def min_max_scaler(data,min,max):
  before_min = np.min(data)
  before_max = np.max(data)
  x = (data-before_min) / (before_max-before_min)
  newData = x*(max-min) + min
  return newData

N = 313
lo_bnd = 3*np.pi
hi_bnd = np.exp(np.pi)

data = np.random.uniform(lo_bnd,hi_bnd,size=N)

dataScale = min_max_scaler(data,-.999,.999) 

dataFish = np.arctanh(dataScale)

dataFinal = dataFish - np.mean(dataFish) + (lo_bnd+hi_bnd)/2

print(f'Expected mean : {(lo_bnd+hi_bnd)/2:.3f}')
print(f'Empirical mean: {np.mean(dataFinal):.3f}')

yO,xO = np.histogram(data,bins='fd')
yF,xF = np.histogram(dataFinal,bins='fd')

xO = (xO[1:]+xO[:-1])/2
xF = (xF[1:]+xF[:-1])/2

plt.figure(figsize=(8,4))
plt.plot(xO,yO,'rs--',linewidth=3,label='Original data')
plt.plot(xF,yF,'g^-',linewidth=3,label='Transformed data')

plt.axvline(x=np.mean(data),color='black', linestyle=':',label='DataAverage')

plt.xlabel('Data value')
plt.ylabel('Count')
plt.legend()

plt.tight_layout()
plt.grid()
plt.show()