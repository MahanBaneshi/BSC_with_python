from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

N = 300
sample1 = np.random.randn(N)**2
sample2 = np.random.randn(N)**2

difference = sample1 - sample2

y1,x1 = np.histogram(sample1,bins='fd')
y2,x2 = np.histogram(sample2,bins='fd')
yd,xd = np.histogram(difference,bins='fd')

_,axs = plt.subplots(1,2,figsize=(10,4))

axs[0].plot((x1[:-1]+x1[1:])/2,y1,'k',linewidth=2,label='Sample 1')
axs[0].plot((x2[:-1]+x2[1:])/2,y2,'--',color='gray',linewidth=2,label='Sample 2')
axs[0].set(xlabel='Data value',ylabel='Count')
axs[0].set_title(r'$\bf{A}$)  Individual histograms')
axs[0].grid()
axs[0].legend()

axs[1].plot((xd[:-1]+xd[1:])/2,yd,'k',linewidth=2)
axs[1].set(xlabel='Difference value',ylabel='Count')
axs[1].set_title(r'$\bf{B}$)  Difference histograms')


plt.tight_layout()
plt.grid()
plt.show()