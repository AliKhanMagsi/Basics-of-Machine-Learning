#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('F:\\5th Semester\\ML\\Python\\Logistic_Regression(MultiClass)\\Iris\\Iris.csv')
df


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 


# In[5]:


plt.scatter(df.SepalLengthCm,df.SepalWidthCm,df.PetalLengthCm,df.PetalLengthCm)


# In[6]:


x=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalLengthCm']]
y=df[['Species']]


# In[7]:


from sklearn.model_selection import train_test_split


# In[8]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


# In[12]:


from sklearn.linear_model import LogisticRegression
reg=LogisticRegression()


# In[13]:


reg.fit(x_train,y_train)


# In[15]:


reg.predict(x_test)


# In[16]:


reg.score(x_test,y_test)


# In[ ]:




