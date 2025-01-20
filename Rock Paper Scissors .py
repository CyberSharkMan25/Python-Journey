#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random #imports the random library

options = ["ROCK", "PAPER", "SCISSORS"] #creates a list of the three options: Rocks, Paper, and Scissors

user_score = 0 #sets user score

computer_score = 0 #sets computer score

A = str(input("Do you want to play? ")) #prompts the user if they want to play the game

question = A.upper() #converts all user input to uppercase to prevent case sensitivity issues

while question == "YES": #a while loop checks to see if the user wants to play and begins the game if they say "yes"
    
    computer = random.choice(options)
    print(computer) # shows the random choice for the computer. Note that this is used to check if the score output using the conditional statements is correct
    
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
    
        
    print("The user's score is", user_score) #prints the user's final score
    
    print("The computer's score is", computer_score) #prints the computer's final score
    
    A = str(input("Do you want to play? ")) #asks the user if they want to play the game again

    question = A.upper()


# In[ ]:




