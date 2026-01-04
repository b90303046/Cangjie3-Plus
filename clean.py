#%%
import pandas as pd
import re
with open(r'jsonl/BIAU1.txt','r', encoding='utf-8') as r:
    raw_text_list = r.readlines()


raw_list2 = [jj.replace('║','').strip().split('│') for jj in raw_text_list]

clean_list = []
for kk in raw_list2:
    clean_element = [jj.strip().replace('  ',',') for jj in kk]
    if re.search( r'\d+',clean_element[0]):
        clean_list.append(clean_element)

#%%

text_df = (pd.DataFrame(data = clean_list, columns=['indexx','word','部首','數字','次數','占比']).loc[:,['indexx','word','次數','占比']]
           .assign(indexx= lambda df: pd.to_numeric(df['indexx'], errors='coerce'))
           .assign(次數= lambda df: pd.to_numeric(df['次數'], errors='coerce'))
           .assign(占比= lambda  df: pd.to_numeric(df['占比'], errors='coerce'))
           .sort_values('占比', ascending=True).iloc[0:4000,:]
           .dropna(axis=0, how='all')        
           )

#%%
text_df.iloc[0:3000,1:3].to_csv('word_list.csv', encoding='utf-8-sig')

#.drop('indexx')
