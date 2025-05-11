from setuptools import setup, find_packages

setup(
    name="SGDB_Tienda_Anime_Cali",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "sqlite3",  
    ],
)

