#%%
import numpy as np
import time
import pandas as pd
from colorama import Fore, Back, Style
#%%

def highlight(text, fore=Fore.BLUE, back=Back.WHITE):
    return f"{back}{fore}{text}{Style.RESET_ALL}"

 

word_bank = pd.read_csv(r'csv/cangjie_drill.csv',  index_col=None, encoding='utf-8-sig')

#%%
# --- 遊戲設定 ---
try:
    # 設置每次測試的「連擊長度」   
    trial_info = input(f'請輸入練習次數(num), 與起始位置(0~1000) ,以空隔區分: ').split(' ') 
    if trial_info ==[""]: #不輸入
        trial_info = ["10","0"]
    assert(isinstance(trial_info, list)) 
    trial_count = int(trial_info[0])
    trial_start = int(trial_info[1])
    
except ValueError:
    print("輸入無效，程式結束。")
    exit()


# --- 遊戲邏輯 ---
correct_score = 0
total_trials = 0
start_time = time.time()

print(f'\n--- 倉頡訓練開始！(共 {trial_count} 回合) ---')
print('請將注意力放在手指的「連擊」上。')
wrong_list = []
SHOW_HINT = 1
for i in range(trial_count):
    total_trials += 1
    

    target_word = word_bank.iloc[i+trial_start,0]
    cangjie_dcomp = word_bank.iloc[i+trial_start,2]
    cangjie_map = word_bank.iloc[i+trial_start,3]
 
 
    # # 將字根序列和鍵位序列轉換為易於比較的字串
    # cangjie_str = "".join(cangjie_combo)
    # correct_key_str = "".join(correct_key_combo)

    # # 3. 顯示題目並獲取輸入
    print(f'\n第 {total_trials} 回合, 目標字:')
    print('"'+ highlight(f'{target_word}')+'"')
    #print(f',倉頡字碼為 "{cangjie_dcomp}" ')
    print(f'請輸入以下字根的鍵位連擊:(共10次)')
    count=0
    if SHOW_HINT:
        print(f',倉頡字碼為 "{cangjie_dcomp}", 英文字母{cangjie_map} ')
    
    # # 提示: 如果使用倉頡輸入法，請確保輸入的是英文字母，不是中文。
    user_input = input('請輸入對應的鍵位序列: ').strip().lower()
    # # 4. 判斷對錯
    if user_input == cangjie_map:
    #if user_input == cangjie_map:
        print('✅ 輸入正確！')
        correct_score += 1
    else:
        print(f'❌ 輸入錯誤！')
        print(f'   正確答案是: {cangjie_dcomp}, 代碼 {cangjie_map}')
        wrong_list.append(target_word)

# --- 訓練總結 ---
end_time = time.time()
total_duration = end_time - start_time
accuracy = (correct_score / total_trials) * 100 if total_trials > 0 else 0

print(f'\n--- 訓練總結 ---')
print(f'總共花費時間: {total_duration:.2f} 秒')
print(f'正確連擊次數: {correct_score} / {total_trials}')
print(f'連擊準確率: {accuracy:.2f}%')
print(f'平均每次連擊時間: {(total_duration / total_trials):.2f} 秒')
print(f'--- 訓練結束， 錯誤字為:{','.join(wrong_list)}！ ---')
