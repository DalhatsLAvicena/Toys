#!/usr/bin/env python
# coding: utf-8

# # Shalat Inspector

# Notebook to evaluate shalat records. This is a template. Please, copy this notebook before any usage

# In[9]:


# Initiation
import pandas as pd


# ## Functions Available

# ### Dataframe Creation Functions

# In[10]:


def month(month_name, df_name):
    """ Create a month dataframe from yearly dataframe
    """
    monthly = df_name[df_name["Month"] == month_name]
    return monthly

# The function somehow results another column at the end
# Remove it with : .iloc[:, :-1]


# In[11]:


def shalat(shalat_name, df_name):
    """ Create a month dataframe from yearly dataframe
    """
    shalat = df_name[df_name["Shalat"] == shalat_name]
    return shalat

# The function somehow results another column at the end
# Remove it with : .iloc[:, :-1]


# ### Summary Functions

# In[12]:


def commitment(shalat_name, shalat_df, value):
    """Returns the sum of shalat Commitment value, where value is either : 
    - Abandoned
    - Committed"""
    name = shalat_df[shalat_df["Shalat"] == shalat_name]
    commitment = (name["Commitment"] == value).sum() 
    return commitment


# In[13]:


def place(shalat_name, shalat_df, value): 
    """Returns the sum of shalat Place value, where value is either : 
    - Home
    - Mosque"""
    name = shalat_df[shalat_df["Shalat"] == shalat_name]
    place = (name["Place"] == value).sum()
    return place


# In[14]:


def person(shalat_name, shalat_df, value): 
    """Returns the sum of shalat Place value, where value is either : 
    - Alone
    - Jamaah"""
    name = shalat_df[shalat_df["Shalat"] == shalat_name]
    person = (name["Person"] == value).sum()
    return person


# In[15]:


def shalat_summary(name, shalat_df):
    """Summarizes records from an individual shalat (eg: Shubuh)
    """
    print("Summary of Shalat", name)
    print("Committed :", commitment(name, shalat_df, "Committed"))
    print("Abandoned :", commitment(name, shalat_df, "Abandoned"))
    print("Mosque :", place(name, shalat_df, "Mosque"))
    print("Home :", place(name, shalat_df, "Home"))
    print("Jamaah :", person(name, shalat_df, "Jamaah"))
    print("Alone :", person(name, shalat_df, "Alone"))


# ## Your Turn

# In[19]:


# load your dataframe here

