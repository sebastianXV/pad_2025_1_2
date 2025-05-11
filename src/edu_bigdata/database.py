import os
import sqlite3
import pandas as pd

class DataBase:
    def __init__(self, db_path=None):
        try:
            # Crear carpeta "data" si no existe
            os.makedirs("data", exist_ok=True)

            # Ruta segura para el archivo de base de datos
            if db_path is None:
                db_path = os.path.join("data", "anime.db")

            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            print(f"Conectado a la base de datos en: {db_path}")
        except Exception as e:
            print("Error al conectar con la base de datos:", e)

    def insert_data(self, df: pd.DataFrame, table_name: str):
        try:
            df.to_sql(table_name, self.conn, if_exists="replace", index=False)
            print(f"Datos insertados en la tabla: {table_name}")
        except Exception as e:
            print("Error al guardar los datos:", e)

    def read_data(self, table_name: str):
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name}", self.conn)
            return df
        except Exception as e:
            print("Error al leer los datos:", e)
            return pd.DataFrame()
