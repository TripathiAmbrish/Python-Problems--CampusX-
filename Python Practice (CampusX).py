#!/usr/bin/env python
# coding: utf-8

# Solution1:

# In[1]:


# Take input from the user
x = int(input('Enter first age: '))
y = int(input('Enter second age: '))
z = int(input('Enter third age: '))

# Find the oldest
oldest = x
if oldest < y:
    oldest = y
if oldest < z:
    oldest = z

# Display the oldest
print("The oldest age is:", oldest)


# solution2:

# In[5]:


#let C be celcius
C = int(input('Enter celcius value: '))
F = (C*(9/5)) + 32
print(F, 'F')


# solution3:

# In[11]:


x = int(input('Enter first no.: '))
y = int(input('Enter second no.: '))

print(y, x)


# In[19]:


a = int(input('1st digit: '))
b = int(input('2nd digit: '))
c = int(input('3rd digit: '))

print('sum of three digits is ', a+b+c)


# In[ ]:




