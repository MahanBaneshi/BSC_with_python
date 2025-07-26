import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

x = np.linspace(0, 10, 200) 
shape = 0.5  
scale = np.exp(1) 

# create cdf
cdf = lognorm.cdf(x, shape, scale=scale)

# 1:create pdf by lognorm
pdf_direct = lognorm.pdf(x, shape, scale=scale)

# 2: create pdf by cdf
dx = x[1] - x[0]
pdf_derivative = np.gradient(cdf, dx)
pdf_derivative_normalized = pdf_derivative / np.trapz(pdf_derivative, x)

# plot cdf
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(x, cdf, label="CDF", color="blue")
plt.title("CDF of Lognormal Distribution")
plt.xlabel("x")
plt.ylabel("Cumulative Probability")
plt.grid(True)
plt.legend()

# plot pdf
plt.subplot(2, 1, 2)
plt.plot(x, pdf_direct, label="PDF (Direct from lognorm.pdf)", color="green")
plt.plot(x, pdf_derivative_normalized, label="PDF (Derived from CDF)", color="red", linestyle="dashed")
plt.title("PDFs of Lognormal Distribution")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

print(pdf_direct == pdf_derivative_normalized)