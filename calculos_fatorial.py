#!/usr/bin/env python
# coding: utf-8

# In[8]:


# recursão

def fatorial(n):
    if n == 0:
        return 1
    
    return n * fatorial(n - 1)


# In[10]:


fatorial(5)


# In[20]:


# laço for

def fatorialFor(n):
    if n == 0:
        return 1
    
    fatorial = 1
    
    for num in range(1, n+1):
        fatorial *= num
    
    return fatorial


# In[21]:


fatorialFor(5)


# In[28]:


# laço while

def fatorialWhile(n):
    if n == 0:
        return 1
    
    fatorial = 1
    
    while n != 1:
        fatorial *= (n + 1) - 1
        n -= 1
    
    return fatorial


# In[32]:


fatorialWhile(5)


# In[ ]:




