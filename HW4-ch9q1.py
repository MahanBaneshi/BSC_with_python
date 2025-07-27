import numpy as np
import matplotlib.pyplot as plt

n_samples = 20         
n_points = 200         
tau_squared_vals = np.linspace(0.1, 10, 40) 

all_sample_means = []            
all_sample_variances = []         
mean_of_means = []               
mean_of_variances = []           
variance_of_means = []           

for tau_squared in tau_squared_vals:
    sample_means = []
    sample_vars = []
    
    for _ in range(n_samples):
        data = np.random.normal(0, np.sqrt(tau_squared), n_points)
        sample_means.append(np.mean(data))
        sample_vars.append(np.var(data, ddof=1))  

    all_sample_means.append(sample_means)
    all_sample_variances.append(sample_vars)
    mean_of_means.append(np.mean(sample_means))
    mean_of_variances.append(np.mean(sample_vars))
    variance_of_means.append(np.var(sample_means, ddof=1))

# plots
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

axs[0].set_title('A) Sample averages')
for i, tau_squared in enumerate(tau_squared_vals):
    axs[0].scatter([tau_squared]*n_samples, all_sample_means[i], color='gray', marker='s', alpha=0.7)

axs[0].scatter(tau_squared_vals, mean_of_means, color='white', edgecolors='black', marker='D', s=60, zorder=3)
axs[0].set_xlabel(r'$\tau^2$')
axs[0].set_ylabel('Value')
axs[0].legend()

axs[1].set_title('B) Sample variances')
axs[1].plot(tau_squared_vals, mean_of_variances, marker='^', label='Average variances', color='black')
axs[1].plot(tau_squared_vals, variance_of_means, marker='o', label='Variance of averages', color='black', linestyle='none')

axs[1].legend()
axs[1].set_xlabel(r'$\tau^2$')
axs[1].set_ylabel('Value')

plt.tight_layout()
plt.show()
