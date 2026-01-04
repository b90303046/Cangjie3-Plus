#%%
import numpy as np
import time
import pandas as pd
from colorama import Fore, Back, Style
import tomllib
from pathlib import Path
import sqlite3
import re
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
squery = r"""SELECT * FROM  real_estate
WHERE FILENAME LIKE "%HH114Q4%"
"""

df = pd.read_sql(squery, conn)

#print(df.info())

def extract_cht(text):
    chars = re.findall(r'[\u4e00-\u9fff]', text)
    result = ''.join(chars)
    return result

text = df.loc[0,'CONTENT'].replace('\n','').replace(' ','').replace('　','')
text_list = [extract_cht(jj) for jj in  re.split('[，。\t]', text)]

#print(text_list)


section_num =5
# %%
text_set = list(text_list[section_num])
text_practice = word_bank.loc[word_bank['單字'].isin(text_set),['單字','拆字1']]

text_dct = dict()
for kk in text_set:
    if kk in text_dct.keys():
        continue
    else:
        test=  text_practice.loc[text_practice['單字']==kk, '拆字1']
        print(test)

#print(text_dct)
        #text_dct[kk] = 