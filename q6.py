import numpy as np
import matplotlib.pyplot as plt

def add_outlier(data):
    max_value_index = np.argmax(data)
    outlier = data[max_value_index] ** 4  
    data[max_value_index] = outlier 
    return data

def plot_histogram(data, title, ax, x_limit=None):
    mean_value = np.mean(data)
    median_value = np.median(data)

    if x_limit:
        filtered_data = np.copy(data)
        filtered_data[filtered_data > x_limit[1]] = x_limit[1]
    else:
        filtered_data = data

    ax.hist(filtered_data, bins=30, alpha=0.7, color='gray', edgecolor='black')
    ax.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label='Mean')
    ax.axvline(median_value, color='blue', linestyle='dashed', linewidth=2, label='Median')
    ax.set_title(title)
    ax.legend()

    if x_limit:
        ax.set_xlim(x_limit)

data_50 = np.random.normal(loc=0, scale=1, size=50)
data_50_outlier = add_outlier(np.copy(data_50))
data_5000 = np.random.normal(loc=0, scale=1, size=5000)
data_5000_outlier = add_outlier(np.copy(data_5000))

x_limit_50 = (-4, 4) 
x_limit_5000 = (-6, 6)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
plot_histogram(data_50, "N=50, No Outlier", axes[0], x_limit_50)
plot_histogram(data_50_outlier, "N=50, With Outlier", axes[1], x_limit_50)
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
plot_histogram(data_5000, "N=5000, No Outlier", axes[0], x_limit_5000)
plot_histogram(data_5000_outlier, "N=5000, With Outlier", axes[1], x_limit_5000)
plt.tight_layout()
plt.show()

print(f"Mean shift for N=50: {np.mean(data_50_outlier) - np.mean(data_50):.2f}")
print(f"Median shift for N=50: {np.median(data_50_outlier) - np.median(data_50):.2f}")
print(f"Mean shift for N=5000: {np.mean(data_5000_outlier) - np.mean(data_5000):.2f}")
print(f"Median shift for N=5000: {np.median(data_5000_outlier) - np.median(data_5000):.2f}")
