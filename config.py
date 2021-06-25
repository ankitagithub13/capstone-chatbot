#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
nltk.download('wordnet')
from nltk.corpus import stopwords
nltk.download('stopwords')
import re


# In[ ]:


class pre_processor:
    stop = []
    lem = []
    stem = []
    
    def __init__(self):
        self.stop = stopwords.words('english')
        self.lem = WordNetLemmatizer().lemmatize
        self.stem_words = PorterStemmer().stem
        
    def apply_lower(self, input_string):
        input_string = input_string.lower()
        return input_string
        
    def remove_spaces(self, input_string):
        input_string=input_string.strip()
        return input_string
        
    
    def remove_special_char(self,input_string):
        sentence = re.sub('[^a-zA-Z\s\d]', '',input_string)
        return sentence
    
    def remove_numbers(self,input_string):
        sentence = re.sub('\d', '',input_string)
        return sentence
    
    def remove_stop_words(self,input_string):
        sentence = ' '.join(word for word in input_string.split() if word not in self.stop)
        return sentence
    
    def lemmatize_the_words(self,input_string):
        sentence = ' '.join(self.lem(word) for word in input_string.split())
        return sentence
    
    def stem_the_words(self, input_string):
        sentence = ' '.join(self.stem_words(word) for word in input_string.split())
        return sentence
    
    def pre_process(self, df, lower_flag=0, remove_spaces_flag=0, remove_special_char_flag=0,  remove_numbers_flag=0,  remove_stop_words_flag=0,  lemmatize_the_words_flag=0, stem_the_words_flag=0):
        if lower_flag==1:
            df = df.apply(self.apply_lower)
        if remove_spaces_flag==1:
            df =df.apply(self.remove_spaces)
        if remove_special_char_flag == 1 :
            df = df.apply(self.remove_special_char)
        if remove_numbers_flag == 1 :
            df =df.apply(self.remove_numbers)
        if remove_stop_words_flag == 1:
            df = df.apply(self.remove_stop_words)
        if lemmatize_the_words_flag ==1:
            df = df.apply(self.lemmatize_the_words)
        if stem_the_words_flag == 1:
            df =df.apply(self.stem_the_words)
            
        return df

