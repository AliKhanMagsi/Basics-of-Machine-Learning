#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('F:\\Final\\customer.csv')
df


# In[3]:


missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)


# In[6]:


numerical_features = ['Age', 'Income', 'Monthly Spending']
categorical_features = ['City', 'Education Level', 'Preferred Product Category']
numerical_imputer = SimpleImputer(strategy='mean')
df[numerical_features] = numerical_imputer.fit_transform(df[numerical_features])
categorical_imputer = SimpleImputer(strategy='most_frequent')
df[categorical_features] = categorical_imputer.fit_transform(df[categorical_features])
missing_values_after = df.isnull().sum()
print("Missing Values After Imputation:\n", missing_values_after)


# In[7]:


numerical_features_for_pca = ['Age', 'Income', 'Monthly Spending']


# In[8]:


df_numerical = df[numerical_features_for_pca]
df_numerical_standardized = (df_numerical - df_numerical.mean()) / df_numerical.std()


# In[9]:


pca = PCA()
pca_result = pca.fit_transform(df_numerical_standardized)


# In[10]:


explained_variance_ratio = pca.explained_variance_ratio_


# In[11]:


cumulative_variance_ratio = explained_variance_ratio.cumsum()
plt.plot(range(1, len(cumulative_variance_ratio) + 1), cumulative_variance_ratio, marker='o')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance Ratio')
plt.title('PCA - Cumulative Explained Variance')
plt.show()


# In[21]:


num_components = 3
pca = PCA(n_components=num_components)
pca_result = pca.fit_transform(df_numerical_standardized)


# In[22]:


df_pca = pd.DataFrame(data=pca_result, columns=[f'PC{i}' for i in range(1, num_components + 1)])


# In[23]:


df_final = pd.concat([df, df_pca], axis=1)


# In[24]:


sns.scatterplot(x='PC1', y='PC2', hue='Preferred Product Category', data=df_final)
plt.title('PCA - Reduced Space Visualization')
plt.show()


# In[25]:


df_final.to_csv('F:\\Final\\customer1.csv', index=False)


# In[ ]:


In the above code I use 2 components because we reduce the dimensionality of our data. This can be beneficial for various reasons, such as simplifying models, reducing computational complexity, and potentially improving the interpretability of the data.
It is difficult to visualize the 3D or more the 3D

