from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("CONSULTA CON FILTER()")
print("=" * 60)
print("Descripción: Obtener registros que cumplan condiciones específicas")
print("-" * 60)

# Filtrar instituciones por país
print("\n1. INSTITUCIONES DE ECUADOR:")
print("-" * 60)
instituciones_ecuador = session.query(Institucion).filter(
    Institucion.pais == "Ecuador"
).all()
for inst in instituciones_ecuador:
    print(inst)

# Filtrar investigadores por área de investigación
print("\n2. INVESTIGADORES DEL ÁREA DE INTELIGENCIA ARTIFICIAL:")
print("-" * 60)
investigadores_ia = session.query(Investigador).filter(
    Investigador.area_investigacion == "Inteligencia Artificial"
).all()
for inv in investigadores_ia:
    print(inv)

# Filtrar publicaciones por tipo
print("\n3. PUBLICACIONES DE TIPO 'ARTÍCULO':")
print("-" * 60)
publicaciones_articulo = session.query(Publicacion).filter(
    Publicacion.tipo_publicacion == "Artículo"
).all()
for pub in publicaciones_articulo:
    print(pub)

# Filtrar departamentos por código específico
print("\n4. DEPARTAMENTO CON CÓDIGO 'DCC-001':")
print("-" * 60)
departamento_especifico = session.query(Departamento).filter(
    Departamento.codigo == "DCC-001"
).all()
for dept in departamento_especifico:
    print(dept)

# Filtrar instituciones por ciudad
print("\n5. INSTITUCIONES EN LA CIUDAD DE LOJA:")
print("-" * 60)
instituciones_loja = session.query(Institucion).filter(
    Institucion.ciudad == "Loja"
).all()
for inst in instituciones_loja:
    print(inst)

print("\n" + "=" * 60)
print("RESUMEN DE FILTROS:")
print("-" * 60)
print(f"  - Instituciones de Ecuador: {len(instituciones_ecuador)}")
print(f"  - Investigadores en IA: {len(investigadores_ia)}")
print(f"  - Publicaciones tipo Artículo: {len(publicaciones_articulo)}")
print(f"  - Departamentos con código DCC-001: {len(departamento_especifico)}")
print(f"  - Instituciones en Loja: {len(instituciones_loja)}")
print("=" * 60)

# Cerrar sesión
session.close()
