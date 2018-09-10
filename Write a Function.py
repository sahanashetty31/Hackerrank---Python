
# coding: utf-8

# In[8]:


def is_leap(year):
    leap = False
    #Writ your Code Here
    if(year % 400 == 0):
        year = True
    elif(year % 4 == 0 and year % 100 != 0):
        year = True
    return leap
year = int(input())
print(is_leap(year))
        

