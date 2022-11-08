#kütüphanelerin yüklenmesi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

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
df = pd.read_csv("datasets/PM2.5 Global Air Pollution 2010-2017.csv")
df_copy = df.copy()
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

#todo düzenle
"""
plt.figure(figsize=(12,5))
plt.title("Price Distirbution Graph")
ax = sns.distplot(df["2010"], color = 'y')
"""

# todo: model kurulumu ve test değerlendirmeler
# Todo: veriye göz atma kısmında bazı görselleştirmeler yapılmalı.

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

#standartlaştırma adımlarının yapılması

#standart scaler nesnemizi sklern kütüphanesinden çağırdık
ss = StandardScaler()

df = df.copy()
df.head()

for col in df.columns[2:]:
    df[col] = ss.fit_transform(df[[col]])
df.head()
#böylelikle veriyi standartlaştırmış olduk

#model kurulumu:

#model için gerekli olan sayısal verileri içeren sütunları ayrı bir df olarak belirleuelim

df_last = df.iloc[:,2:]
df_last.head()

#tekrar kopya alalım, isimlendirme kolay olsun diye x yapalım
x = df_last.copy()

#model nesnemizi kuralım, tercihen 4 küme belirledik

kmeans = KMeans(4)

#modelimizi eğitelim

kmeans.fit(x)

#tahmin değerlerini pred değişkeniyle df e ekleyelim
df["pred"] = pred

df.head()

#her bir gruptaki ülke sayısına bakalım
df["pred"].value_counts()

# todo ilişkisel analizler

df["Country Name"]
df[df["pred"]==1]["2010"].mean()
df[df["pred"]==2]["2010"].mean()
df[df["pred"]==3]["2010"].mean()
df[df["pred"]==0]["2010"].mean()

df[df["pred"]==1]["2017"].mean()
df[df["pred"]==2]["2017"].mean()
df[df["pred"]==3]["2017"].mean()
df[df["pred"]==0]["2017"].mean()