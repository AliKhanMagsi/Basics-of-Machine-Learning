#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
from sklearn.datasets import load_digits
digits=load_digits()


# In[41]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[42]:


plt.gray()
for i in range(4):
    plt.matshow(digits.images[i])


# In[43]:


df=pd.DataFrame(digits.data)
df.head()


# In[44]:


df['target']=digits.target #creating new columns
df.head()


# In[45]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df.drop(['target'],axis='columns'),digits.target, test_size=0.2)


# In[46]:


from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()


# In[47]:


model.fit(x_train,y_train)


# In[48]:


model.score(x_test,y_test)


# In[49]:


y_predict=model.predict(x_test)


# In[50]:


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predict)


# In[51]:


cm


# In[52]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm,annot=True)
plt.xlabel('predict')
plt.ylabel('Truth')


# In[ ]:




