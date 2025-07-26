import numpy as np
import matplotlib.pyplot as plt

def perform_experiment(range_start, range_end, sample_sizes, repeats):
    differences = []

    for _ in range(repeats):
        difference_for_sizes = []
        for size in sample_sizes:
            # create random data
            data = np.random.randint(range_start, range_end + 1, size=size)

            # calculate Variances
            variance_population = np.var(data, ddof=0)
            variance_sample = np.var(data, ddof=1)

            difference = abs(variance_sample - variance_population)
            difference_for_sizes.append(difference)

        differences.append(difference_for_sizes)

    mean_differences = np.mean(differences, axis=0)
    std_differences = np.std(differences, axis=0)
    return mean_differences, std_differences

sample_sizes = range(5, 101)
repeats = 25


mean_diff_large_range, std_diff_large_range = perform_experiment(-100, 100, sample_sizes, repeats)
mean_diff_small_range, std_diff_small_range = perform_experiment(-10, 10, sample_sizes, repeats)

# plot
plt.figure(figsize=(12, 6))

plt.errorbar(sample_sizes, mean_diff_large_range, yerr=std_diff_large_range, fmt='o', label='Range: -100 to 100', ecolor='r', capsize=5)
plt.errorbar(sample_sizes, mean_diff_small_range, yerr=std_diff_small_range, fmt='o', label='Range: -10 to 10', ecolor='b', capsize=5)

plt.xlabel('Sample Size')
plt.ylabel('Mean Difference in Variance')
plt.title('Impact of Sample Size and Data Range on Variance Differences')
plt.legend()
plt.show()