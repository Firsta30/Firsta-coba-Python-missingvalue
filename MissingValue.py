import pandas as pd
import numpy as np
from sklearn import preprocessing

# Membaca data dari file CSV
data_awal = pd.read_csv('shopping_data_missingvalue.csv')

# Menampilkan data awal
print("Data Awal:")
print(data_awal)

# Mengisi missing value dengan nilai rata-rata pada setiap kolom
df_filled = data_awal.fillna(data_awal.mean(numeric_only=True))

# Menampilkan data setelah mengisi missing value
print("\nData Setelah Mengisi Missing Value:")
print(df_filled)
