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

# In[2]:


#let C be celcius
C = int(input('Enter celcius value: '))
F = (C*(9/5)) + 32
F = round(F, 2)
print(F, 'F')


# solution3:

# In[3]:


x = int(input('Enter first no.: '))
y = int(input('Enter second no.: '))

print(y, x)


# solution4:

# In[4]:


a = int(input('1st digit: '))
b = int(input('2nd digit: '))
c = int(input('3rd digit: '))

print('sum of three digits is ', a+b+c)


# solutiob5:

# In[5]:


four_dig_num = int(input('Enter a four digit nunber: '))

reversed_num = int(str(four_dig_num)[::-1])
print(reversed_num)

if four_dig_num != reversed_num:
    print(True)
else:
    print(False)


# solution6:

# In[6]:


num = int(input('Enter a number: '))

if num % 2 == 0:
    print(num,' is even')
else:
    print(num,' is odd')


# solution7:

# In[9]:


year = int(input('Enter a year: '))

if year / 4 and not year / 100:
    print(year, ' is a leap year.')
else:
    print(year, ' not a leap year.')


# In[ ]:





# In[ ]:





# In[ ]:




