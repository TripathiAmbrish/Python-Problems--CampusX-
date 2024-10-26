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


# solution8:

# In[8]:


import math

x = int(input("Enter x: "))
y = int(input("Enter y: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

euc_dis = math.sqrt((x - a)**2 + (y - b)**2)
euc_dis = round(euc_dis,2)
print("Euclidean distance is ",euc_dis)


# solution9:

# In[1]:


#angles
a = int(input("Enter the angle: "))
b = int(input("Enter the angle: "))
c = int(input("Enter the angle: "))

if a+b+c == 180:
    print("abc is a triangle")
else:
    print("abc is not a triangle")


# In[4]:


s_p = int(input("Enter the selling price: "))
c_p = int(input("Enter the cost price: "))

if s_p - c_p > s_p:
    print("Profit of ",s_p-c_p)
else:
        print("Loss of",abs(s_p-c_p))


# In[6]:


P = int(input("Enter Principle: "))
R = int(input("Enter Rate of interest: "))
T = int(input("Enter time: "))

SI = round(P*R*T/100,2)
print(SI)


# In[ ]:





# In[ ]:




