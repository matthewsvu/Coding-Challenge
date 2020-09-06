#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_samples
from sklearn.metrics import silhouette_score

import matplotlib.pyplot as plt
import matplotlib as mpl



get_ipython().run_line_magic('matplotlib', 'inline')


# In[41]:


# Import data
df = pd.read_csv("C:\\Users\Matthew Vu\Coding-Challenge\ClusterPlot.csv")
df.head()


# In[42]:


dfClustering = df[['V1','V2']]
dfClustering.head()


# In[43]:


# Extract Features to suitable format
X = dfClustering.iloc[:, :].values


# In[44]:


wscc = []

for i in range(1, 11):
    
    # 1. Fit the KMeans algo to data X
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300,
                   n_init = 10, random_state = 42)
    kmeans.fit(X)
    # max_iter: Is the max num of iterations there can be to find the final clusters
    # when kmeans algo is running.
    # 2 compute within cluster sum of squares and append to wscc list
    wscc.append(kmeans.inertia_)


# In[49]:


_ = plt.plot(range(1,11), wscc, linewidth = 4, color = 'black',
        marker = 'D', markersize = 10)
_ = plt.title('Elbow Method', family = 'Arial', fontsize = 14, color = 'black')
_ = plt.xlabel('Num of clusters', family = 'Arial', fontsize = 12, color = 'black')
_ = plt.ylabel('WCSS (inertia)', family = 'Arial', fontsize = 12, color = 'black')
_ = plt.xticks(fontsize = 12, color = 'black')
_ = plt.yticks(fontsize = 12, color = 'black')
_ = plt.grid(which = 'both', color = 'black', axis = 'x', alpha = 0.5)

numClusters = 2

_ = plt.axvline(x = numClusters, linewidth = 2, color = 'blue', linestyle = "--")
_ = plt.show()


# In[46]:


#Create a list of hypothetical scenarios for different number of clusters
kmeansPerK = [KMeans(n_clusters=k, random_state = 42).fit(X) for k in range(1,10)]
silhouette_scores = [silhouette_score(X,model.labels_)
                    for model in kmeansPerK[1:]]


# In[47]:

# S
k = np.argmax(silhouette_scores) + 2


# In[48]:


print('Num of clusters is ', k)







