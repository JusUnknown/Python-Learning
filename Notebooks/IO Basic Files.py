#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'Derpy Derp Derp\nBlah blah blah')


# In[2]:


myfile = open('myfile.txt')


# In[3]:


myfile = open('epic.txt')


# In[4]:


pwd


# In[5]:


myfile = open('myfile.txt')


# In[6]:


myfile.read()


# In[7]:


myfile.read()


# Nothing left to read, reset back to the start always use .seek(0)

# In[12]:


myfile.seek(0)


# In[9]:


myfile.read()


# In[14]:


contents = myfile.read()


# In[15]:


contents


# In[16]:


myfile.seek(0)


# In[17]:


myfile.readlines()


# In[18]:


myfile.close()


# In[21]:


with open ('myfile.txt') as my_new_file:
        contents=my_new_file.read()


# In[22]:


contents


# In[23]:


with open('myfile.txt',mode='r') as myfile:
    contents = myfile.read()


# , w for write-only , a for append-only, r for read-only, r+ for reading and writing, w+ for writing and reading (Overwrites exisiting files/creates a new file)

# In[25]:


with open('myfile.txt',mode='w') as myfile:
    contents = myfile.read()


# In[26]:


get_ipython().run_cell_magic('writefile', 'my_new_file.txt', '')


# In[27]:


get_ipython().run_cell_magic('writefile', 'my_new_file.txt', 'ONE ON FIRST\nTWO ON SECOND\nTHREE ON THIRD')


# In[30]:


with open('my_new_file.txt', mode='r') as f:
    print(f.read())


# In[31]:


with open('my_new_file.txt', mode ='a') as f:
    f.write('FOUR ON FOURTH')


# In[32]:


with open('my_new_file.txt', mode='r') as f:
    print(f.read())


# In[33]:


with open('pineapples.txt',mode='w') as f:
    f.write('PINEAPPLES ARE THE BEST')


# In[34]:


with open('pineapples.txt',mode='r') as f:
    print(f.read())


# In[ ]:




