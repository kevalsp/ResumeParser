#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
file = pd.read_csv('/Users/kevalpaida/Moyyn/Languages.csv')
Languages_List = file['Language name ']


# In[16]:


job_titles = open('/Users/kevalpaida/Moyyn/job-titles.txt','r').read().split('\n')

for pos in job_titles:
    if len(pos)<2:
        job_titles.remove(pos)


# In[19]:


technical_skills = open('/Users/kevalpaida/Moyyn/technical_skills_list.txt','r').read().split('\n')


# In[21]:


all_skills = open('/Users/kevalpaida/Moyyn/all_skills.txt','r').read().split('\n')

