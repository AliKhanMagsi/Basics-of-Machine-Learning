#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[46]:


df=pd.read_csv('F:\\5th Semester\\ML\\Python\\Home_Price\\Book1.csv')
df


# In[47]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(df.area,df.price, color='black', marker='*')


# In[48]:


reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)


# In[49]:


reg.predict([[4300]])


# In[64]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(df.area,df.price, color='black', marker='*')
plt.plot(df.area,reg.predict(df[['area']]), color='blue')


# In[50]:


print('Task2..........')


# In[51]:


d=pd.read_csv('F:\\5th Semester\\ML\\Python\\Home_Price\\area\\Book1.csv')


# In[52]:


d.head()


# In[53]:


p=reg.predict(d)


# In[54]:


d['price']=p


# In[55]:


d


# In[59]:


d.to_csv("pridection.csv", index=False)


# In[ ]:




