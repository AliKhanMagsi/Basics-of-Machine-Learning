#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[13]:


df=pd.read_csv('F:\\5th Semester\\ML\\Python\\Canda_Per_Income\\canada_per_capita_income.csv')
df.head()


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('Income')
plt.ylabel('year')
plt.scatter(df.year,df.income)


# In[16]:


reg= linear_model.LinearRegression()
reg.fit(df[['year']],df.income)


# In[18]:


reg.predict([[2026]])


# In[ ]:




