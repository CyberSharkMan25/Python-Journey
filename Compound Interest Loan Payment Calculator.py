#!/usr/bin/env python
# coding: utf-8

# In[31]:


def interest_per_month(i,y):
    total_months = y*12
    interest_per_month = i/total_months
    return round(interest_per_month,10)

def total_amount_owed(i,a,y):
    total = a
    years = 0
    for x in range(1,y+1):
        years+=1
        total += total*i
        print(f"The amount owed after year {years} ${round(total,2)}")

years = int(input("How many years long is the loan? "))
loan = float(input("Enter the amount of the loan: "))
interest = float(input("Enter the amount of the loan in decimal form: "))

total_amount_owed(interest,loan,years)

interest_per_month(interest,years)


# In[ ]:




