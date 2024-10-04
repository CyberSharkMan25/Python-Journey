#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# a while loop is an infinite loop that functions with a boolean (true/false value)

# Here is a simple example

i = int(input("Enter a number: ")) # prompts the uesr to enter an integer

while i > 0: # if the user enters a number above 0, the loop continues
    print("You are still in the loop")
    i = int(input("Enter a number: ")) # reprompts the user to enter a number and they remain in the loop if they enter a number above 0


# In[ ]:


# Let's use the while loop to find the max value entered by the user

i = int(input("Enter a number: "))

Max = 0 # make sure to make the Max variable uppercase, max will call the max function

while i != 0:
    if i > Max:
        Max = i
        print("The max is", Max)
    i = int(input("Enter a number: "))


# In[ ]:




