import numpy as np
import matplotlib.pyplot as plt

# gaussian function
def gaussian(x, mu, sigma, normalize=True):
    factor = 1 / (np.sqrt(2 * np.pi) * sigma) if normalize else 1
    return factor * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

x = np.linspace(-5, 5, 1000)
sigmas = [0.5, 1, 2]

# create gaussians
plt.figure(figsize=(8, 5))
for sigma in sigmas:
    y = gaussian(x, mu=0, sigma=sigma)
    plt.plot(x, y, label=f'σ = {sigma}')

plt.xlabel('x')
plt.ylabel('Gaussian Distribution')
plt.title('Different Gaussians with Various σ')
plt.legend()
plt.grid(True)
plt.show()

# calculate Integral for 2 domains
domains = [(-3, 3), (-5, 5)] 
for domain in domains:
    mask = (x >= domain[0]) & (x <= domain[1])
    x_domain = x[mask]
    
    print(f"\nDomain: {domain}")
    for sigma in sigmas:
        y = gaussian(x, mu=0, sigma=sigma)
        y_domain = y[mask]
        
    
        sum_gaussian = np.sum(y_domain)
        integral_gaussian = np.trapz(y_domain, x_domain)
        
        print(f"σ = {sigma}: Sum = {sum_gaussian:.4f}, Integral = {integral_gaussian:.4f}")

# without Normalization
plt.figure(figsize=(8, 5))
for sigma in sigmas:
    y = gaussian(x, mu=0, sigma=sigma, normalize=False)
    plt.plot(x, y, label=f'σ = {sigma} (No Normalization)')

plt.xlabel('x')
plt.ylabel('Gaussian Without Normalization')
plt.title('Gaussians Without Normalization Factor')
plt.legend()
plt.grid(True)
plt.show()