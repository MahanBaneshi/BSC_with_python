import numpy as np
import matplotlib.pyplot as plt

# creating two populations
population_size = 10000
mean_pop1 = 3.0
mean_pop2 = 3.2
std_dev = 1.0

# creating data
np.random.seed(0)
population1 = np.random.normal(mean_pop1, std_dev, population_size)
population2 = np.random.normal(mean_pop2, std_dev, population_size)

sample_sizes = np.arange(10, 1001, 10)  
n_trials = 50  
mean_differences = []

# calculate differences
for size in sample_sizes:
    for _ in range(n_trials):
        sample1 = np.random.choice(population1, size, replace=False)
        sample2 = np.random.choice(population2, size, replace=False)
        mean_diff = np.mean(sample1) - np.mean(sample2)
        mean_differences.append((size, mean_diff))

sizes, diffs = zip(*mean_differences)

# plots
plt.figure(figsize=(10, 6))
plt.scatter(sizes, diffs, alpha=0.5, color='gray', label="Sample diffs", marker='s')
plt.axhline(mean_pop1 - mean_pop2, color='black', linewidth=2, label="Population diff")

plt.xlabel("Sample size")
plt.ylabel("Sample differences")
plt.title("Sample Mean Differences vs. Population Mean Difference")
plt.legend()
plt.grid(True)
plt.show()
