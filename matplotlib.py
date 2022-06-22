#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install matplotlib     #to install matplotlib


# In[4]:


import matplotlib.pyplot as plt


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline   # graph bnana k liye zarori ha')


# import numpy as np

# In[9]:


import numpy as np


# In[14]:


x=np.linspace(0,5,11)     #linspace 0 se 5 tak 11 values generate karega
x


# In[15]:


y=x**2
y


# In[22]:


plt.plot(x,y,'c')   # x aur y k dermyan graph


# In[23]:


plt.xlabel('time')
plt.ylabel('velocity')


# In[25]:


plt.plot(x,y,'c')
plt.xlabel('time')
plt.ylabel('velocity')
plt.title('v-t graph')    #graph ko name dega


# In[41]:


z=np.linspace(0,100,11)    # z new variable ha 11 values ka  
plt.subplot(1,2,1)    #   brackket ma (size,total graph,  graph no.)    
plt.plot(x,z,'c')
plt.subplot(1,2,2)
plt.plot(y,z,'r')


# In[42]:


#   fig.savefig('fileame.png')     # pehla fig object ha,  png ki jaga jpg bhi extension de sakte ha 

#  fig.savefig('filename.png' , dpi=200)  # dpi ma resolutioin dekar save karwaya ha


# In[43]:


ax.set_tiltle('title')


# In[ ]:




