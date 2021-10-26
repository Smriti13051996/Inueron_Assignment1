#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program to print the numbers divisible by 7 but are not a multiple of 5 in range 2000 to 3200 (both included):
def print_divisible():
    for num in range(2000,3201):
        if (num%5)!=0:
            if (num%7)==0:
                print(num,end=",")
print_divisible()


# In[6]:


#Program to accept user's first & last name an print them in reverse order with a space between first an last name:
def reverse_name():
    first=input("Enter your first name:")
    last=input("Enter your last name:")
    reverse_first=""
    reverse_last=""
    for count in range(len(first)-1,-1,-1):
        reverse_first=reverse_first+first[count]
    for count in range(len(last)-1,-1,-1):
        reverse_last=reverse_last+last[count]
    print(reverse_first," ",reverse_last)
reverse_name()


# In[8]:


#Program to find volume of sphere with diameter 12cm:
def volume_sphere():
    diameter=12
    radius=diameter/2
    volume=(4/3)*(22/7)*(radius**3)
    return volume
volume_sphere()


# In[ ]:




