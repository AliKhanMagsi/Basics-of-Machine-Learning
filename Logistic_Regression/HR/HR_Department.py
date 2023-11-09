#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd


# In[86]:


df=pd.read_csv('F:\\5th Semester\\ML\\Python\\Logistic_Regression\\HR\\HR_comma_sep.csv')
df


# In[87]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
pd.crosstab(df.salary,df.left).plot(kind='bar')


# In[88]:


pd.crosstab(df.Department,df.left).plot(kind='bar')


# In[89]:


subdf = df[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]
subdf.head()


# In[90]:


salary_dummies = pd.get_dummies(subdf.salary, prefix="salary")


# In[91]:


df_with_dummies = pd.concat([subdf,salary_dummies],axis='columns')


# In[92]:


df_with_dummies.head()


# In[93]:


df_with_dummies.drop('salary',axis='columns',inplace=True)
df_with_dummies.head()


# In[94]:


X = df_with_dummies
X.head()


# In[95]:


y = df.left


# In[96]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)


# In[97]:


from sklearn.linear_model import LogisticRegression
reg = LogisticRegression()


# In[98]:


reg.fit(X_train, y_train)


# In[99]:


reg.predict(X_test)


# In[100]:


reg.score(X_test,y_test)


# In[ ]:




