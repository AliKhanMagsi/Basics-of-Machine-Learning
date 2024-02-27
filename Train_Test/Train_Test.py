#!/usr/bin/env python
# coding: utf-8

# In[96]:


import pandas as pd


# In[97]:


df=pd.read_csv('F:\\5th Semester\\ML\\Python\\Train_Test\\Book1.csv')
df.head()


# In[98]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[99]:


plt.scatter(df['Mileage'],df['SellPrice'])


# In[100]:


x=df[['Mileage','Age']]
y=df[['SellPrice']]


# In[101]:


x


# In[102]:


y


# In[103]:


from sklearn.model_selection import train_test_split


# In[104]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


# In[105]:


from sklearn.linear_model import LinearRegression
reg=LinearRegression()


# In[106]:


reg.fit(x_train,y_train)


# In[107]:


reg.predict(x_test)


# In[108]:


y_test


# In[109]:


reg.score(x_test,y_test)

