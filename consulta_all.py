from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("CONSULTA CON ALL()")
print("=" * 60)
print("Descripción: Obtener todos los registros de cada entidad")
print("-" * 60)

# Consultar todas las instituciones
print("\n1. TODAS LAS INSTITUCIONES:")
print("-" * 60)
instituciones = session.query(Institucion).all()
for inst in instituciones:
    print(inst)

# Consultar todos los departamentos
print("\n2. TODOS LOS DEPARTAMENTOS:")
print("-" * 60)
departamentos = session.query(Departamento).all()
for dept in departamentos:
    print(dept)

# Consultar todos los investigadores
print("\n3. TODOS LOS INVESTIGADORES:")
print("-" * 60)
investigadores = session.query(Investigador).all()
for inv in investigadores:
    print(inv)

# Consultar todas las publicaciones
print("\n4. TODAS LAS PUBLICACIONES:")
print("-" * 60)
publicaciones = session.query(Publicacion).all()
for pub in publicaciones:
    print(pub)

print("\n" + "=" * 60)
print("RESUMEN:")
print("-" * 60)
print(f"Total de registros encontrados:")
print(f"  - Instituciones: {len(instituciones)}")
print(f"  - Departamentos: {len(departamentos)}")
print(f"  - Investigadores: {len(investigadores)}")
print(f"  - Publicaciones: {len(publicaciones)}")
print("=" * 60)

# Cerrar sesión
session.close()
