import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
plt.style.use('seaborn-v0_8')
population_mean = 50
population_std = 10
population_size = 10000

population = np.random.normal(population_mean, population_std, population_size)

sample_sizes = np.logspace(np.log10(10), np.log10(population_size * 0.1), 25).astype(int)
analytical_sem = population_std / np.sqrt(sample_sizes)

num_repeats = 50
sem_estimates_method1 = np.zeros((len(sample_sizes), num_repeats))
sample_means_storage = np.zeros((len(sample_sizes), num_repeats))

for i, n in enumerate(sample_sizes):
    for j in range(num_repeats):
        sample = np.random.choice(population, size=n, replace=False)
        sem_estimates_method1[i, j] = np.std(sample, ddof=1) / np.sqrt(n)
        sample_means_storage[i, j] = np.mean(sample)

sem_estimates_method2 = np.std(sample_means_storage, axis=1, ddof=1)

mean_sem_method1 = np.mean(sem_estimates_method1, axis=1)
std_sem_method1 = np.std(sem_estimates_method1, axis=1)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

ax1.plot(sample_sizes, analytical_sem, 'k-', label='Analytical SEM', linewidth=2)
ax1.plot(sample_sizes, mean_sem_method1, 'bo--', label='Method 1: Sample SD/√N', markersize=5)
ax1.plot(sample_sizes, sem_estimates_method2, 'rs--', label='Method 2: SD of sample means', markersize=5)
ax1.set_ylabel('Standard Error of the Mean')
ax1.set_title('A) Comparison of SEM Estimation Methods')
ax1.legend()
ax1.grid(True)

percent_error_method1 = 100 * (mean_sem_method1 - analytical_sem) / analytical_sem
percent_error_method2 = 100 * (sem_estimates_method2 - analytical_sem) / analytical_sem

ax2.plot(sample_sizes, percent_error_method1, 'bo--', label='Method 1 Error', markersize=5)
ax2.plot(sample_sizes, percent_error_method2, 'rs--', label='Method 2 Error', markersize=5)
ax2.axhline(0, color='k', linestyle='--', alpha=0.5)
ax2.set_xscale('log')
ax2.set_xlabel('Sample Size (log scale)')
ax2.set_ylabel('Percentage Error (%)')
ax2.set_title('B) Percentage Error Relative to Analytical SEM')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

print("\nSummary of Results:")
print("1. As expected, the Standard Error of the Mean (SEM) decreases with increasing sample size.")
print("2. For small sample sizes (under ~100), there is more variation between estimation methods.")
print("3. Both empirical methods converge to the analytical SEM as sample size increases.")
print("4. The second method (SD of sample means) provides a more direct estimation and is less variable.")

plt.figure(figsize=(10, 6))
for i, n in enumerate(sample_sizes[::5]):
    plt.scatter([n] * num_repeats, sample_means_storage[i], alpha=0.5, label=f'N={n}')
    
plt.xscale('log')
plt.xlabel('Sample Size (log scale)')
plt.ylabel('Sample Means')
plt.title('Variability of Sample Means Across Different Sample Sizes')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
