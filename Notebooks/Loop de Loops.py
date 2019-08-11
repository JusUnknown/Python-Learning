#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[7]:


for num in mylist:
    print('hello');


# In[12]:


for num in mylist:
#Is it even?
    if num % 2 == 0:
        print('num')
    else:
        print(f'Odd Number: {num}')


# In[14]:


list_sum = 0

for num in mylist:
    list_sum = list_sum + num
    
print(list_sum)


# In[16]:




for letter in 'Hello World':
    print(letter)


# In[17]:


tup = (1,2,3)

for item in tup:
    print(item)


# In[18]:


mylist = [(1,2),(3,4),(5,6),(7,8)]


# In[19]:


len(mylist)


# In[20]:


for item in mylist:
    print(item)


# In[21]:


for (a,b) in mylist:
    print(a)
    print(b)


# In[22]:


for a,b in mylist:
    print(b)


# In[23]:


mylist = [(1,2,3),(5,6,7),(8,9,10)]


# In[25]:


for a,b,c in mylist:
    print(item)


# In[26]:


for a,b,c in mylist:
    print(b)


# In[27]:


d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)


# In[29]:


d = {'k1':1,'k2':2,'k3':3}
for item in d.items():
    print(item)


# In[30]:


d = {'k1':1,'k2':2,'k3':3}
for value in d.values():
    print(value)


# In[ ]:




