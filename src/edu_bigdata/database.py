import sqlite3
import pandas as pd

class DataBase:
    def __init__(self, db_name="src/edu_bigdata/static/db/anime_store.sqlite"):
        self.db_name = db_name

    def insert_data(self, df: pd.DataFrame, table_name="anime_data"):
        try:
            conn = sqlite3.connect(self.db_name)
            df.to_sql(name=table_name, con=conn, if_exists='replace', index=False) 
            conn.close()
            print(f"Datos insertados correctamente en la tabla {table_name}")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def read_data(self, table_name="anime_data"):
        try:
            conn = sqlite3.connect(self.db_name)
            df = pd.read_sql(f"SELECT * FROM {table_name}", con=conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error al leer los datos: {e}")
            return pd.DataFrame()
