import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
population = np.random.exponential(scale=1, size=100000)
num_samples = 500

def simulate_clt(sample_size):
    sample_means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size, replace=True)
        sample_means.append(np.mean(sample))
    return sample_means

means_n5 = simulate_clt(5)

means_n100 = simulate_clt(100)

# plots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(means_n5, kde=True, color='skyblue')
plt.title(f'Sample Mean Distribution (N=5)\nSkewness: {np.round(np.mean(means_n5), 3)}')
plt.xlabel('Sample Mean')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
sns.histplot(means_n100, kde=True, color='salmon')
plt.title(f'Sample Mean Distribution (N=100)\nSkewness: {np.round(np.mean(means_n100), 3)}')
plt.xlabel('Sample Mean')
plt.ylabel('Count')

plt.tight_layout()
plt.show()