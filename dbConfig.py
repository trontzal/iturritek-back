import sqlite3
from flask import g

# En este archivo se conecta la bbdd 

DATABASE_URI = 'bbdd.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        try:
            db = g._database = sqlite3.connect(DATABASE_URI)
            cursor = db.cursor()

            # Crea la tabla si no existe
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS categorias (
                    id_Categoria INTEGER PRIMARY KEY,
                    nombre_Categoria TEXT
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS solicitudes (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    apellidos TEXT,
                    telefono TEXT,
                    email TEXT,
                    servicio_Id INTEGER,
                    mensaje TEXT,
                    FOREIGN KEY (servicio_Id) REFERENCES servicios (id_Servicio)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS servicios (
                    id_Servicio INTEGER PRIMARY KEY,
                    nombre_Servicio TEXT,
                    descripcion_Servicio TEXT,
                    img_Servicio BLOB,
                    categoria_Id INTEGER,
                    FOREIGN KEY (categoria_id) REFERENCES categorias (id_Categoria)
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL
                )
            ''')
            db.commit()
            
            print("Conexión exitosa a la base de datos")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
    return db
