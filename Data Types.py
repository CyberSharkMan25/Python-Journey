#!/usr/bin/env python
# coding: utf-8

# In[12]:


a = 5 # a is set equal to an integer value
# an integer value must be a whole number i.e 1,2,333,100
# 5.6,3.3,9.9999999999 are not integers
type(a) # outputs the type of value 


# In[13]:


b = "Bob" # b is a string variable 
# a string variable is enclosed in double quotes ("") or single quotes ('') in python
# Note: other programming languages such as java don't allow strings to be enclosed in single quotes
type(b) # returns the variable type as a string


# In[14]:


c = 5.6 # c is a float value meaning it is not a whole number
type(c) # returns the variable type as float


# In[15]:


d = [1,2,3,4,5] # d is set equal to a list in python
type(d) # returns the data type of d as list.


# In[17]:


e = {"IBM":"Tech","Amazon":"E-commerce"} # e is a dictionary that stores values in key-value pairs. 
# for example {"football":5} could be a key value pair that says that there are 5 people (value) who play football
type(e) # returns the data type as dictionary


# In[18]:


f = (1,2,3,4,4) # sets the variable f to a tuple
# Note: tuples can have duplicate values e.g (1,1,2,3,4,5)
type(f) # returns the data type as variable


# In[20]:


g = {1,2,3,3,4,5} # g is a set of values
# Note: a set cannot repeat any values
type(g)
print(g) # notice that even though 3 appears twice in the initial set, when the set is printed, 3 only appears once


# In[ ]:




