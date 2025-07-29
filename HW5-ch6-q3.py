from matplotlib import pyplot as plt
import numpy as np

data = np.random.randint(4,15,25)

orig_m = np.mean(data)
orig_s = np.std(data,ddof=1)

dataz = (data-orig_m) / orig_s
data_inv = dataz*orig_s + orig_m

plt.figure(figsize=(8,4))
plt.plot(data,'bs',markersize=12,markerfacecolor='w',label='Original_data')
plt.plot(data,'ro',markersize=5,markerfacecolor='w',label='New_data')

plt.legend()
plt.xlabel('Data index')
plt.ylabel('Data value')
plt.grid()
plt.show()