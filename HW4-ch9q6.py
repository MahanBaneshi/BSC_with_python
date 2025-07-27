import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

np.random.seed(42)
x = np.random.normal(0, 1, 1000000)
population = x**2
true_mean = np.mean(population)

sample_sizes = np.arange(5, 501, 8)
num_samples = 1000
bins = np.linspace(0.4, 1.6, 40)

def calculate_fwhm(hist, bin_centers):
    peak_idx = np.argmax(hist)
    half_max = hist[peak_idx] / 2

    left_candidates = np.where(hist[:peak_idx] <= half_max)[0]
    left_idx = left_candidates[-1] if len(left_candidates) > 0 else 0

    right_candidates = np.where(hist[peak_idx:] <= half_max)[0]
    if len(right_candidates) > 0:
        right_idx = right_candidates[0] + peak_idx
    else:
        right_idx = len(hist) - 1

    if left_idx >= right_idx:
        return bin_centers[-1] - bin_centers[0]  
    return bin_centers[right_idx] - bin_centers[left_idx]

results = []
for n in sample_sizes:
    sample_means = [np.mean(np.random.choice(population, n)) for _ in range(num_samples)]
    hist, bin_edges = np.histogram(sample_means, bins=bins, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    try:
        fwhm = calculate_fwhm(hist, bin_centers)
        peak_value = bin_centers[np.argmax(hist)]
    except Exception as e:
        print(f"Error at n={n}: {str(e)}")
        fwhm = np.nan
        peak_value = np.nan

    results.append({'n': n, 'hist': hist, 'fwhm': fwhm, 'peak': peak_value})

plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
fwhms = [res['fwhm'] for res in results if not np.isnan(res['fwhm'])]
valid_sample_sizes = [res['n'] for res in results if not np.isnan(res['fwhm'])]
plt.plot(valid_sample_sizes, fwhms, 'o-', color='royalblue')
plt.axvline(400, color='red', linestyle='--', alpha=0.5)
plt.title('Panel A: FWHM vs Sample Size', fontsize=14)
plt.xlabel('Sample Size (N)', fontsize=12)
plt.ylabel('FWHM of Distribution', fontsize=12)
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
peaks = [res['peak'] for res in results if not np.isnan(res['peak'])]
plt.plot(valid_sample_sizes, peaks, 'o-', color='green')
plt.axhline(true_mean, color='red', linestyle='--', label=f'True Mean: {true_mean:.3f}')
plt.title('Panel B: Peak Value vs Sample Size', fontsize=14)
plt.xlabel('Sample Size (N)', fontsize=12)
plt.ylabel('Peak Value', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(12, 8))
norm = Normalize(vmin=5, vmax=500)

for res in results:
    if not np.isnan(res['fwhm']):
        ax.plot(bin_centers, res['hist'], color=plt.cm.gray(norm(res['n'])), linewidth=1.5)

ax.set_title('Sample Mean Distributions (Darker = Larger N)', fontsize=14)
ax.set_xlabel('Sample Mean', fontsize=12)
ax.set_ylabel('Density', fontsize=12)

sm = ScalarMappable(norm=norm, cmap='gray')
sm.set_array([])  
fig.colorbar(sm, ax=ax, label='Sample Size (N)')

plt.show()
