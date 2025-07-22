import numpy as np
import matplotlib.pyplot as plt

old_sources = [40,10,85,20]
new_sources = [25,7,55,13]
source_labels = ['TV','Newspapers','Internet','Word of mouth']

plt.figure(figsize=(10,3.9))
plt.bar(source_labels,new_sources,color='hotpink')
plt.title('Where do people get their news?',loc= 'center')
plt.ylabel('Percent responding "yes"')
plt.xlabel('Media type')
plt.xticks(rotation=-30)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6.3,6.3))
plt.pie(old_sources,labels=source_labels,autopct='%.2f%%',
        radius=1.2,wedgeprops={'edgecolor':'purple'}, shadow=True)

plt.tight_layout()

plt.show()