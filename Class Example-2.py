#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Car: # creates the class named "Car"
    
    def __init__(self, make, model, year): #gets the variables that can make up the instance
        self.make = make # creates make requirement in car instances
        self.model = model # creates model requirement in car instances
        self.year = year # creates year requirement in car instances
          
    def __str__(self): # special string function to print all the parts of the car instance
        return f"{self.make},{self.model},{year}"
            
    def setmake(self, make): # sets the car make
        self.make = self.make
        
    def getmake(self): # returns the make
        return self.make
    
    def setmodel(self, make): # sets the model
        return self.model
    
    def getmodel(self): # returns the model
        return self.model
    
    def setyear(self, year): # sets the year
        return self.year
    
    def getyear(self): # returns the year
        return self.year
    
c1 = Car("Ford","F-150",2025) # Car instances example

# the next three lines are printing the parts of the c1 instance using the individual parts of the instance
print(c1.make) # prints
print(c1.model)
print(c1.year)

# the remaining three lines call the get function to retrieve the three parts from the instance individually
print(c1.getmake())
print(c1.getmodel())
print(c1.getyear())


# In[ ]:




