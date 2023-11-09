#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt


# In[8]:


df=pd.read_csv('F:\\5th Semester\\ML\\Python\\Logistic_Regression\\Insurance\\insurance_data.csv')
df.head()


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df.age,df.bought_insurance)


# In[13]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df[['age']],df.bought_insurance, test_size=0.1)


# In[14]:


from sklearn.linear_model import LogisticRegression
reg=LogisticRegression()


# In[15]:


reg.fit(x_train,y_train)


# In[18]:


reg.predict(x_test)


# In[23]:


reg.score(x_test,y_test)


# In[ ]:




