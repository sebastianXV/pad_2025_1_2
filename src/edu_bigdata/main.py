import pandas as pd
from edu_bigdata.database import DataBase
from edu_bigdata.dataweb import DataWeb

def main():
    # Configurar pandas para mostrar todo
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    # Instanciamos las clases
    db = DataBase()  # Conexión a la base de datos SQLite
    dataweb = DataWeb()  # Conexión a la API Jikan
    
    # Obtener los datos desde la API de Jikan
    anime_data = dataweb.get_animes(limit=20)
    
    if not anime_data.empty:
        # Insertamos los datos en la base de datos
        db.insert_data(anime_data, "anime_data")
    
    # Leer los datos insertados en la base de datos
    print("Datos leídos desde la base de datos:")
    print(db.read_data("anime_data"))

if __name__ == "__main__":
    main()
