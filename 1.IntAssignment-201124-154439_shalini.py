#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Q. ​Declare an int value and store it in a variable. Check the type and print the id of the same.

a=10
print(a,type(a)) #to print the type of variable
print(int(10))
id(a) #to check the id of variable


# In[20]:


# 2.Take one int value between 0 - 256. Assign it to two different variables. Check the id of both the variables. 
# It should come the same. Check why?

c=50
d=50
print("c",id(c))
print("d",id(d))


# If value is with in range of 0 to 256 then id will be same.


# In[21]:


# 3. Take one int value either less than -5 or greater than 256. Assign it to two different variables.
# Check the id of both the variables. It should come different.Check why? 

a=-2
b=257
print(id(a), id(b))

# If value is beyond 256 that means not in range  of 0 to 256 then id will differ.


# In[4]:


#4. Arithmetic Operations on integers Take two different integer values. Store them in two different variables. 

# Do below operations on them:-  
# Find sum of both numbers   
a=5
b=6
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b) 


# Find difference between them  
# Find the product of both numbers.  
# Find value after dividing first num with second number   
# Find the remainder after dividing first number with second number 
# Find the quotient after dividing first number with second number  
# Find the result of the first num to the power of the second number. 


# In[29]:


#5 Comparison Operators on integers Take two different integer values. Store them in two different variables. 
# Do below operations on them:-   
# Compare se two numbers with below operator:-    
#     Greater than, '>'      
#     Smaller than, '<'      
#     Greater than or equal to, '>='      
#     Less than or equal to, '<=' 
#     Observe their output(return type should be boolean) 

a=10
b=20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


# In[31]:


# 6.Equality Operator Take two different integer values. Store them in two different variables. 
# Equate them using equality operators (==, !=) 
# Observe the output(return type should be boolean) 

x=5
y=10
print(x==y)
print(x!=y)


# In[13]:


# 7. Logical operators Observe the output of below code 
# Cross check the output manually 
#  print​(​10​ ​and​ ​20​) #----------------------------------------->Output is 20
#  print​(​0​ ​and​ ​20​) #----------------------------------------->Output is 0 
# print​(​20​ ​and​ ​0​) #----------------------------------------->Output is 0 
# print​(​0​ ​and​ ​0​) #----------------------------------------->Output is 0 
#  print​(​10​ ​or​ ​20​) #----------------------------------------->Output is 10 
# print​(​0​ ​or​ ​20​) #----------------------------------------->Output is 20
#  print​(​20​ ​or​ ​0​) #----------------------------------------->Output is 20 
# print​(​0​ ​or​ ​0​) #---------------------------------------->Output is 0 
#  print​(​not​ ​10​) #----------------------------------------->Output is False 
# print​(​not​ ​0​) #----------------------------------------->Output is True b


print(10 and 20) 
print(0 and 20) #if one operand is 0 then o/p is 0
print(20 and 0)
print(0 and 0)
print(10 or 20) #if first operand "or"  expression is True it returns the first operand otherwise it returns second
print(0 or 20) #if first operand "or"  expression is True it returns the first operand otherwise it returns second
print(20 or 0)
print(0 or 0)
print(not 20)
print(not 0)


# In[64]:


# 8. Bitwise Operators Do below operations on the values provided below:-  
#  Bitwise and(&) -----------------------------------------> 10, 20 -------> Output is 0  
#  Bitwise or(|)  -----------------------------------------> 10, 20 -------> Output is 30 
#  Bitwise(^)     -----------------------------------------> 10, 20 -------> Output is 30  
#  Bitwise negation(~) ------------------------------------> 10 -------> Output is -11   
#  Bitwise left shift  ------------------------------------> 10,2 -------> Output is 40   
#  Bitwise right shift ------------------------------------> 10,2 -------> Output is 2 
#  Cross check the output manually 
 
# print(10 & 20)  #if a & b find the binary value of 10 and 20


a = print("a",bin(10))
b = print("b",bin(20))


b=0b10100
a=0b1010

print(a & b)
print(a | b)
print(a ^ b)
print(~a)

x=10
y=2

c = print("x", bin(x))
d = print("y", bin(y))

print(x<<y)


print(x>>y)
print(int(0b10))

print(10<<2)

# print(10|20) 
# print(10^20)
# print(~10)
# print(10<<2)
# print(10>>2)


# In[33]:


# 9 What is the output of expression inside print statement.
#  Cross check before running the program. 
# a = 10 b = 10 print(a is b) #True or False? 
#print(a is not b)      #True or False? 
# a = 1000 b = 1000 print(a is b)  #True or False? 
#print(a is not b)      #True or False? 

a = 10 
b = 10
print(a is b)
print(a is not b) 

print(id(a))
print(id(b))
a = 1000 
b = 1000 
print(a is b) 
print(a is not b) 
print(id(a))
print(id(b))




# In[56]:


#  10 What is the output of expression inside print statement. Cross check before running the program. 
#     print​(​10​+(​10​*​32​)//​2​**​5​&​20​+(~(​-10​))<<​2​)


print(10+(10*32)//2**5&20+(~(-10))<<2)


# In[72]:


# 11 Q.Membership operation in, not in are two membership operators and it returns boolean value 
print('2' in 'Python2.7.8')
print(10 in [10,10.20,10+20j,'Python'])
print(10 in (10,10.20,10+20j,'Python'))
print(2 in {1,2,3}) 
print(3 in {1:100, 2:200, 3:300})
print(10 in range(20)) 


# In[18]:


# 12 An integer can be represented in binary, octal or hexadecimal form. Declare one binary, one octal 
# and one hexadecimal value and store them in three different variables. Convert 9876 to its binary, octal
# and hexadecimal equivalent and print their corresponding value. 
 


num1 = 100
num2 = 200
num3 = 300

print(bin(num1))
print(oct(num2))
print(hex(num3))

num_bin = bin(num1)
num_oct = oct(num2)
num_hex = hex(num3)

print(num_bin)
print(num_oct)
print(num_hex)


print(bin(9876))
print(oct(9876))
print(hex(9876))


# In[19]:


# 13  What will be the output of following:-

a = 0b1010000 
print(a) 

b = 0o7436 
print(b) 

c = 0xfade 
print(c) 

print(bin(80)) 
print(oct(3870)) 
print(hex(64222)) 
print(bin(0b1010000)) 
print(bin(0xfade)) 
print(oct(0xfade)) 
print(oct(0o7436)) 
print(hex(0b1010000)) 
print(hex(0xfade)) 
 


# In[ ]:




