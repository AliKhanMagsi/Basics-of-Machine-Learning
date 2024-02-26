#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[6]:


year = [2000, 2005, 2010, 2020]

pop = ['1B','2B','4B','6B']


# In[16]:


plt.plot(year,pop)
plt.show()


# In[17]:


plt.hist(pop, bins=6)
plt.show()


# In[18]:


#customizing the chart
plt.plot(year,pop)
plt.show()


# In[20]:


plt.plot(year, pop)
plt.xlabel("years")
plt.ylabel("population")
plt.title("world population development")
plt.show()


# In[26]:





# In[ ]:





# In[ ]:




