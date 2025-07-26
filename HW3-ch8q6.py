import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 1001) 
dx = x[1] - x[0]

def gaussian(x, mean, std_dev):
    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std_dev**2))

# create 2 pdfs
pdf1 = gaussian(x, mean=-2.7, std_dev=1)
pdf2 = gaussian(x, mean=2.7, std_dev=1)

pdf = pdf1 + pdf2

# create cdf by pdf
cdf = np.cumsum(pdf) * dx

# normalized cdf and pdf
pdf_normalized = pdf / np.sum(pdf * dx)  
cdf_normalized = np.cumsum(pdf_normalized) * dx

# plot them
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(x, pdf, label="PDF (Unnormalized)", color='blue')
plt.plot(x, pdf_normalized, label="PDF (Normalized)", color='green', linestyle='dashed')
plt.title("PDF (Original and Normalized)")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(x, cdf, label="CDF (Unnormalized)", color='red')
plt.title("CDF (Unnormalized)")
plt.xlabel("x")
plt.ylabel("Cumulative Probability")
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(x, cdf_normalized, label="CDF (Normalized)", color='purple')
plt.title("CDF (Normalized)")
plt.xlabel("x")
plt.ylabel("Cumulative Probability")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print("Unnormalized CDF:")
print(f"Final value of unnormalized CDF: {cdf[-1]:.4f}")

print("\nNormalized CDF:")
print(f"Final value of normalized CDF: {cdf_normalized[-1]:.4f}")