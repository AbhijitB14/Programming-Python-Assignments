#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Write a Python program to print "Hello Python"?


# In[1]:


print("Hello Python")


# In[ ]:


2. Write a Python program to do arithmetical operations addition and division.?


# In[2]:


a = 10
b = 2

## Addition
add = a + b
## Division
div = a/b

print(add)
print(div)


# In[ ]:


get_ipython().set_next_input('3. Write a Python program to find the area of a triangle');get_ipython().run_line_magic('pinfo', 'triangle')


# In[3]:


height = 100
base = 25

area = height*base/2

print("Area of triangle:", area)


# In[ ]:


get_ipython().set_next_input('4. Write a Python program to swap two variables');get_ipython().run_line_magic('pinfo', 'variables')


# In[4]:


var1 = 123
var2 = 111

print('Before swap:\nvar1 = {} and var2 = {}'.format(var1, var2))

temp = var1
var1 = var2
var2 = temp
print('\nAfter swap:\nvar1 = {} and var2 = {}'.format(var1, var2))


# In[ ]:


get_ipython().set_next_input('5. Write a Python program to generate a random number');get_ipython().run_line_magic('pinfo', 'number')


# In[5]:


import random

print(random.random())
print(random.randint(1, 1000))

