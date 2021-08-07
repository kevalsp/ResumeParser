#!/usr/bin/env python
# coding: utf-8

# In[1]:


import io
import os
import re
import nltk
import constants as cs
import utils
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from nltk.corpus import stopwords
from nltk import word_tokenize
import spacy
nlp = spacy.load('en_core_web_sm')


# In[2]:


def extract_text_from_pdf(pdf_path):
    
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,caching=True,check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle, codec='utf-8', laparams=LAParams())
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
 
            text = fake_file_handle.getvalue()
            yield text
 
            converter.close()
            fake_file_handle.close()
            
def extract_text(file_path, extension):
    text = ''
    if extension == '.pdf':
        for page in extract_text_from_pdf(file_path):
            text += ' ' + page
    else:
        raise ValueError("file is not pdf")
    return text


# In[3]:


def process_text(text):
    nlp_text = text1.split('\n\n')
    nlp_text = [(i.replace('\n','').replace('\x0c','')) for i in nlp_text]
    return nlp_text
    


# In[4]:


def append_value(dict_obj, key, value):
    if key in dict_obj:
        
        if not isinstance(dict_obj[key], list):
            
            dict_obj[key] = [dict_obj[key]]
        
        dict_obj[key].append(value)
    else:
        dict_obj[key] = value


# In[5]:


def extract_language(language_list,nlp_text):
    languages = []
    for i in language_list:
        for tex in nlp_text:
            tex = tex.lower()
            if i.lower().strip() == tex or i.lower() in tex.split() or i.lower() == 'a':
                languages.append(i)
        continue
    return languages


# In[6]:


def extraact_education(degree_list,nlp_text):
    all_education = []
    name = ['college','university','institute',
            'universität', 'hochschule', 'school',
            'technische universität', 'hauptschule',
            'realschule', 'gesamtschule', 'gymnasium',
            'Ecole','schule','school','institut']
    for index, tex in enumerate(nlp_text):

        tex = re.sub(r'[?|$|.|!|,()]', r'', tex)
        tex = tex.upper()
        for i in degree_list:                                     

            if i.upper() in word_tokenize(tex):                   
                prev2 = nlp_text[index-2]
                prev1 = nlp_text[index-1]
                next1 = nlp_text[index+1]
                next2 = nlp_text[index+2]

                for nm in name:
                    if nm.upper() in prev1.upper():
                        uni = prev1
                        educat = (tex+'--'+uni)
                        break

                    elif nm.upper() in prev2.upper():
                        uni = prev2
                        educat = (tex+'--'+uni)
                        break

                    elif nm.upper() in next1.upper():
                        uni = next1
                        educat = (tex+'--'+uni)
                        break

                    elif nm.upper() in next2.upper():
                        uni = next2
                        educat = (tex+'--'+uni)
                        break


                    else:
                        educat = tex

                if educat not in all_education:
                    all_education.append(educat)

    return all_education


# In[7]:


def extract_all_employment(job_title_list,section_text):
    employ = []
    for x,i in enumerate(nlp_text):

        match1 = re.match(r'.*([1-3][0-9]{3})', i)

        if match1:
            jobs = []
            for y,j in enumerate(nlp_text):
                match2 = re.match(r'.*([1-3][0-9]{3})', j)
                if match2 and i != j:
                    duration = i

                    prev2 = nlp_text[x-2]
                    prev1 = nlp_text[x-1]
                    next1 = nlp_text[x+1]
                    next2 = nlp_text[x+2]

                    title = str()
                    for pos in job_title_list: 

                        if pos.lower() in next1.lower():
                            title = next1
                            break

                        elif pos in next2:
                            title = next2
                            break

                        elif pos in prev1:
                            title = prev1
                            break

                        else:
                            title = None
                            continue


                   
                    pl1 = [(i) for i in nlp(next1) if i.ent_type_=="GPE"]
                    pl2 = [(i) for i in nlp(next2) if i.ent_type_=="GPE"]
                    pl3 = [(i) for i in nlp(prev1) if i.ent_type_=="GPE"]
                    pl4 = [(i) for i in nlp(prev2) if i.ent_type_=="GPE"]

                    if pl1:
                        place = next1
                    elif pl2:
                        place = next2
                    elif pl3:
                        place = prev1
                    elif pl4:
                        place = prev2

                    else:
                        place= 'Unknown'

                    try:
                        if 'at' in word_tokenize(title):
                            emp = duration+' -- '+title

                        else:
                            emp = duration+' -- '+title+' at '+place

                        if emp not in employ:
                            employ.append(emp)
                            break

                    except:
                        break

    return employ


# In[8]:


def extract_all_words(nlp_text):
    words = []
    for i in nlp_text:
        for j in word_tokenize(i):
            words.append(j)
    return words
    
    
def extract_other_skills(all_skills,nlp_text):
    words = extract_all_words(nlp_text)
    sk = []
    for i in all_skills:
        for j in words:
            if i.lower() == j.lower():
                if i not in sk:
                    sk.append(i)
    return sk

def extract_tech_skills(tech_skill_list, nlp_text):
    words = extract_all_words(nlp_text)
    skills = []
    for j in tech_skill_list:
        for i in words:
            if j.lower() in i.lower() and j not in skills:
                skills.append(j)
                break
                
    return skills

