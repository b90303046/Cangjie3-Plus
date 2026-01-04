#%%
import pandas as pd
import re

cangjie_map = {
    'Q': '手', 'W': '田', 'E': '水', 'R': '口', 'T': '廿', 'Y': '卜', 'U': '山', 'I': '戈', 'O': '人', 'P': '心', 
    'A': '日', 'S': '尸', 'D': '木', 'F': '火', 'G': '土', 'H': '竹', 'J': '十', 'K': '大', 'L': '中', 
    'C': '金', 'V': '女', 'B': '月', 'N': '弓', 'M': '一', 'X': '難'
    }

with open(r'source_txt/cj3.txt','r', encoding='utf-8-sig') as r:
    raw_text_list = r.readlines()

clean_raw_list=[jj.strip().replace('\n','').split() for jj in raw_text_list]


def code_to_radicals(code, m=cangjie_map):
    """
    將倉頡補完的字碼轉為拆字模式
    """
    return ''.join(m.get(c,'') for c in code)

text_df = (pd.DataFrame(data = clean_raw_list, columns=['code', '單字'])
           .assign(code = lambda df: df['code'].str.upper())
           .assign(拆字 = lambda df: df['code'].apply(code_to_radicals))
           #.pipe(lambda df: df.drop_duplicates('中文字', keep='first'))
            .pipe(lambda df: df.drop_duplicates('單字', keep='first'))[['單字','code','拆字']]
            )
            
text_df.to_csv(r'csv/cangjie_drill.csv', index=False, encoding='utf-8-sig')

print('檔案輸出完成...')
# text='影響房價因素眾多利率只是其中之一'
# 