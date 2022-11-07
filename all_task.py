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

