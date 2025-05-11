import requests
import pandas as pd

class DataWeb:
    def __init__(self):
        self.base_url = "https://api.jikan.moe/v4/anime"
    
    def get_animes(self, limit=20):
        try:
            response = requests.get(f"{self.base_url}?page=1&limit={limit}")
            if response.status_code == 200:
                data = response.json()
                animes = data['data']
                anime_data = []
                for anime in animes:
                    anime_data.append({
                        'id': anime['mal_id'],
                        'title': anime['title'],
                        'type': anime['type'],
                        'status': anime['status'],
                        'score': anime['score'],
                        'genres': ', '.join([genre['name'] for genre in anime['genres']])
                    })
                return pd.DataFrame(anime_data)
            else:
                print("Error al obtener los datos desde la API")
                return pd.DataFrame()
        except Exception as e:
            print(f"Error al conectar con la API: {e}")
            return pd.DataFrame()
