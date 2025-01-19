#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random

score = 0

side = ["heads","tails"]

question = str(input("Do you want to play the coin flip game?"))

while question == "YES":
    chosen_side = random.choice(side)
    print(chosen_side)
    
    guess = str(input("Is the side heads or tails?"))
    
    if guess == chosen_side:
        score+=1
        print("congrats! You got the side correct!")
        
    question = (str(input("Do you want to play the coin flip game?")))
        
print(score)


# In[ ]:




