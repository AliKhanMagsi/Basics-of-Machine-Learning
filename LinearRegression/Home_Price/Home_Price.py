#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[26]:


df=pd.read_csv('F:\\5th Semester\\ML\\Python\\Home_Price\\Book1.csv')
df


# In[34]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(df.area,df.price, color='black', marker='*')


# In[28]:


reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)


# In[35]:


reg.predict([[4300]])


# In[ ]:




