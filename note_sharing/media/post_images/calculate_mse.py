import pandas as pd
from sklearn.metrics import mean_squared_error

# Excel dosyasını oku
# Excel dosyasının adını ve yolunu değiştirin
excel_file = "../../roboflow_alku100.xlsx"
df = pd.read_excel(excel_file)

# Tahmin değerleri ile gerçek değerleri al
tahmin_degerleri = df["Ki67 Value"]
gercek_degerler = df["Real Ki67 Value"]

# Ortalama karesel hatayı hesapla
mse = mean_squared_error(gercek_degerler, tahmin_degerleri)

print("Ortalama Karesel Hata:", mse)
