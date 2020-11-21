import csv
import pandas as pd

#テーブル作成
table = []

# カラム名
Column = ['会社名', 'ふりがな']

# CSV行列出力
with open('okayama_reclute_list.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]

# l[行番号][列番号]
for i in range(1,50):
    print(l[i][0],l[i][1])
    table.append([l[i][1],l[i][2]])

# データフレームを作成
df = pd.DataFrame(table,columns=Column)

# CSV ファイル出力
df.to_csv(r"okayama_reclute_list2.csv",encoding='utf_8_sig')