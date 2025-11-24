from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos SQLite
DATABASE_URL = 'sqlite:///bd_estudios.db'

# Crear el engine
engine = create_engine(DATABASE_URL, echo=False)

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Función para obtener una sesión
def get_session():
    """
    Retorna una nueva sesión de base de datos
    """
    return Session()
