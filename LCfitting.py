# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np
import matplotlib# グラフをウィンドウ表示しない。GUI表示できないサーバモニタ等で重宝する[1]
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv
import matplotlib.cm as cm
import pandas as pd

##### 生データ
dataset = pd.read_csv('8OBAH140.csv')
xdata = dataset['lambda']
ydata = dataset['Intensity']

##### フィッティングする関数y=f(x)の定義
def func(Io, a, b, c, x):
    return Io*np.sin(51350.488252937*np.pi*(a*x**(-1) + b*x**(-3) + c*x**(-5)))**2

##### 最適化するy=f(x)の係数の初期値
prameter_initial = np.array([46, 0.153, 1060, 0])

##### 最適化の計算[2]
popt, pcov = curve_fit(func, xdata, ydata, p0= prameter_initial)
print ("parameter ->", popt)

##### 最適化後のy=f(x)の関数
#y = func(xdata, popt[0], popt[1], popt[2], popt[3])
y = func(xdata, *popt)

##### 生データと最適化後の関数をグラフにプロット
# 元の生データを点プロット
plt.scatter(xdata, ydata, c='blue', label='raw data')
# 最適化後のフィット関数を線でプロット
plt.plot(xdata, y, 'r-',
         label = 'fit: Io=%2.2E, a=%3.2f, b=%2.2E, c=%2.2E' \
         % tuple(popt))

##### グラフ表示のオプション設定 #####
plt.xlabel('x', fontsize=18)     # x軸の名称とフォントサイズ
plt.ylabel('y', fontsize=18)     # y軸の名称とフォントサイズ
plt.ylim([0,100])            # y軸のレンジの範囲を指定
plt.grid(which="both")           # 表中にグリッド入れる
#plt.rcParams["font.size"]=16    # 全体のフォントを変更
plt.legend(loc='upper right')    # ラベルを右上に記載
plt.tight_layout()               # タイトルを重ねない
plt.show()                       # グラフをプロット
plt.savefig("optimize_fit.png")  # 画像をファイルで保存
