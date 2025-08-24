import os
import duckdb
from kaggle.api.kaggle_api_extended import KaggleApi

BASE = r"C:\Github\fz-dataworks\data-analysis\classicmodels-proyect"
DB   = os.path.join(BASE, "classicmodels.duckdb")
OUT  = os.path.join(BASE, "classicmodels_join.csv")

print("Autenticando con Kaggle API...")
api = KaggleApi(); api.authenticate()
print("Autenticación lista")
print("Descargando dataset ClassicModels de Kaggle...")
api.dataset_download_files("martatavares/classicmodels", path=BASE, unzip=True)
print("Dataset descargado y descomprimido en", BASE)