import numpy as np
import matplotlib.pyplot as plt

# plot histogram
def plot_histogram(data, title, panel):

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    # calculate mean and standard deviation
    mean = np.mean(data)
    std = np.std(data)

    # Plot histogram
    plt.hist(data, bins='fd', alpha=0.7, color='blue', edgecolor='black') 
    plt.axvline(q1, color='black', linestyle='solid', label='Q1 (25th Percentile)')
    plt.axvline(q3, color='black', linestyle='solid', label='Q3 (75th Percentile)')
    plt.axvline(mean - 1.35 * std, color='red', linestyle='dashed', label='-1.35σ')
    plt.axvline(mean + 1.35 * std, color='red', linestyle='dashed', label='+1.35σ')
    plt.title(f"{title} (Panel {panel})")
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)

    return iqr, std

np.random.seed(42)
normal_data = np.random.normal(loc=0, scale=1, size=10000)

# plot
plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
iqr_normal, std_normal = plot_histogram(normal_data, "Normal Distribution", "A")

exponential_data = np.exp(normal_data)

plt.subplot(2, 1, 2)
iqr_exponential, std_exponential = plot_histogram(exponential_data, "Exponential Distribution", "B")

plt.tight_layout()
plt.show()

# print results
print("Results for Normal Distribution:")
print(f"Standard Deviation (σ): {std_normal:.4f}")
print(f"Interquartile Range (IQR): {iqr_normal:.4f}")
print(f"IQR / σ ≈ {iqr_normal / std_normal:.4f}")

print("\nResults for Exponential Distribution:")
print(f"Standard Deviation (σ): {std_exponential:.4f}")
print(f"Interquartile Range (IQR): {iqr_exponential:.4f}")
print(f"IQR / σ ≈ {iqr_exponential / std_exponential:.4f}")