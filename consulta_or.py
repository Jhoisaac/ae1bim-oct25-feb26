from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("CONSULTA CON OR_()")
print("=" * 60)
print("Descripción: Obtener registros que cumplan AL MENOS UNA condición")
print("-" * 60)

# Filtrar instituciones por ciudad (Loja O Quito)
print("\n1. INSTITUCIONES EN LOJA O QUITO:")
print("-" * 60)
instituciones_or = session.query(Institucion).filter(
    or_(
        Institucion.ciudad == "Loja",
        Institucion.ciudad == "Quito"
    )
).order_by(Institucion.nombre).all()
for inst in instituciones_or:
    print(inst)

# Filtrar investigadores por área de investigación
print("\n2. INVESTIGADORES EN IA O MACHINE LEARNING:")
print("-" * 60)
investigadores_or = session.query(Investigador).filter(
    or_(
        Investigador.area_investigacion == "Inteligencia Artificial",
        Investigador.area_investigacion == "Machine Learning"
    )
).order_by(Investigador.apellido).all()
for inv in investigadores_or:
    print(inv)

# Filtrar publicaciones por tipo
print("\n3. PUBLICACIONES TIPO 'TESIS' O 'CONFERENCIA':")
print("-" * 60)
publicaciones_or = session.query(Publicacion).filter(
    or_(
        Publicacion.tipo_publicacion == "Tesis",
        Publicacion.tipo_publicacion == "Conferencia"
    )
).order_by(Publicacion.fecha_publicacion).all()
for pub in publicaciones_or:
    print(pub)

# Filtrar departamentos por código
print("\n4. DEPARTAMENTOS CON CÓDIGO 'DCC-001' O 'DMAT-003':")
print("-" * 60)
departamentos_or = session.query(Departamento).filter(
    or_(
        Departamento.codigo == "DCC-001",
        Departamento.codigo == "DMAT-003"
    )
).all()
for dept in departamentos_or:
    print(dept)

# Filtrar investigadores por apellido
print("\n5. INVESTIGADORES CON APELLIDO 'MENDOZA' O 'GONZÁLEZ':")
print("-" * 60)
investigadores_apellidos = session.query(Investigador).filter(
    or_(
        Investigador.apellido == "Mendoza",
        Investigador.apellido == "González"
    )
).order_by(Investigador.nombre).all()
for inv in investigadores_apellidos:
    print(inv)

# Filtrar publicaciones por investigador (múltiples IDs)
print("\n6. PUBLICACIONES DE INVESTIGADOR 1 O INVESTIGADOR 3:")
print("-" * 60)
publicaciones_investigadores = session.query(Publicacion).filter(
    or_(
        Publicacion.investigador_id == 1,
        Publicacion.investigador_id == 3
    )
).order_by(Publicacion.titulo).all()
for pub in publicaciones_investigadores:
    print(pub)

print("\n" + "=" * 60)
print("RESUMEN:")
print("-" * 60)
print(f"  - Instituciones (Loja o Quito): {len(instituciones_or)}")
print(f"  - Investigadores (IA o ML): {len(investigadores_or)}")
print(f"  - Publicaciones (Tesis o Conf): {len(publicaciones_or)}")
print(f"  - Departamentos (códigos): {len(departamentos_or)}")
print(f"  - Investigadores (apellidos): {len(investigadores_apellidos)}")
print(f"  - Publicaciones (Inv 1 o 3): {len(publicaciones_investigadores)}")
print("=" * 60)

# Cerrar sesión
session.close()
