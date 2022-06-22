#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install numpy


# In[5]:


import numpy as np


# In[9]:


arr=np.arange(20,31) #20 se 30 tak value hogi
arr


# In[10]:


arr[2]  # index 2 k element ko dega


# In[14]:


arr[:6]  # start se index 5 tak ki value milagi 6 se aik kam  index tak


# In[15]:


arr[5:]  #5 se end tak sari values dega array ki


# In[17]:


#braodcasting
arr[0:5]=92    #pehli 4 values ko 92 aassign kardega
arr


# In[19]:


arr[8:]=34   #last two values ko 34 assign karega
arr


# In[21]:


arr_copy=np.copy(arr)  #arr ki copy array bnagi 
arr_copy


# In[ ]:




