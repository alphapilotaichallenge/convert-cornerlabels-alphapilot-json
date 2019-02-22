
# coding: utf-8

# In[154]:


# Import libraries necessary for this project
import numpy as np
import pandas as pd
import json
# Load the dataset
in_file = 'label.txt'
fname = ''
values = []


# In[155]:


def process(line):
    global fname
    global values
    fname = line.split(':')[0]
    fname = fname[:-1]
    values = line.split(':')[1]
    values = values[:-1]
    array = values.split(',')
    array = np.roll(array,-2)
    values = ",".join(map(str, array))


# In[156]:


with open(in_file) as f:
    file = open('labels.json','w') 
    file.write("{") 
    count = 0;
    for line in f:
        process(line)
        if count > 0:
            file.write(",") 
        file.write('"')    
        file.write(fname) 
        file.write('"')             
        file.write(": ")
        file.write("[")           
        file.write("[")
        file.write(values)
        file.write("]")
        file.write("]")           
        count = 1
    file.write("}")     
    file.close()    

