import numpy as np
import matplotlib.pyplot as plt

most_news = [15, 5, 70, 10]
source_labels = ['TV', 'Newspapers', 'Internet', 'Word of Mouth']

plt.figure(figsize=(8, 4))

colors = ['#f48b04', '#fff75a', '#08ff01', '#59ebff']  
bars = plt.bar(source_labels, most_news, color=colors, edgecolor='black', linewidth=0.9, width=0.9)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height + 1, f'{height}%', 
             ha='center', fontsize=10, fontweight='bold', color='black')

plt.title('Where Do People Get Their News?', fontsize=14, fontweight='bold', color='#34495E')
plt.ylabel('Percent Responding "Yes"', fontsize=12, color='#34495E')
plt.xlabel('Media Type', fontsize=12, color='#34495E')

plt.xticks(rotation=-20, fontsize=10, fontweight='bold', color='#2C3E50')
plt.yticks(fontsize=10, color='#2C3E50')

plt.grid(axis='y', linestyle='--', alpha=1)

plt.tight_layout()
plt.show()
