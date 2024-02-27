#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# In[24]:


a = np.array([[1,2,3],[2,3,4]], dtype=("int32"))
print(a)


# In[17]:


a.ndim


# In[18]:


a.shape


# In[25]:


a.itemsize


# In[26]:


a.itemsize


# In[34]:


#all 1s matrices
np.ones([3,3,3], float)


# In[36]:


#all 0s matrices
np.zeros([3,2,2], int)


# In[41]:


#customized number
np.full([3,2,2], 5)


# In[60]:


#random matrices of integer value
#4,7 is range and size is order of matrix
np.random.randint(4,7, size=(2,2))


# In[64]:


#identity matrix
np.identity(3)


# In[76]:


#mathematical operation on array with numpy

a = np.array([1,2,4,5])
b = 2 


#you can perfom all these mathematical operations on numpy.......

a+b
a-b
a*b
a/b
a**b
np.sin(a)
np.cos(a)
np.tan(a)


# In[109]:


#loading data from files...
np.genfromtxt("C:\\Users\\ALI\\Desktop\\Numpy\\numpy\\DataTobeLoad.txt", delimiter=",")



# In[111]:


#you can convert above data into integer form..
data = data.astype("int32")
data



# In[ ]:




