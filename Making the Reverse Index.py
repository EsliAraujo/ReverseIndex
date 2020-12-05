
# coding: utf-8

# In[61]:

from collections import Counter
import re
import os,sys
import pandas as pd
import numpy as np


# ## Definição de variaveis de ambiente

# In[50]:

user_path = os.environ.get('USERPROFILE')
path_dir = user_path+'\\Documents\\Consultoria\\dataset'
nan_value = float("NaN") 


# ## Geração do dicionário

# In[3]:

df_index = pd.DataFrame([['','']],columns=['doc','word_ids'])
word_dic = pd.read_csv(user_path+'\\Documents\\Consultoria\\word_dic.csv')


# In[4]:

#word_dic = pd.Series(word_dic.c1)
#word_dic = word_dic.to_dict('series')
word_dic = dict(zip(word_dic.c1, word_dic.word_id))
#word_dic


# ## Iniciando Data Frame do Index

# In[250]:

doc_df = pd.DataFrame([['','']],columns=['word_id','doc_num'])

for filename in os.listdir(path_dir):
    #print(filename)    
    filepath = path_dir+'\\'+filename   
    with open(filepath) as fp:
        #Lê texto convertendo em lowercase para facilitar a ordenação
        text = fp.read().lower()
        #quebra o texto em palavras
        words = re.split(r"\W+", text) 
        #cria uma série com as palavras
        word_series = pd.Series(data=words)        
        #faz o de-para com os ID do dicionário gerado no script anterior
        word_series = word_series.map(word_dic.get)
        #remove registros que não estão no dicionario (stop words)
        word_series = word_series.dropna()
        #converte para dataFrame
        word_df = pd.DataFrame(word_series)
        #renomeia coluna
        word_df = word_df.rename(columns={0:'word_id'})
        #remove palavras duplicadas
        word_df = word_df.drop_duplicates(subset=['word_id'])                
        #ordena as palavras pelo id
        word_df = word_df.sort_values(by='word_id')        
        #adiciona coluna doc_num com o nome do arquivo
        word_df['doc_num'] = int(filename)              
        #word_df = word_df.dropna(inplace=True)
        #incrementa o dataFrame de palavras e documentos
        doc_df = doc_df.append(word_df)        
        #break
    #break
#word_df = word_df.drop_duplicates(subset=['doc_num'])
#Converve vazio para NaN
doc_df.replace('', np.nan, inplace=True)
#doc_df['word_id'] = doc_df['word_id'].astype(str).int(doc_df['word_id'])
#Remove NaN
doc_df.dropna(inplace=True)
#Remove decimal
doc_df = doc_df.round(decimals=0).astype('int')
#doc_df = doc_df.word_id.astype('object')
#doc_df.word_id.astype(str).replace('\.0','')
#ordena docNum para Indice
doc_df = doc_df.sort_values(by='doc_num')
#Cria o Indice
doc_df = doc_df.groupby('word_id')['doc_num'].apply(list).reset_index(name='doc_num')
#doc_df
#Gera CSV com o indice
doc_df.to_csv(path_or_buf=user_path+'\\Documents\\Consultoria\\doc_df.csv',
                     index=False, sep=';')


# In[249]:

#doc_df
#word_df
#word_dic
#word_series

