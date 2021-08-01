#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import utils
import spacy
import main
import constants as cs
import json


# In[16]:


class ResumeParser(object):
    def __init__(self, resume):
        nlp = spacy.load('en_core_web_sm')
        
        self.__details = {
            'technical skills'  : None,
            'other skills'      : None,
            'education'         : None,
            'experience'        : None,
            'languages'         : None
        }
        self.__resume      = resume
        self.__text_raw    = main.extract_text(self.__resume, os.path.splitext(self.__resume)[1])
        self.__nlp         = main.process_text(self.__text_raw)
        self.__tech_sk     = utils.technical_skills
        self.__get_basic_details()

    def get_extracted_data(self):
        return self.__details
    
    def __get_basic_details(self):
        
        tech_skills     = main.extract_tech_skills(utils.technical_skills, self.__nlp)
        other_skills    = main.extract_other_skills(utils.all_skills, self.__nlp)
        edu             = main.extraact_education(cs.EDUCATION, self.__nlp)
        experience      = main.extract_all_employment(utils.job_titles, self.__nlp)
        languages       = main.extract_language(utils.Languages_List, self.__nlp)
        
        self.__details['technical skills'] = tech_skills
        self.__details['other skills'] = other_skills
        self.__details['education'] = edu
        self.__details['experience'] = experience
        self.__details['languages'] = languages
        
        return
    


# In[17]:


def resume_result_wrapper(resume):
        parser = ResumeParser(resume)
        return parser.get_extracted_data()


# In[41]:


if __name__ == '__main__':

    resume_path = "/Users/kevalpaida/Moyyn/CVs/AhMa_batch1_anonymized.pdf"

    results = resume_result_wrapper(resume_path)
    
    json_object = json.dumps(results, indent = 3)
    print(json_object)
    
    with open("/Users/kevalpaida/Moyyn/output/sample.json", "w") as outfile: 
        json.dump(results, outfile)

