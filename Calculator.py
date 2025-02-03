#!/usr/bin/env python
# coding: utf-8

# In[22]:



def division(n1,n2): # division function
    res = round(n1/n2,2)
    return res

def multiplication(n1,n2): # multiplication function
    res = round(n1*n2)
    return res

def addition(n1,n2): # addition function
    res = round(n1+n2,2)
    return res

def subtraction(n1,n2): # subtraction function
    res = round(n1-n2,2)
    return res


num1 = float(input("Enter the first number: ")) # first number

num2 = float(input("Enter the second number: ")) # second number


operation = str(input("Enter the type of operation you wish to complete: division(/), multiplication(*), addition(+), subtraction(-)")) #ask the user what type of operation they wish to perform

if operation == "/": # calls divsion function
    res = division(num1,num2)
    
elif operation == "*": # calls multiplication function
    res = multiplication(num1,num2)
    
elif operation == "-": # calls subtraction function
    res = subtraction(num1,num2)

elif operation == "+": # calls addition function
    res = addition(num1,num2)

else: # if the user doesn't enter valid input
    print("invalid input")
    
print(res) # print statement to check if the operations are happening correctly
    
    
question = str(input("Do you want to continue this calculation? (yes) or (no)")) # asks the user if they wish to continue arithmetic

while question == "yes":
    n = float(input("Enter the value: ")) # prompts the user for the new value
    operation = str(input("Enter the type of operation: ")) # asks the user what type of operation they wish to perform
    
    if operation == "/": # calls division function
        res = division(res,n)
        
    elif operation == "*": # calls multiplication function
        res = multiplication(res,n)
        
    elif operation == "-": # calls subtraction function
        res = subtraction(res,n)
        
    elif operation == "+": # calls addition function
        res = addition(res,n)
        
    else: # called when there is an input error
        print("input error")
        
    question = str(input("Do you want to continue this calculation? (yes) or (no)")) # prompts the user if they wish to continue to stay in the while loop and perform another operation
     

print(res) # prints the final result
    
    


# In[ ]:





# In[ ]:




