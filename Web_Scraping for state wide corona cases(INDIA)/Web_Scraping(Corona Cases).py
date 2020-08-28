#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


url = "https://www.ndtv.com/coronavirus/india-covid-19-tracker"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
table = soup.find_all('table')
rows = table[0].find_all('tr')
headings = [i.text.replace('\n','').strip() for i in rows[0]]  # Assigning a variable
all_rows = []
for i in rows:
    td = i.find_all('td')
    row = [i.text for i in td]
    all_rows.append(row)              #get the rows in a list
all_rows.pop(0)   #remove first element
for i in all_rows:
    i[0] = i[0][:i[0].find("DistrictCases")]   #Remove the part of first element after 'DistrictCases'
for i in all_rows:
    i[1] = i[1][:i[1].find(" ")]
    i[2] = i[2][:i[2].find(" ")]
    i[3] = i[3][:i[3].find(" ")]
    i[4] = i[4][:i[4].find(" ")]  #remove inc/dec part after space
df = pd.DataFrame(all_rows,columns=headings) 


df

