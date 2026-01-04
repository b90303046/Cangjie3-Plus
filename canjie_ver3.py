#%%
import numpy as np
import time
import pandas as pd
from colorama import Fore, Back, Style
import tomllib
from pathlib import Path
import sqlite3
import re
from tabulate import tabulate
#%%
"""
給一段文字, 順便提供相對應的字碼來練習
"""
def highlight(text, fore=Fore.BLUE, back=Back.WHITE):
    return f"{back}{fore}{text}{Style.RESET_ALL}"

word_bank = pd.read_csv(r'csv/cangjie_drill.csv',  index_col=None, encoding='utf-8-sig')

with open('config.toml','rb') as rb:
    config = tomllib.load(rb)

db_loc = Path(config['database']['load_loc'])
dbname = config['database']['dbname']
dbpath = db_loc /dbname


#%% 

conn = sqlite3.connect(dbpath)

# 比如找出所有的不動產季報文字來練習
squery = r"""SELECT * FROM  real_estate
WHERE FILENAME LIKE "%HH114Q4%"
"""

df = pd.read_sql(squery, conn)

#print(df.info())

def extract_cht(text):
    """
    找出所有的中文字, 並且合併
    """
    chars = re.findall(r'[\u4e00-\u9fff]', text)
    result = ''.join(chars)
    return result

text = df.loc[0,'CONTENT']
assert isinstance(text,str)
text_new = text.replace('\n','').strip()
text_list = [extract_cht(jj) for jj in  re.split('[，。\t]', text)]
text_list = list(filter(None,text_list))
#print(text_list)



#%% 

def export_table(txt,df):
    df_list =[ df[df['單字'].str.contains(jj, na=False)]  for jj in txt]

    result_df = pd.concat(df_list, axis=0, join='outer')
    table = tabulate(result_df.values, headers=list(result_df.columns), 
                     tablefmt='psql')
    return table



#for jj in 

# text_dct = dict()
# for kk in text_set:
#     if kk in text_dct.keys():
#         continue
#     else:
#         test=  text_practice.loc[text_practice['單字']==kk, '拆字1']
#         print(test)

#print(text_dct)
        #text_dct[kk] = 
# %%
