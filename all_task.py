#kütüphanelerin yüklenmesi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#bazı ayarlar (notebookta gerekli olmayabilir)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

"""
1)İşi anlama 
2)Veriyi Anlama 
3)Veriyi Hazırlama
4)Modelleme 
5)Değerlendirme
6)Dağıtım, Konumlandırma

"""

#veriyi okumak
df = pd.read_csv("datasets/PM2.5 Global Air Pollution 2010-2017.csv")
df2 = pd.read_csv("datasets/death-rates-from-air-pollution.csv")
df3 = pd.read_csv("datasets/death-rates-total-air-pollution.csv")
df4 = pd.read_csv("datasets/number-of-deaths-by-risk-factor.csv")
df5 = pd.read_csv("datasets/share-deaths-air-pollution.csv")


import all_fonk