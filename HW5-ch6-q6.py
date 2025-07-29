from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

X1 = np.arctanh(np.random.uniform(-.999,.999,size=5000))
X2 = np.arctanh(np.random.uniform(-.2,.999,size=5000))
X3 = np.arctanh(np.random.uniform(-.999,.8,size=5000))

skews = [0]*3
skews[0] = stats.skew(X1)
skews[1] = stats.skew(X2)
skews[2] = stats.skew(X3)

_,axs = plt.subplots(1,3,figsize=(10,3.5))

axs[0].hist(X1,40,color=(.8,.8,.8),edgecolor='k')
axs[0].set_title(f'$\\bf{{A}}$)  skew = {skews[0]:.2f}')

axs[1].hist(X2,40,color=(.8,.8,.8),edgecolor='k')
axs[1].set_title(f'$\\bf{{B}}$)  skew = {skews[1]:.2f}')

axs[2].hist(X3,40,color=(.8,.8,.8),edgecolor='k')
axs[2].set_title(f'$\\bf{{C}}$)  skew = {skews[2]:.2f}')


for a in axs:
  a.set(yticks=[],ylabel='Counts',xticks=[],xlabel='Data values')

plt.tight_layout()
plt.grid()
plt.show()