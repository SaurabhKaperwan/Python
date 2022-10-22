#!/usr/bin/env python
# coding: utf-8

# ## Numpy

# In[1]:


import numpy as np


# In[2]:


np1=np.array([1,2,3,4])


# In[3]:


np1


# In[4]:


type(np1)


# In[6]:


Mat1=np.array([[1,2],[3,4]])


# In[7]:


Mat1


# In[8]:


np1.shape


# In[9]:


Mat1.shape


# In[10]:


Mat1.dtype


# In[12]:


Mat1[0,0]=5


# In[13]:


Mat1


# In[15]:


Mat2=np.arange(0,10,1)


# In[16]:


Mat2


# In[17]:


Mat3=np.linspace(0,10,20)


# In[18]:


Mat3


# In[19]:


Mat3.shape


# In[20]:


Mat4=np.random.rand(5,5)


# In[21]:


Mat4


# In[22]:


Mat5=np.random.randn(5,5)


# In[23]:


Mat5


# In[24]:


Mat5[0,0]


# In[25]:


Mat5[0,1]


# In[26]:


Mat5[0:3,:]


# In[ ]:




