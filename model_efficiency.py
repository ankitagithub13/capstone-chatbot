#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


def fn_confusion_matrix(title, y_test,y_predict):
    cm = metrics.confusion_matrix(y_test,y_predict, labels=[0,1,2,3,4])
    cm_df=pd.DataFrame(cm, index=['I','II', 'III', 'IV','V'], columns=['Predict I','P II', 'P III', 'P IV','P V'])
    plt.figure(figsize=(6,4))
    plt.suptitle(title)
    sns.heatmap(cm_df, annot=True, fmt='1g')


# In[ ]:




