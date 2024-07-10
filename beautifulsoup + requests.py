#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests


# In[35]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[36]:


print(soup)


# In[37]:


soup.find('table')


# In[49]:


table = soup.find_all('table')[1]


# In[50]:


table.find('table', class_ = 'wikitable sortable')


# In[51]:


print(table)


# In[52]:


world_titles = table.find_all('th')


# In[53]:


world_titles


# In[54]:


world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)


# In[55]:


import pandas as pd


# In[65]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[66]:


column_data = table.find_all('tr')


# In[78]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data


# In[79]:


df


# In[83]:


df.to_csv(r'/Users/imenkhemaissia/Downloads/Outputscrap/company.csv', index = False)


# In[ ]:




