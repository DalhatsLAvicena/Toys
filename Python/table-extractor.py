#!/usr/bin/env python
# coding: utf-8

# # Table Extractor
# Extract a table from website and export  it into csv
# Given there is only one table  in the website

# In[34]:


import pandas as pd
import sys

# Turn table into DataFrame function
def extract(link, csv_name):
    url = pd.read_html(link)
    data = url[0]
    csv = data.to_csv(csv_name, index=False)
    return csv

extract(sys.argv[1], sys.argv[2])

