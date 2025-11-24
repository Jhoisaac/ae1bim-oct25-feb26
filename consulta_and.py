from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("CONSULTA CON AND_()")
print("=" * 60)
print("Descripción: Obtener registros que cumplan TODAS las condiciones")
print("-" * 60)

# Filtrar instituciones por ciudad Y país
print("\n1. INSTITUCIONES EN LOJA Y DE ECUADOR:")
print("-" * 60)
instituciones_and = session.query(Institucion).filter(
    and_(
        Institucion.ciudad == "Loja",
        Institucion.pais == "Ecuador"
    )
).all()
for inst in instituciones_and:
    print(inst)

# Filtrar investigadores por área Y ordenar
print("\n2. INVESTIGADORES EN IA CON EMAIL DE unl.edu.ec:")
print("-" * 60)
investigadores_and = session.query(Investigador).filter(
    and_(
        Investigador.area_investigacion == "Inteligencia Artificial",
        Investigador.email.like("%unl.edu.ec%")
    )
).order_by(Investigador.apellido).all()
for inv in investigadores_and:
    print(inv)

# Filtrar publicaciones por tipo Y fecha
print("\n3. PUBLICACIONES TIPO 'ARTÍCULO' DEL AÑO 2024:")
print("-" * 60)
publicaciones_and = session.query(Publicacion).filter(
    and_(
        Publicacion.tipo_publicacion == "Artículo",
        Publicacion.fecha_publicacion.like("2024%")
    )
).order_by(Publicacion.fecha_publicacion).all()
for pub in publicaciones_and:
    print(pub)

# Filtrar departamentos por institución específica Y nombre
print("\n4. DEPARTAMENTOS DE INSTITUCIÓN ID=1 CON 'Ciencias' EN EL NOMBRE:")
print("-" * 60)
departamentos_and = session.query(Departamento).filter(
    and_(
        Departamento.institucion_id == 1,
        Departamento.nombre.like("%Ciencias%")
    )
).all()
for dept in departamentos_and:
    print(dept)

# Filtrar investigadores con múltiples condiciones
print("\n5. INVESTIGADORES DE DEPARTAMENTO 1 CON APELLIDO NO NULO:")
print("-" * 60)
investigadores_complejos = session.query(Investigador).filter(
    and_(
        Investigador.departamento_id == 1,
        Investigador.apellido != None
    )
).order_by(Investigador.nombre).all()
for inv in investigadores_complejos:
    print(inv)

print("\n" + "=" * 60)
print("RESUMEN:")
print("-" * 60)
print(f"  - Instituciones (Loja + Ecuador): {len(instituciones_and)}")
print(f"  - Investigadores (IA + unl.edu.ec): {len(investigadores_and)}")
print(f"  - Publicaciones (Artículo + 2024): {len(publicaciones_and)}")
print(f"  - Departamentos (Inst 1 + Ciencias): {len(departamentos_and)}")
print(f"  - Investigadores (Dept 1 + Apellido): {len(investigadores_complejos)}")
print("=" * 60)

# Cerrar sesión
session.close()
