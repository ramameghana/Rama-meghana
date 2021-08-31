#!/usr/bin/env python
# coding: utf-8
#mini project on data analytics- using fifa data from https://www.kaggle.com/stefanoleone992/fifa-20-complete-player-dataset/version/1?select=players_20.csv
# In[2]:


import pandas as pd
#for data visualization
from matplotlib import pyplot as plt
import seaborn as sns


# In[3]:


fifa=pd.read_csv(r'C:\Users\ramam\Desktop\players_20.csv')
fifa


# In[4]:


#first 5 rows and all columns
fifa.head()


# In[5]:


fifa.tail()


# In[6]:


fifa.index


# In[11]:


for col in fifa.columns:
    print(col)


# In[12]:


fifa.shape
#18278 players 
#104 features


# In[13]:


fifa['nationality'].value_counts()


# In[14]:


#only top 10 counties
fifa['nationality'].value_counts()[0:10]


# In[24]:


#only names of top 5 countries
#both gives the same result
fifa['nationality'].value_counts()[0:10].index
fifa['nationality'].value_counts()[0:10].keys()


# In[42]:


#plot bar graph
# step-1: set dimensions
plt.figure(figsize=(10,5))
#format(x=country,y=value,color)
plt.bar(list(fifa['nationality'].value_counts()[0:10].keys()),list(fifa['nationality'].value_counts()[0:10]),color=["r","b"])


# In[29]:


player_sal=fifa[['short_name','wage_eur']]
player_sal


# In[30]:


player_sal.head()


# In[33]:


#sorting high salary to low
player_sal=player_sal.sort_values(by=["wage_eur"],ascending=False)
player_sal.head()


# In[41]:


#plot
plt.figure(figsize=(15,10))
plt.bar(list(player_sal["short_name"])[0:10],list(player_sal["wage_eur"])[0:10],color=["blue","green","pink","red"])
plt.show()


# In[43]:


fifa['nationality']=='Germany'


# In[49]:


# data of german players
Germany=fifa[fifa['nationality']=='Germany']
# first 10 germans data
Germany.head(10)


# In[51]:


#tallest german player
Tall=Germany.sort_values(by=["height_cm"],ascending=False)
Tall.head()


# In[53]:


#sort by weight
Germany.sort_values(by=["weight_kg"],ascending=False).head()


# In[56]:


#sort by wage
Germany.sort_values(by=["wage_eur"],ascending=False).head()


# In[59]:


# names,height,age,weight and wages of german players according to highest salary
Germany[['short_name','height_cm','age','weight_kg','wage_eur']].sort_values(by=["wage_eur"],ascending=False).head()


# In[64]:


#shooting skills
shoot=fifa[["short_name","shooting"]]
shoot.head()


# In[66]:


shoot.sort_values(by=["shooting"],ascending=False).head()


# In[67]:


defend=fifa[['short_name','nationality','age','defending']]
defend.head()


# In[79]:


#players who play for madrid
madrid=fifa[fifa['club']=="Real Madrid"]
madrid.head()


# In[80]:


madrid.sort_values(by=["defending"],ascending=False).head()


# In[81]:


madrid['nationality'].value_counts()


# In[82]:


madrid.sort_values(by=["wage_eur"],ascending=False).head()


# In[ ]:




