#!/usr/bin/env python
# coding: utf-8

# In[1]:


#data visualization
#importing libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[2]:


df=sns.load_dataset('penguins')


# In[3]:


df


# In[4]:


df.species.unique()


# In[5]:


df.species.value_counts()


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


sns.lineplot(x='bill_length_mm',y='bill_depth_mm',data=df,ci=None)
plt.show()


# In[9]:


sns.lineplot(x='bill_length_mm',y='bill_depth_mm',data=df,hue='species',ci=None)


# In[10]:


sns.lineplot(x='body_mass_g',y='species',data=df,hue='species',ci=None)
plt.show()


# In[11]:


sns.lineplot(x='bill_length_mm',y='species',data=df,ci=None,hue='species')
plt.show()


# In[12]:


#scatter plot
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=df,hue='species')
plt.title('Scatter plot')
plt.show()


# In[13]:


sns.barplot(x='bill_length_mm',y='species',data=df)
plt.show()


# In[14]:


sns.barplot(x='species',y='bill_length_mm',data=df)
plt.show()


# In[15]:


df


# In[16]:


sns.boxplot(x='bill_length_mm',data=df)
plt.show()


# In[17]:


sns.boxplot(x='bill_depth_mm',data=df)


# In[18]:


sns.boxplot(x='species',y='bill_depth_mm',data=df)
plt.show()


# In[19]:


sns.violinplot(x='species',y='bill_depth_mm',data=df)


# In[20]:


sns.stripplot(x='species',y='bill_depth_mm',data=df)


# In[21]:


sns.histplot(x='bill_depth_mm',data=df)
plt.show()


# In[22]:


sns.histplot(x='bill_depth_mm',data=df,hue='species',kde=True)


# In[23]:


import warnings
warnings.filterwarnings('ignore')
sns.distplot(df['bill_depth_mm'],color='g')


# In[24]:


sns.pairplot(data=df,hue='species')
plt.show()


# In[25]:


sns.catplot(x='bill_length_mm',data=df,kind='violin')


# In[26]:


sns.catplot(x='species',y='bill_length_mm',data=df,kind='swarm')
plt.show()


# In[27]:


sns.catplot(x='bill_depth_mm',y='species',data=df)
plt.show()


# In[28]:


sns.violinplot(x='species',y='bill_depth_mm',data=df)
plt.show()

sns.stripplot(x='species',y='bill_length_mm',data=df)
plt.show()

sns.catplot(x='bill_length_mm',y='species',data=df)
plt.show()


# In[ ]:




