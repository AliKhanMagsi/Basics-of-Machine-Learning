#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits


# In[7]:


digit=load_digits()


# In[8]:


dir(digit)


# In[9]:


digit.data[0]


# In[10]:


plt.gray()
plt.matshow(digit.images[1])


# In[11]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(digit.data,digit.target, test_size=0.2)


# In[12]:


from sklearn.linear_model import LogisticRegression
reg=LogisticRegression()


# In[13]:


reg.fit(x_train,y_train)


# In[14]:


reg.score(x_test,y_test)


# In[15]:


reg.predict(digit.data[0:5])


# In[17]:


y_predict=reg.predict(x_test)
from sklearn.metrics import confusion_matrix


# In[19]:


cm=confusion_matrix(y_test,y_predict)
cm


# In[24]:


import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm,annot=True)
plt.xlabel('predict')
plt.ylabel('Truth')


# In[ ]:




