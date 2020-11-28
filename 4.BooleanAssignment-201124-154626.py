#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Q. ​Declare a boolean value and store it in a variable. Check the type and print the id of the same. 

a = 1
print(a, type(a), id(a))


# In[22]:


# Take one boolean value between 0 - 256. Assign it to two different variables. Check the id of both the variables. 
# It should come the same. Check why? 

a = 0
b = 0

print(id(a))
print(id(b))


# In[16]:


# 3. Take one float value either less than -5 or greater than 256. Assign it to two different variables.
# Check the id of both the variables. It should come different.Check why? 

a = 256.50
b = 256.50

print(id(a))
print(id(b))


# In[8]:


#4. Arithmetic Operations on integers Take two different boolean values. Store them in two different variables. 

# Do below operations on them:-  
# Find sum of both numbers   
# Find difference between them  
# Find the product of both numbers.  
# Find value after dividing first num with second number   
# Find the remainder after dividing first number with second number 
# Find the quotient after dividing first number with second number  
# Find the result of the first num to the power of the second number. 2

x=40
y=50
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x // y)
print(x ** y)


# In[7]:


#5 Comparison Operators on boolean Take two different integer values. Store them in two different variables. 
# Do below operations on them:-   
# Compare se two numbers with below operator:-    
#     Greater than, '>'      
#     Smaller than, '<'      
#     Greater than or equal to, '>='      
#     Less than or equal to, '<=' 
#     Observe their output(return type should be boolean) 

x=10
y=20
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# In[6]:


# 6.Equality Operator Take two different boolean values. Store them in two different variables. 
# Equate them using equality operators (==, !=) 
# Observe the output(return type should be boolean) 


x=True
y=False
print(x == y)
print ( x != y)


# In[5]:


# Logical operators Observe the output of below code Cross check the output manually 
print(True and True) #----------------------------------------->Output is True 
print(False and True) #----------------------------------------->Output is False 
print(True and False) #----------------------------------------->Output is False 
print(False and False) #----------------------------------------->Output is False 
print(True or True) #----------------------------------------->Output is True 
print(False or True) #----------------------------------------->Output is True 
print(True or False) #----------------------------------------->Output is True 
print(False or False) #----------------------------------------->Output is False 
print(not True) #----------------------------------------->Output is False 
print(not False) #----------------------------------------->Output is True 


# In[4]:


# Q.​ Bitwise Operators Do below operations on the values provided below:-    
# Bitwise and(&) --------------> True, True   -------> Output is True    
# Bitwise or(|)  --------------> True, False   -------> Output is True    
# Bitwise(^)     --------------> True, False   -------> Output is True    
# Bitwise negation(~) ---------> True          -------> Output is -2    
# Bitwise left shift  ---------> True,2        -------> Output is 4    
# Bitwise right shift ---------> True,2        -------> Output is 0 Cross check the output manually 
 
print(True & True)
print(True | False)
print(True ^ False)
print(~True)
print(True << 2)
print(True >> 2)


# In[2]:


# What is the output of expression inside the print statement. 
# Cross check before running the program.
a = True 
b = True 
print(a is b)          #True or False?   # 
print(a is not b)      #True or False? 
a = False
b = False 
print(a is b)          #True or False? print(a is not b)      #True or False? 


# In[1]:


# Q Membership operation in, not in are two membership operators and it returns boolean value 
print(True in [10,10.20,10+20j,'Python', True]) 
print(False in (10,10.20,10+20j,'Python', False))
print(True in {1,2,3, True}) 
print(True in {True:100, False:200, True:300}) 
print(False in {True:100, False:200, True:300}) 


# In[ ]:




