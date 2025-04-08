from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import numpy as np

# Données
points = np.array([[2,10], [2,5], [8,4], [5,8], [7,5], [6,4], [1,2], [4,9]])
# Clustering hiérarchique
Z = linkage(points, method='single', metric='cityblock')
# Dendrogramme
dendrogram(Z, labels=['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'])
plt.show()