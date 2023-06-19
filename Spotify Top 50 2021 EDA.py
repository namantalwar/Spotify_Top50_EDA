#!/usr/bin/env python
# coding: utf-8

# <h1 align = 'center'>Spotify Visualization</h1>
# <br>
# <br>
# <h3 align = 'center'>Author - Naman Talwar</h3>
# <br>
# <br>

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


data = pd.read_csv("spotify_top50_2021.csv")
data.head()


# In[3]:


data.shape


# In[4]:


data.info


# In[5]:


data.columns


# In[6]:


data.isnull().sum()


# In[7]:


data.describe()


# In[8]:


data.corr()


# In[9]:


corr = data.corr()
plt.figure(figsize = (15,6))
ax = sns.heatmap(corr,annot = True)


# In[10]:


data.cov()


# In[11]:


spopu = data[['track_name','popularity']].groupby('track_name').sum()
spopu.head()


# In[12]:


from matplotlib import style
style.use('ggplot')


# In[13]:


spopu.plot(kind = 'bar', color = 'red', figsize = (15,6))
plt.title("Song Name vs Popularity",fontsize = 20)
plt.ylabel("Popularity",fontsize = 15)
plt.xlabel("Song Name",fontsize = 15)
plt.show()


# In[14]:


apopu = data[['artist_name','popularity']].groupby("artist_name").sum()
apopu.head()


# In[15]:


apopu.plot(kind = "bar", color = 'blue', figsize = (15,6))
plt.title("Artist vs popularity",fontsize = 20)
plt.xlabel("Artist Name",fontsize = 15)
plt.ylabel("Popularity",fontsize = 15)
plt.show()


# In[16]:


rep = data['artist_name'].value_counts()
rep


# In[17]:


rep.plot(kind = 'bar', color = 'purple', figsize = (15,6))
plt.title("Number of Times an Artist Appears on this Top 50",fontsize = 20)
plt.xlabel("Artist Name", fontsize =15)
plt.ylabel("Number of Songs",fontsize = 15)
plt.show()


# In[18]:


danpopu = data[["popularity",'danceability']].groupby('danceability').sum()
danpopu.head()


# In[19]:


danpopu.plot(kind = 'line', color = 'yellow', figsize = (15,6))
plt.title("Danceability vs Popularity",fontsize = 20)
plt.ylabel("Popularity",fontsize = 15)
plt.xlabel("Danceability",fontsize = 15)
plt.show()


# In[20]:


enpopu = data[["popularity", "energy"]].groupby("energy").sum()
enpopu.head()


# In[21]:


enpopu.plot(kind = 'line', color = 'orange', figsize = (15,6))
plt.title("Energy vs Popularity", fontsize = 20)
plt.xlabel("Energy", fontsize = 15)
plt.ylabel("popularity", fontsize = 15)
plt.show()


# In[22]:


data['loudness'] = abs(data['loudness'])
loudpopu = data[["loudness",'popularity']].groupby("loudness").sum()
loudpopu.head()


# In[23]:


loudpopu.plot(kind = 'line', color = 'green', figsize = (15,6))
plt.title("Loudness vs Popularity", fontsize = 20)
plt.xlabel("Loudness", fontsize = 15)
plt.ylabel("Popularity", fontsize = 15)
plt.show()


# In[24]:


livpopu = data[["liveness",'popularity']].groupby('liveness').sum()
livpopu.head()


# In[25]:


livpopu.plot(kind = 'line', color = 'cornflowerblue', figsize = (15,6))
plt.title("Liveness vs Popularity", fontsize = 20)
plt.xlabel("Liveness",fontsize = 15)
plt.ylabel("Popularity", fontsize = 15)
plt.show()


# In[26]:


tempopu = data[["tempo","popularity"]].groupby("tempo").sum()
tempopu.head()


# In[27]:


tempopu.plot(kind = 'line', color = 'black', figsize = (15,6))
plt.title("Tempo vs Popularity", fontsize = 20)
plt.xlabel("Tempo", fontsize = 15)
plt.ylabel("Popularity",fontsize = 15)
plt.show()


# In[28]:


data["duration_ms"] = data['duration_ms']/60000
durpopu = data[["duration_ms", "popularity"]].groupby('duration_ms').sum()
durpopu.head()


# In[30]:


durpopu.plot(kind = 'line', color = 'brown', figsize = (15,6))
plt.title("Duration vs Popularity", fontsize = 20)
plt.xlabel("Duration (in mins)",fontsize = 15)
plt.ylabel("Popularity",fontsize = 15)
plt.show()


# In[39]:


keys = data["key"].value_counts()
keys


# In[40]:


keys.plot(kind = "bar", color = 'blue', figsize = (15,6))
plt.title("Number of songs in a Key", fontsize = 20)
plt.xlabel("Key",fontsize = 15)
plt.ylabel("Number of Songs",fontsize = 15)
plt.show()

