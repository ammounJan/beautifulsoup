#!/usr/bin/env python
# coding: utf-8

# # beautifulSoup and Request

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[7]:


url = 'https://www.scrapethissite.com/pages/forms/'


# In[9]:


page = requests.get(url)


# In[10]:


page


# In[20]:


Soup = BeautifulSoup(page.text, 'html')


# In[16]:


print(Soup)


# In[18]:


print(Soup.prettify())


# In[21]:


Soup.find('div')


# In[22]:


Soup.find_all('div')


# In[25]:


Soup.find_all('div', class_ = 'col-md-12')


# In[26]:


Soup.find_all('p')


# In[27]:


Soup.find_all('p', class_ = 'lead')


# In[28]:


Soup.find('p', class_ = 'lead').text


# In[29]:


Soup.find_all('th')


# In[30]:


Soup.find_all('td')


# In[34]:


Soup.find('td')


# In[36]:


Soup.find_all('table')


# In[38]:


table = Soup.find_all('table')


# In[39]:


print(table)


# In[41]:


world_titles = Soup.find_all('th')


# In[42]:


world_titles


# In[43]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[44]:


import pandas as pd


# In[45]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[50]:


column_data = Soup.find_all('tr')


# In[51]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[52]:


df


# In[ ]:




