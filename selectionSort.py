#!/usr/bin/env python
# coding: utf-8

# # Selection Sort

# In[7]:


import random as rnd
import numpy as np


# In[8]:


def create_list(x):
    list_1 = []
    for i in range(x):
        e = rnd.randint(-30,30)
        list_1.append(e)
    return list_1


# In[9]:


list_1 = create_list(10)
list_1


# In[10]:


for i in range(len(list_1)):
    mini = list_1[i]
    for j in range(i+1,len(list_1)):
        if list_1[j] < mini:
            mini = list_1[j]
            list_1[j] = list_1[i]
            list_1[i] = mini
            


# In[11]:


list_1


# In[ ]:




