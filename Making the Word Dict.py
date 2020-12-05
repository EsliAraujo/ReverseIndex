
# coding: utf-8

# In[2]:

'''
Author: Esli Marques Florêncio Araújo
Create Date: 25/11/2020
Obejtivo: Criar um dicionário de palavras contidas em documentos
Melhorias Futuras: Tornar incremental, ler apenas palavras de documentos novos no diretorio
                    e incrementar as palavras novas destes documentos no dicionário existente
'''


# In[3]:

from collections import Counter
import re
import os,sys
import pandas as pd


# In[4]:

user_path = os.environ.get('USERPROFILE')
path_dir = user_path+'\\Documents\\Consultoria\\dataset'


# # 1st approach

# In[249]:

#for filename in os.listdir(path_dir):
#    #print(filename)    
#    filepath = path_dir+'\\'+filename
#    #print(filepath)
#    f = open(filepath, 'r')
#    lines = f.read()
#    print(lines[10:100])
    


# # 2nd Approach

# In[5]:

#wordcounts = Counter()
singlewords = pd.DataFrame([''],columns=['c1'])


# In[6]:

#dic_words


# In[6]:

for filename in os.listdir(path_dir):
    #print(filename)    
    filepath = path_dir+'\\'+filename   
    with open(filepath) as fp:
        text = fp.read().lower()
        #print(text[10:100])
        words = re.split(r"\W+", text) 
        #print(type(words))
        df = pd.DataFrame(words, columns=['c1']) 
        singlewords = singlewords.append(df)
        
#         #wordcounts.update(set(words))
#         #print(wordcounts)
#         singlewords = singlewords.append(df, ignore_index=True)


# In[7]:


'''
#Extrair apenas palavras
#Remove caracteres especiais que passaram
#Ordena rows
#Remove rows com menos de 3 letras (stop words)
#Remove duplicados
#Remove nullos
#Ordena rows
#Cria coluna Id
'''
        
#Extrair apenas palavras
singlewords['c1'] = singlewords['c1'].str.extract('([aA-zZ]+)', expand=False)

#singlewords['c1'] = singlewords.c1.replace('[^aA-zZ]', '', regex=True)
#singlewords['c1'] = re.sub(r'[^aA-zZ]','',singlewords['c1'].str)
#singlewords['c1'] = singlewords['c1'].str.replace('_', '')

#Remove caracteres especiais que passaram
singlewords['c1'] = singlewords['c1'].replace(to_replace=r'[_()]', value='', regex=True)
#Ordena rows
singlewords = singlewords.sort_values(by='c1').reset_index(drop=True)
#Remove rows com menos de 3 letras
singlewords['c1'] = singlewords[singlewords['c1'].str.len()>2]
#Remove duplicados
singlewords = singlewords.drop_duplicates(subset=['c1'])
#Remove nullos
singlewords['c1'] = singlewords.dropna()
#Ordena rows
singlewords = singlewords.sort_values(by='c1').reset_index(drop=True)
#Cria coluna Id
singlewords['word_id'] = singlewords.index

#print(singlewords)
singlewords.to_csv(path_or_buf=user_path+'\\Documents\\Consultoria\\word_dic.csv',
                    index=False, sep=';')


# In[ ]:



