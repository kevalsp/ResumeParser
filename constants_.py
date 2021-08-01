#!/usr/bin/env python
# coding: utf-8

# In[2]:


from nltk.corpus import stopwords

EDUCATION         = [
                    'BE','B.E.', 'B.E', 'BS', 'B.S', 'ME', 'M.E', 'M.E.', 'MS', 'M.S', 'BTECH', 'MTECH', 
                    'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII', 'MASTER DEGREE',  'MSC','M.SC.', 'TECHNICAL STUDIES CERTIFICATE',
                    'BACHELOR DEGREE','BACHELOR', 'MASTER', 'B.ENG', 'PHD', 'PH.D', 'DOCTOR OF PHILOSOPHY','GYMNASIUM'
                    ]

STOPWORDS         = set(stopwords.words('english'))

RESUME_SECTIONS = [
                    'accomplishments',
                    'experience',
                    'employment',
                    'internship experience',
                    'education','academic career',
                    'interests', 'personal interest',
                    'projects',
                    'professional experience',
                    'publications',
                    'skills','personal skills', 'it skills', 'soft skills','organization skills', 'language skills',
                    'languages'
                ]

