from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("CONSULTA CON ORDER_BY()")
print("=" * 60)
print("Descripción: Obtener registros ordenados por atributos específicos")
print("-" * 60)

# Ordenar instituciones por nombre
print("\n1. INSTITUCIONES ORDENADAS POR NOMBRE:")
print("-" * 60)
instituciones_ordenadas = session.query(Institucion).order_by(
    Institucion.nombre
).all()
for inst in instituciones_ordenadas:
    print(inst)

# Ordenar investigadores por apellido
print("\n2. INVESTIGADORES ORDENADOS POR APELLIDO:")
print("-" * 60)
investigadores_ordenados = session.query(Investigador).order_by(
    Investigador.apellido
).all()
for inv in investigadores_ordenados:
    print(inv)

# Ordenar publicaciones por fecha de publicación
print("\n3. PUBLICACIONES ORDENADAS POR FECHA (MÁS RECIENTES PRIMERO):")
print("-" * 60)
publicaciones_ordenadas = session.query(Publicacion).order_by(
    Publicacion.fecha_publicacion.desc()
).all()
for pub in publicaciones_ordenadas:
    print(pub)

# Ordenar departamentos por código
print("\n4. DEPARTAMENTOS ORDENADOS POR CÓDIGO:")
print("-" * 60)
departamentos_ordenados = session.query(Departamento).order_by(
    Departamento.codigo
).all()
for dept in departamentos_ordenados:
    print(dept)

# Ordenar investigadores por área de investigación y luego por apellido
print("\n5. INVESTIGADORES ORDENADOS POR ÁREA Y APELLIDO:")
print("-" * 60)
investigadores_multiple = session.query(Investigador).order_by(
    Investigador.area_investigacion,
    Investigador.apellido
).all()
for inv in investigadores_multiple:
    print(inv)

print("\n" + "=" * 60)
print("NOTA: Los registros se muestran en orden según el criterio especificado")
print("=" * 60)

# Cerrar sesión
session.close()
