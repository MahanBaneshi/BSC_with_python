import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=5000)

bin_rules = {
    "Fixed (40 bins)": 40,
    "FD Rule": 'fd',   # fridman
    "Sturges Rule": 'sturges',  # sturges
    "Scott Rule": 'scott'  # scott
}

# create historgam as a graph
plt.figure(figsize=(10, 6))

for rule_name, bins in bin_rules.items():
    counts, bin_edges = np.histogram(data, bins=bins, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2 
    plt.plot(bin_centers, counts, marker='o', linestyle='-', label=rule_name)

plt.title("Histogram Comparison with Line Plot")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()
