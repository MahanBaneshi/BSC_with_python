import numpy as np
import matplotlib.pyplot as plt

# create FWHM
def empFWHM(x, y):
    
    normalized_y = (y - np.min(y)) / (np.max(y) - np.min(y))
    peak_index = np.argmax(normalized_y)
    
    # find halfMaxes
    pre_half_max_x = x[np.where(normalized_y[:peak_index] >= 0.5)[-1][0]]
    post_half_max_x = x[np.where(normalized_y[peak_index:] >= 0.5)[0][0] + peak_index]
    
    # calculate FWHM
    fwhm = post_half_max_x - pre_half_max_x
    return fwhm, pre_half_max_x, post_half_max_x

# experiment
sigma_values = np.linspace(1, 5, 50)
fwhm_empirical = []
fwhm_analytical = []

for sigma in sigma_values:
    x = np.linspace(-8, 8, 1001)
    y = np.exp(-x**2 / (2 * sigma**2))
    
    fwhm_exp, _, _ = empFWHM(x, y)
    fwhm_empirical.append(fwhm_exp)
    fwhm_analytical.append(2.35482 * sigma)  

# plot
plt.figure(figsize=(8, 6))
plt.plot(sigma_values, fwhm_empirical, 'ks-', label='Empirical FWHM') 
plt.plot(sigma_values, fwhm_analytical, 'd-', color='gray', label='Analytical FWHM') 
plt.xlabel('σ (Standard Deviation)')
plt.ylabel('FWHM')
plt.title('Comparison of Empirical and Analytical FWHM')
plt.legend()
plt.grid(True)
plt.show()

# FWHM and histogram
data = np.random.normal(0, 1, 12345)
hist_values, bin_edges = np.histogram(data, bins=100, density=True)

# middles
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# calculate FWHM
fwhm_histogram, pre_half_max, post_half_max = empFWHM(bin_centers, hist_values)

# plot histogram
plt.figure(figsize=(8, 6))
plt.bar(bin_centers, hist_values, width=(bin_edges[1] - bin_edges[0]), color='lightblue', label='Histogram')
plt.axvline(pre_half_max, color='r', linestyle='--', label='Half-Max Points')
plt.axvline(post_half_max, color='r', linestyle='--')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title(f'Empirical FWHM = {fwhm_histogram:.2f}')
plt.legend()
plt.grid(True)
plt.show()