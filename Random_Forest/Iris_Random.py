#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.datasets import load_iris
iris=load_iris()


# In[5]:


df=pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()


# In[6]:


df['target']=iris.target


# In[7]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df.drop(['target'],axis='columns'),iris.target,test_size=0.2)


# In[8]:


from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(x_train,y_train)


# In[9]:


model.score(x_test,y_test)

