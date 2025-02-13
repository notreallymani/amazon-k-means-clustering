# -*- coding: utf-8 -*-
"""amazon k means clustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18kweY2GQOXU21Sglxq7RxuvN7N9cpUpY

# K Means Clustering

## Importing libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing dataset"""

dataset = pd.read_csv('/content/amazon.csv')
X = dataset.iloc[:, [2, 4]].values

print(X)

"""## Optimal number of clusters via Elbow Method"""

from sklearn.cluster import KMeans
wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters= i, init= 'k-means++', random_state = 21)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

plt.plot(range(1,11), wcss)
plt.title('WCSS via Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS Value')

plt.show()

"""## K Means Model Training on Training set"""

kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_means = kmeans.fit_predict(X)

print(y_means)

"""## Visualizing Clusters"""

plt.scatter(X[y_means == 0, 0], X[y_means == 0, 1], s = 100, c = 'magenta', label = 'Cluster 1')
plt.scatter(X[y_means == 1, 0], X[y_means == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_means == 2, 0], X[y_means == 2, 1], s = 100, c = 'red', label = 'Cluster 3')
plt.scatter(X[y_means == 3, 0], X[y_means == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'black', label = 'Centroids')
plt.title('Cluster of Amazon users')
plt.xlabel('Age')
plt.ylabel('Purchase Rating')
plt.legend()
plt.show()