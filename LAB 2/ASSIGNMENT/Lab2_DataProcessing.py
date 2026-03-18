#!/usr/bin/env python
# coding: utf-8

# In[ ]:


LAB MANUAL 2
    1. WORKS WITH LIST DICTIONERIES AND TUPLES


# In[1]:


# LIST
numbers = [10, 20, 30, 40]
print("List:", numbers)

# TUPLE
t = (1, 2, 3)
print("Tuple:", t)

# SET
s = {1, 2, 3, 3}
print("Set:", s)

# DICTIONARY
student = {"name": "Ali", "marks": 85}
print("Dictionary:", student)


# In[ ]:


2.FUNCTIONS FOR DATA PROCESSING


# In[2]:


# LIST
numbers = [10, 20, 30, 40]
print("List:", numbers)

# TUPLE
t = (1, 2, 3)
print("Tuple:", t)

# SET
s = {1, 2, 3, 3}
print("Set:", s)

# DICTIONARY
student = {"name": "Ali", "marks": 85}
print("Dictionary:", student)


# In[ ]:


3.CSV FILE CREATED


# In[3]:


import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

print("CSV file created")


# In[4]:


import pandas as pd

data = pd.read_csv("students.csv")
print(data)


# In[5]:


data["Grade"] = ["A", "A+", "B"]

data.to_csv("output.csv", index=False)

print(data)


# In[ ]:


4.READ AND WRITE JSON FILE


# In[6]:


import json

student = {"name": "Ali", "marks": 85}

# Write JSON file
with open("student.json", "w") as file:
    json.dump(student, file)

# Read JSON file
with open("student.json", "r") as file:
    data = json.load(file)
    print(data)


# In[ ]:


5.READ AND WRITE TEXT FILE


# In[7]:


# Write text file
with open("file.txt", "w") as f:
    f.write("Hello Data Analytics")

# Read text file
with open("file.txt", "r") as f:
    print(f.read())


# 6.LIST COMPREHENSION

# In[8]:


numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]

print("Squares:", squares)


# In[ ]:


7. ERROR HANDLING


# In[12]:


try:
    a = int(input("Enter a number: "))
    print(10 / a)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")


# In[ ]:


8.FINAL DATASET PROCESSING


# In[10]:


import pandas as pd

data = pd.read_csv("students.csv")

# Add new column
data["Grade"] = ["A", "A+", "B"]

print(data)


# In[ ]:




