#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[34]:


df = pd.read_csv("C:/Users/ALI/Desktop/numpy and pandas/Employee Hiring Prediction/employeeData.csv")

df


# In[35]:


plt.scatter(df.Exp, df.written_Test, df.interview_score)
plt.xlabel("Experience")
plt.ylabel("score (out of 10)")


# In[36]:


reg = linear_model.LinearRegression()
reg.fit(df[["Exp", "written_Test", "interview_score"]], df.salary)


# In[43]:


reg.predict([[10,10,10]])


# In[ ]:




