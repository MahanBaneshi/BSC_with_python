import numpy as np
import matplotlib.pyplot as plt

population_std = 2.4
population_mean = 0

sample_sizes = np.arange(10, 1001, 10) 
n_trials = 50
sample_stds = []

for size in sample_sizes:
    for _ in range(n_trials):
        sample = np.random.normal(population_mean, population_std, size)
        std = np.std(sample, ddof=1)  
        sample_stds.append((size, std)) 

sizes, stds = zip(*sample_stds)

plt.figure(figsize=(10, 6))
plt.scatter(sizes, stds, color='gray', alpha=0.5, label='Sample stds', marker='s')
plt.axhline(population_std, color='black', linewidth=2, label='Population std')

plt.xlabel("Sample size")
plt.ylabel("Standard deviation value")
plt.title("Sample Standard Deviations vs. Population Std (LLN)")
plt.legend()
plt.grid(True)
plt.show()
