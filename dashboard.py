import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

"""# Menyiapkan Dataset"""

day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

"""Tabel Hari (Day)"""

day_df = pd.read_csv("/content/day.csv")
day_df.head()

"""Tabel Jam (Hour)"""

hr_df = pd.read_csv("/content/hour.csv")
hr_df.head()

"""Assessing Data

# Cek day_df

1. Melihat Day_df
"""

day_df.info()

"""2. Melihat apakah ada duplikasi data"""

print("Jumlah duplikasi data day_df : ", day_df.duplicated().sum())

"""3. Melihat apakah ada missing values"""

day_df.isna().sum()

"""4. Melihat apakah data terdapat keanehan day_df (anomali)"""

day_df.describe()

"""# cek hour_df

1. Melihat hour_df
"""

hour_df.info()

"""2. Melihat apakah terdapat duplikasi data"""

print("Jumlah duplikasi data hour_df : ", hour_df.duplicated().sum())

"""3. Melihat apakah terdapat missing values"""

hour_df.isna().sum()

"""4. Melihat apakah data terdapat keanehan hour_df (anomali)"""

hour_df.describe()

hour_df.info()
day_df.info()

"""Cleaning Data"""

datetime_columns = ["dteday"]

for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])
    hour_df[column] = pd.to_datetime(hour_df[column])
#--> mengubah tipedata dteday dari object ke datetime

day_df.info()

"""## Exploratory Data Analysis (EDA)

Menampilkan Jumlah penyewaan sepeda berdasarkan kondisi cuaca dengan barplot
"""

cuaca_df = day_df.groupby(by="weathersit").cnt.nunique().sort_values(ascending=False).reset_index()
cuaca_df.head()

# Menggabungkan day_df & hour_df
day_hour_df = pd.merge( day_df, hour_df, on='dteday')

# Membuat dataframe baru guna mengetahui rata-rata jam perhari
rata_jam_df = day_hour_df.groupby('dteday')['hr'].mean().reset_index()

rata_jam_df.head()

"""## Visualization & Explanatory Analysis

Berapa Jumlah Penyewa sesuai Cuaca yang terjadi?
"""

sns.barplot(day_df, x="weathersit", y="cnt", color='grey', errorbar=None)

"""Berapakah Jumlah Seluruh Penyewa dalam Beberapa Bulan/Tahun Terakhir?"""

plt.figure(figsize=(12, 5))
plt.plot(day_df["dteday"], day_df["weathersit"], color='blue')
plt.title("Jumlah Sewa beberapa bulan/tahun terakhir", loc="center", fontsize=20)
plt.xlabel('tanggal',size=15)
plt.ylabel('sewa',size=15)
plt.show()

"""Conclusion

1. Jumlah Penyewa Berdasar Cuaca Yang Terjadi
"""

print("Jumlah Penyewa Berdasar Cuaca: ", cuaca_df.iloc[0])

print("Jumlah Penyewa Berdasar Cuaca: ", cuaca_df.iloc[1])

print("Jumlah Penyewa Berdasar Cuaca: ", cuaca_df.iloc[2])

"""2. Jumlah Seluruh Penyewa dalam Beberapa Bulan/Tahun Terakhir"""

print("Jumlah Seluruh penyewa dalam beberapa bulan/tahun terakhir mencapai : ", day_df.cnt.sum())