#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random

options = ["ROCK", "PAPER", "SCISSORS"]

user_score = 0

computer_score = 0

A = str(input("Do you want to play? "))

question = A.upper()

while question == "YES":
    
    computer = random.choice(options)
    print(computer)
    
    B = str(input("Enter rock, paper, or scissors"))
    user = B.upper()

    print("Rock..paper...scissors...shoot\n")
    
    if computer == "ROCK" and user == "SCISSORS":
        print("Darn, the computer won\n")
        computer_score +=1
    
    elif computer == "SCISSORS" and user == "PAPER":
        print("Darn, the computer won\n")
        computer_score +=1

    elif computer == "PAPER" and user == "ROCK":
        print("Darn, the computer won\n")
        computer_score +=1
        
    elif computer == "SCISSORS" and user == "ROCK":
        print("You win!\n")
        user_score +=1
        
    elif computer == "ROCK" and user == "PAPER":
        print("You win!\n")
        user_score +=1
    
    elif computer == "PAPER" and user == "SCISSORS":
        print("You win!\n")
        user_score +=1
        
    elif computer == "SCISSORS" and user == "SCISSORS":
        print("Tie\n")
        
    elif computer == "ROCK" and user == "ROCK":
        print("Tie\n")
        
    elif computer == "PAPER" and user == "PAPER":
        print("Tie\n")
    
    else:
        print("input error. Please try again.\n")
    
        
    print("The user's score is", user_score)
    
    print("The computer's score is", computer_score)
    
    A = str(input("Do you want to play? "))

    question = A.upper()


# In[ ]:




