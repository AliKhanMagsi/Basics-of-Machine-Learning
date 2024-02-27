#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


from sklearn.datasets import load_digits
digits=load_digits()


# In[5]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(digits.data,digits.target, test_size=0.3)


# In[6]:


lr=LogisticRegression()
lr.fit(x_train,y_train)
lr.score(x_test,y_test)


# In[7]:


svm=SVC()
svm.fit(x_train,y_train)
svm.score(x_test,y_test)


# In[8]:


rf=RandomForestClassifier()
rf.fit(x_train,y_train)
rf.score(x_test,y_test)


# In[9]:


from sklearn.model_selection import KFold
kf=KFold(n_splits=3)
kf


# In[10]:


for train_index,test_index in kf.split([1,2,3,4,5,6,7,8,9]):
    print(train_index,test_index)


# In[11]:


def get_score(model,x_train,x_test,y_train,y_test):
    model.fit(x_train,y_train)
    return model.score(x_test,y_test)


# In[13]:


from sklearn.model_selection import StratifiedKFold
folds=StratifiedKFold(n_splits=3)


# In[40]:


score_l=[]
score_svm=[]
score_rf=[]
for train_index,test_index in kf.split(digits.data):
    x_train,x_test,y_train,y_test=digits.data[train_index],digits.data[test_index], digits.target[train_index],digits.target[test_index]
                            
    score_l.append(get_score(LogisticRegression(),x_train,x_test,y_train,y_test))
    score_svm.append(get_score(SVC(),x_train,x_test,y_train,y_test))
    score_rf.append(get_score(RandomForestClassifier(),x_train,x_test,y_train,y_test))


# In[41]:


score_l


# In[42]:


score_svm


# In[43]:


score_rf


# In[44]:


from sklearn.model_selection import cross_val_score #instead of using above loop code to store in array we can import this model
cross_val_score(LogisticRegression(), digits.data,digits.target)


# In[ ]:




