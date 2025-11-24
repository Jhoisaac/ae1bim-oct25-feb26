from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

print("Iniciando proceso de población de base de datos...")

# Crear Instituciones
print("\n--- Creando Instituciones ---")
inst1 = Institucion(
    nombre="Universidad Nacional de Loja",
    ciudad="Loja",
    pais="Ecuador"
)

inst2 = Institucion(
    nombre="Escuela Politécnica Nacional",
    ciudad="Quito",
    pais="Ecuador"
)

inst3 = Institucion(
    nombre="Universidad de Cuenca",
    ciudad="Cuenca",
    pais="Ecuador"
)

# Agregar instituciones a la sesión
session.add(inst1)
session.add(inst2)
session.add(inst3)
session.commit()
print("Instituciones creadas exitosamente")

# Crear Departamentos
print("\n--- Creando Departamentos ---")
dept1 = Departamento(
    nombre="Departamento de Ciencias de la Computación",
    codigo="DCC-001",
    institucion_id=inst1.id
)

dept2 = Departamento(
    nombre="Departamento de Ingeniería Eléctrica",
    codigo="DIE-002",
    institucion_id=inst2.id
)

dept3 = Departamento(
    nombre="Departamento de Matemáticas",
    codigo="DMAT-003",
    institucion_id=inst1.id
)

dept4 = Departamento(
    nombre="Departamento de Física",
    codigo="DFIS-004",
    institucion_id=inst3.id
)

# Agregar departamentos a la sesión
session.add(dept1)
session.add(dept2)
session.add(dept3)
session.add(dept4)
session.commit()
print("Departamentos creados exitosamente")

# Crear Investigadores
print("\n--- Creando Investigadores ---")
inv1 = Investigador(
    nombre="Carlos",
    apellido="Mendoza",
    email="carlos.mendoza@unl.edu.ec",
    area_investigacion="Inteligencia Artificial",
    departamento_id=dept1.id
)

inv2 = Investigador(
    nombre="María",
    apellido="González",
    email="maria.gonzalez@epn.edu.ec",
    area_investigacion="Sistemas de Potencia",
    departamento_id=dept2.id
)

inv3 = Investigador(
    nombre="José",
    apellido="Ramírez",
    email="jose.ramirez@unl.edu.ec",
    area_investigacion="Álgebra Abstracta",
    departamento_id=dept3.id
)

inv4 = Investigador(
    nombre="Ana",
    apellido="Torres",
    email="ana.torres@ucuenca.edu.ec",
    area_investigacion="Física Cuántica",
    departamento_id=dept4.id
)

inv5 = Investigador(
    nombre="Pedro",
    apellido="Sánchez",
    email="pedro.sanchez@unl.edu.ec",
    area_investigacion="Machine Learning",
    departamento_id=dept1.id
)

# Agregar investigadores a la sesión
session.add(inv1)
session.add(inv2)
session.add(inv3)
session.add(inv4)
session.add(inv5)
session.commit()
print("Investigadores creados exitosamente")

# Crear Publicaciones
print("\n--- Creando Publicaciones ---")
pub1 = Publicacion(
    titulo="Algoritmos de Deep Learning para Reconocimiento de Imágenes",
    fecha_publicacion="2024-03-15",
    doi="10.1234/dl.2024.001",
    tipo_publicacion="Artículo",
    investigador_id=inv1.id
)

pub2 = Publicacion(
    titulo="Optimización de Redes Eléctricas Inteligentes",
    fecha_publicacion="2024-05-20",
    doi="10.1234/power.2024.002",
    tipo_publicacion="Artículo",
    investigador_id=inv2.id
)

pub3 = Publicacion(
    titulo="Estructuras Algebraicas en Criptografía Moderna",
    fecha_publicacion="2023-11-10",
    doi="10.1234/algebra.2023.003",
    tipo_publicacion="Tesis",
    investigador_id=inv3.id
)

pub4 = Publicacion(
    titulo="Aplicaciones de la Mecánica Cuántica en Computación",
    fecha_publicacion="2024-01-25",
    doi="10.1234/quantum.2024.004",
    tipo_publicacion="Conferencia",
    investigador_id=inv4.id
)

pub5 = Publicacion(
    titulo="Redes Neuronales Convolucionales para Visión por Computadora",
    fecha_publicacion="2024-06-30",
    doi="10.1234/cnn.2024.005",
    tipo_publicacion="Artículo",
    investigador_id=inv1.id
)

pub6 = Publicacion(
    titulo="Transfer Learning en Clasificación de Datos Médicos",
    fecha_publicacion="2024-02-14",
    doi="10.1234/ml.2024.006",
    tipo_publicacion="Artículo",
    investigador_id=inv5.id
)

pub7 = Publicacion(
    titulo="Avances en Teoría de Grupos Finitos",
    fecha_publicacion="2023-09-05",
    doi="10.1234/groups.2023.007",
    tipo_publicacion="Conferencia",
    investigador_id=inv3.id
)

pub8 = Publicacion(
    titulo="Sistemas de Distribución Eléctrica Sostenibles",
    fecha_publicacion="2024-04-18",
    doi="10.1234/sustainable.2024.008",
    tipo_publicacion="Tesis",
    investigador_id=inv2.id
)

# Agregar publicaciones a la sesión
session.add(pub1)
session.add(pub2)
session.add(pub3)
session.add(pub4)
session.add(pub5)
session.add(pub6)
session.add(pub7)
session.add(pub8)
session.commit()
print("Publicaciones creadas exitosamente")

print("\n=== Base de datos poblada exitosamente ===")
print(f"Total Instituciones: {session.query(Institucion).count()}")
print(f"Total Departamentos: {session.query(Departamento).count()}")
print(f"Total Investigadores: {session.query(Investigador).count()}")
print(f"Total Publicaciones: {session.query(Publicacion).count()}")

# Cerrar sesión
session.close()
