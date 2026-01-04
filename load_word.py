#%%
"""
Docstring for load_word
"""
#%%
import sqlite3
from pathlib import Path
import pandas as pd
import json
from tabulate import tabulate
import numpy as np
#%%

df_estate = ( pd.read_csv(r'csv/real_estate.csv', index_col=None,encoding='utf-8-sig'))

df_word =(pd.read_csv(r'csv/word_list.csv', index_col=None)  
             .assign(次數 = lambda df: df['次數'].div(df['次數'].sum()).mul(df_estate['字頻統計'].sum()))
             )


df_merge1 = (pd.merge(left = df_estate, right=df_word, 
                     left_on='index', right_on='word', how='outer')
             .assign(單字 = lambda df: np.where(df['index'].notnull(), df['index'], df['word'] ))
             .assign(字頻 =  lambda df: df['次數'].fillna(0).round(0) + df['字頻統計'].fillna(0).round(0))   
             .sort_values('字頻', ascending=False)[['單字','字頻']]    
                     )


#%%
cangjie_list = []

with open(r'josnl/cangjie.jsonl', 'r', encoding='utf-8-sig') as ff:
    for line in ff:
        files = json.loads(line)
        cangjie_list.append(files)


df_cangjie = pd.DataFrame(cangjie_list, index=None)
# df_cangjie = pd.read_json('cangjie_dct.jsonl', 
#                           lines=True)
#table = tabulate(df_cangjie.tail(20).values, headers= list(df_cangjie.columns), tablefmt='psql')
 
#%%

use_col = ['單字','字頻','拆字1','code1']
df_merge = (pd.merge(left= df_merge1, right=df_cangjie,  
                     on='單字', how='left')[use_col]      
            )

export =1

db_loc = Path(r'F:/FDropbox/Dropbox/Database/cangjie.db')
con = sqlite3.connect(db_loc)
if export:
    #df_merge.to_sql('Dictionary', con, if_exists='replace')
    #print('輸出成功')
    df_merge.to_csv(r'csv/cangjie_drill.csv', index=False, encoding='utf-8-sig')
    print('輸出完成')
