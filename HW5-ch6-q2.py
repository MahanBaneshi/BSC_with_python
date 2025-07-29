from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

X = (np.random.randn(10000)+3)**2

y_r,x_r = np.histogram(X,bins=100) # r = raw
y_l,x_l = np.histogram(np.log(X),bins=100) # l = log
y_s,x_s = np.histogram(np.sqrt(X),bins=100) # s = sqrt

_,axs = plt.subplots(1,3,figsize=(10,4))

q = np.linspace(.1,10,100)
axs[0].plot(q,np.log(q),'k',linewidth=3,label='ln(x)')
axs[0].plot(q,np.sqrt(q),'--',color='gray',linewidth=3,label='sqrt(x)')
axs[0].set(xlim=[0,10],xlabel='Raw data value',ylabel='Transformed data value')
axs[0].set_title(r'$\bf{A}$)  Transformation')
axs[0].legend()
axs[0].grid()

axs[1].plot((x_r[1:]+x_r[:-1])/2,y_r,'k',linewidth=2)
axs[1].set(xlabel='Raw data value',ylabel='Count')
axs[1].set_title(r'$\bf{B}$)  Data histogram')
axs[1].grid()

axs[2].plot((x_l[1:]+x_l[:-1])/2,y_l,'k',linewidth=2,label='ln(x)')
axs[2].plot((x_s[1:]+x_s[:-1])/2,y_s,'--',color='gray',linewidth=2,label='sqrt(x)')
axs[2].set(xlabel='Transformed data value',ylabel='Count')
axs[2].set_title(r'$\bf{C}$)  Trans data hist.')
axs[2].legend()
axs[2].grid()


plt.tight_layout()
plt.show()

X1 = (np.random.randn(1000)+0)**2
X2 = (np.random.randn(1000)+3)**2

X1s = np.sqrt(X1)
X2s = np.sqrt(X2)


_,axs = plt.subplots(2,2,figsize=(10,8))

stats.probplot(X1,plot=axs[0,0],fit=True)
stats.probplot(X2,plot=axs[0,1],fit=True)

stats.probplot(X1s,plot=axs[1,0],fit=True)
stats.probplot(X2s,plot=axs[1,1],fit=True)

for a in axs.flatten():
  a.get_lines()[0].set_markerfacecolor('k')
  a.get_lines()[0].set_markeredgecolor('k')
  a.get_lines()[1].set_color('gray')
  a.get_lines()[1].set_linewidth(3)
  a.set_title(' ')
  a.set_ylabel('Data values (sorted)')


axs[0,0].set_title(r'$\bf{A}$)  QQ plot of $x^2$')
axs[0,0].grid()
axs[0,1].set_title(r'$\bf{B}$)  QQ plot of $\sqrt{x^2}$')
axs[0,1].grid()
axs[1,0].set_title(r'$\bf{C}$)  QQ plot of $(x+3)^2$')
axs[1,0].grid()
axs[1,1].set_title(r'$\bf{D}$)  QQ plot of $\sqrt{(x+3)^2}$')
axs[1,1].grid()


plt.tight_layout()
plt.show()

X1s = np.log(X1)
X2s = np.log(X2)


_,axs = plt.subplots(2,2,figsize=(10,8))

stats.probplot(X1,plot=axs[0,0],fit=True)
stats.probplot(X2,plot=axs[0,1],fit=True)

stats.probplot(X1s,plot=axs[1,0],fit=True)
stats.probplot(X2s,plot=axs[1,1],fit=True)

for a in axs.flatten():
  a.get_lines()[0].set_markerfacecolor('k')
  a.get_lines()[0].set_markeredgecolor('k')
  a.get_lines()[1].set_color('gray')
  a.get_lines()[1].set_linewidth(3)
  a.set_title(' ')
  a.set_ylabel('Data values (sorted)')


axs[0,0].set_title(r'$\bf{A}$)  QQ plot of $x^2$')
axs[0,0].grid()
axs[0,1].set_title(r'$\bf{B}$)  QQ plot of $\ln{x^2}$')
axs[0,1].grid()
axs[1,0].set_title(r'$\bf{C}$)  QQ plot of $(x+3)^2$')
axs[1,0].grid()
axs[1,1].set_title(r'$\bf{D}$)  QQ plot of $\ln{(x+3)^2}$')
axs[1,1].grid()

plt.tight_layout()
plt.show()

X = (np.random.randn(10000)+3)**2
Y = np.sqrt(X)
Y -= np.mean(Y)
y_s2,x_s2 = np.histogram(Y,bins=100)

plt.plot((x_s[1:]+x_s[:-1])/2,y_s,linewidth=2,label='sqrt(x)')
plt.plot((x_s2[1:]+x_s2[:-1])/2,y_s2,linewidth=2,label='shifted sqrt(x)')
plt.xlabel('Transformed data value')
plt.ylabel('Count')
plt.legend()
plt.grid()
plt.show()