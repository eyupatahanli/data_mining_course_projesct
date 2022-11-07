#kütüphanelerin yüklenmesi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#bazı ayarlar (notebookta gerekli olmayabilir)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

#**********  Crispdm ************
"""
1)İşi anlama 
2)Veriyi Anlama 
3)Veriyi Hazırlama
4)Modelleme 
5)Değerlendirme
6)Dağıtım, Konumlandırma

"""

#veriyi okumak
df = pd.read_csv("PM2.5 Global Air Pollution 2010-2017.csv")

#veriye genel bakış
def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)

    print("##################### Types #####################")
    print(dataframe.dtypes)

    print("##################### Head #####################")
    print(dataframe.head(head))

    print("##################### Tail #####################")
    print(dataframe.tail(head))

    print("##################### NA #####################")
    print(dataframe.isnull().sum())

    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)

# Todo veriye göz atma kısmında bazı görselleştirmeler yapılmalı.

"""
verinin boyutuna 
verideki özelliklerin tipine 
ilk beş - son beş veriye baktık 
çeyreklik değerlerine baktık 

"""
#eksik değer analizi
def missing_values_table(dataframe, na_name=False):
    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]
    if na_name:
        return na_columns

missing_values_table(df,True)
#eksik değer olmadığını gördük

#aykırı değer var mı ?
import all_fonk

df.head()
col_name = ["2010","2011","2012","2013","2014","2015","2016","2017"]
all_fonk.outlier_thresholds(df,col_name)

all_fonk.check_outlier(df,col_name)

#aykırı değer olmadığını gördük





