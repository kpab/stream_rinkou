import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def LifeGame(data):
# データファイルの入力
    data = []
    # 入力ファイル読み込み
    # with open(data, 'r', encoding='utf-8-sig') as file:
    #     for line in file:
    #         line = line.strip().split(',')
    #         data.append(line)
    for line in data:
        line = line.strip().split(',')
        data.append(line)
    ncol = len(data) # 行数の取得
    nrow = len(data[0]) # 列数の取得

    print(f'data:{data}')
    print(f'{ncol}行{nrow}列のデータ！！')
    field_old = np.zeros((ncol, nrow), dtype=int)
    field_new = np.zeros((ncol, nrow), dtype=int)

    ccol = 0
    for lis in data:
        crow = 0
        for i in lis:
            if i == '●':
                field_old[ccol, crow] = 1
            else:
                field_old[ccol, crow] = 0
            crow += 1
        ccol += 1
    print(field_old)
    # 初期描画
    plt.imshow(field_old)
    
    plt.show()
    # plt.pause(3)

    # 何世代にわたってシミュレートするか
    sim_count = st.input_text('何世代にわたってシミュレートしますか？', type='csv')


st.title('lifegame')
upped_data = st.file_uploader('csvをアップロード')

btn = st.button("go")
if btn:
    data = pd.read_csv(upped_data)
    LifeGame(data)