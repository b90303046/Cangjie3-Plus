import numpy as np
import time

# 倉頡字根對應表 (鍵: QWERTY 鍵位, 值: 倉頡字根)
# 刪除 Z (難) 和 X (重) 以符合基本練習，共 24 個鍵位
cangjie_map = {
    'Q': '手', 'W': '田', 'E': '水', 'R': '口', 'T': '廿', 'Y': '卜', 'U': '山', 'I': '戈', 'O': '人', 'P': '心', 
    'A': '日', 'S': '尸', 'D': '木', 'F': '火', 'G': '土', 'H': '竹', 'J': '十', 'K': '大', 'L': '中', 
    'C': '金', 'V': '女', 'B': '月', 'N': '弓', 'M': '一'
}

# 取得所有 QWERTY 鍵位 (作為隨機抽取的候選集)
all_keys = list(cangjie_map.keys())

# --- 遊戲設定 ---
try:
    # 設置每次測試的「連擊長度」
    COMBO_SIZE = 3 
    
    trial_count = input(f'請輸入練習次數(每次 {COMBO_SIZE} 鍵連擊): ')
    trial_count = int(trial_count)
    
except ValueError:
    print("輸入無效，程式結束。")
    exit()

# --- 遊戲邏輯 ---
correct_score = 0
total_trials = 0
start_time = time.time()

print(f'\n--- 三鍵連擊訓練開始！(共 {trial_count} 回合) ---')
print('請將注意力放在手指的「連擊」上。')

for i in range(trial_count):
    total_trials += 1
    
    # 1. 隨機選取三個 QWERTY 鍵位作為答案序列 (抽出放回)
    #    x 是一個包含三個鍵位字母的 np.array，例如 ['D', 'F', 'C']
    correct_key_combo = np.random.choice(all_keys, size=COMBO_SIZE, replace=True)
    
    # 2. 準備題目：找出對應的倉頡字根序列
    #    '木', '火', '金'
    cangjie_combo = [cangjie_map[key] for key in correct_key_combo]
    
    # 將字根序列和鍵位序列轉換為易於比較的字串
    cangjie_str = "".join(cangjie_combo)
    correct_key_str = "".join(correct_key_combo)

    # 3. 顯示題目並獲取輸入
    print(f'\n第 {total_trials} 回合 (目標鍵: {COMBO_SIZE} 個)')
    print(f'請輸入以下字根的鍵位連擊:')
    print(f'>>> {cangjie_str} <<<')
    
    # 提示: 如果使用倉頡輸入法，請確保輸入的是英文字母，不是中文。
    user_input = input('請輸入對應的鍵位序列: ').strip().upper()

    # 4. 判斷對錯
    if user_input == correct_key_str:
        print('✅ 輸入正確！')
        correct_score += 1
    else:
        print(f'❌ 輸入錯誤！')
        print(f'   正確答案是: {correct_key_str}')

# --- 訓練總結 ---
end_time = time.time()
total_duration = end_time - start_time
accuracy = (correct_score / total_trials) * 100 if total_trials > 0 else 0

print(f'\n--- 訓練總結 ---')
print(f'總共花費時間: {total_duration:.2f} 秒')
print(f'正確連擊次數: {correct_score} / {total_trials}')
print(f'連擊準確率: {accuracy:.2f}%')
print(f'平均每次連擊時間: {(total_duration / total_trials):.2f} 秒')
print('--- 訓練結束，期待您挑戰四鍵連擊！ ---')