#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
nltk.download('wordnet')
from nltk.corpus import stopwords
nltk.download('stopwords')
import re


# In[7]:


class pre_process_data:
    stop = []
    lem = []
    stem = []
    appos = {"ain't": "am not", "aren't": "are not", "can't": "cannot", 
         "can't've": "cannot have", "'cause": "because", 
         "could've": "could have", "couldn't": "could not", 
         "couldn't've": "could not have", "didn't": "did not", 
         "doesn't": "does not", "don't": "do not", "hadn't": "had not", 
         "hadn't've": "had not have", "hasn't": "has not", 
         "haven't": "have not", "he'd": "he would", "he'd've": "he would have", 
         "he'll": "he will", "he'll've": "he will have", 
         "he's": "he is", "how'd": "how did", 
         "how'd'y": "how do you", "how'll": "how will", "how's": "how is",
         "I'd": "I would", "I'd've": "I would have", "I'll": "I will", 
         "I'll've": "I will have", "I'm": "I am", "I've": "I have", 
         "isn't": "is not", "it'd": "it would", "it'd've": "it would have", 
         "it'll": "it will", "it'll've": "it will have", "it's": "it is", 
         "let's": "let us", "ma'am": "madam", "mayn't": "may not", 
         "might've": "might have", "mightn't": "might not", 
         "mightn't've": "might not have", "must've": "must have", 
         "mustn't": "must not", "mustn't've": "must not have", 
         "needn't": "need not", "needn't've": "need not have",
         "o'clock": "of the clock", "oughtn't": "ought not", 
         "oughtn't've": "ought not have", "shan't": "shall not", 
         "sha'n't": "shall not", "shan't've": "shall not have", 
         "she'd": "she would", "she'd've": "she would have", 
         "she'll": "she will", "she'll've": "she will have",
         "she's": "she is", "should've": "should have", 
         "shouldn't": "should not", "shouldn't've": "should not have", 
         "so've": "so have", "so's": "so is", 
         "that'd": "that had", "that'd've": "that would have", 
         "that's": "that that is", "there'd": "there would", 
         "there'd've": "there would have", "there's": "there is", 
         "they'd": "they would", "they'd've": "they would have", 
         "they'll": "they will", "they'll've": "they will have", 
         "they're": "they are", "they've": "they have", 
         "to've": "to have", "wasn't": "was not", "we'd": "we would", 
         "we'd've": "we would have", "we'll": "we will", 
         "we'll've": "we will have", "we're": "we are", 
         "we've": "we have", "weren't": "were not", 
         "what'll": "what will", "what'll've": "what will have", 
         "what're": "what are", "what's": "what is", 
         "what've": "what have", "when's": "when is", 
         "when've": "when have", "where'd": "where did", 
         "where's": "where is", "where've": "where have", 
         "who'll": "who will", "who'll've": "who will have", 
         "who's": "who is", "who've": "who have", 
         "why's": "why is", "why've": "why have", "will've": "will have", 
         "won't": "will not", "won't've": "will not have",
         "would've": "would have", "wouldn't": "would not", 
         "wouldn't've": "would not have", "y'all": "you all", 
         "y'all'd": "you all would", "y'all'd've": "you all would have", 
         "y'all're": "you all are", "y'all've": "you all have", 
         "you'd": "you would", "you'd've": "you would have",
         "you'll": "you will", "you'll've": "you will have", 
         "you're": "you are", "you've": "you have"}

  
    def __init__(self):
        self.stop = stopwords.words('english')
        self.lem = WordNetLemmatizer().lemmatize
        self.stem_words = PorterStemmer().stem
        
    def apply_lower(self, input_string):
        input_string = input_string.lower()
        return input_string
        
    def remove_spaces(self, input_string):
        input_string=re.sub('[\s]{2,}', ' ',input_string)
        return input_string
        
    def remove_new_line(self, input_string):
        input_string=re.sub('[\n]','', input_string)
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

    
    def remove_single_letter_word(self, input_string):
        input_string=re.sub(' [a-zA-Z] ',' ', input_string)
        return input_string
    
    def remove_two_letter_word(self, input_string):
        input_string=re.sub(' [a-zA-Z][a-zA-Z] ',' ', input_string)
        return input_string
    
        
        # Function to Replace appos
    def replace_appos(self,input_string):
        cleaned_description = []
        for word in str(input_string).split():
            if word.lower() in self.appos.keys():
                cleaned_description.append(self.appos[word.lower()])
            else:
                cleaned_description.append(word)
        return ' '.join(cleaned_description)  
    
    def lemmatize_the_words(self,input_string):
        sentence = ' '.join(self.lem(word) for word in input_string.split())
        return sentence
    
    def stem_the_words(self, input_string):
        sentence = ' '.join(self.stem_words(word) for word in input_string.split())
        return sentence

    
    def pre_process(self, df, 
                    lower_flag=0, 
                    remove_spaces_flag=0, 
                    remove_new_line_flag=0,
                    remove_special_char_flag=0,  
                    remove_numbers_flag=0,  
                    replace_appos_flag=0,
                    remove_stop_words_flag=0,  
                    remove_single_letter_word_flag=0,
                    remove_two_letter_word_flag=0,
                    lemmatize_the_words_flag=0, 
                    stem_the_words_flag=0):
        if lower_flag==1:
            df = df.apply(self.apply_lower)
            
        if remove_spaces_flag==1:
            df =df.apply(self.remove_spaces)
            
        if remove_new_line_flag==1:
            df = df.apply(self.remove_new_line)
            
        if remove_special_char_flag == 1 :
            df = df.apply(self.remove_special_char)

        if remove_numbers_flag == 1 :
            df =df.apply(self.remove_numbers)

        if replace_appos_flag==1:
            df = df.apply(self.replace_appos)
            
        if remove_stop_words_flag == 1:
            df = df.apply(self.remove_stop_words)
            
        if remove_single_letter_word_flag==1:
            df =df.apply(self.remove_single_letter_word)
            
        if remove_two_letter_word_flag==1:
            df = df.apply(self.remove_two_letter_word)
            
        if lemmatize_the_words_flag ==1:
            df = df.apply(self.lemmatize_the_words)
            
        if stem_the_words_flag == 1:
            df =df.apply(self.stem_the_words)
            
        return df


# In[ ]:




