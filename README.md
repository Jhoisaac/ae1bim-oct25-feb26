# ae1bim-oct25-feb26

## Instrucciones de Uso

### Requisitos Previos

Instalar SQLAlchemy:
```bash
pip install sqlalchemy
```

### Pasos de Ejecución

#### 1. Crear la Base de Datos y las Tablas

```bash
python crear_base_entidades.py
```

El script:
- Crea la base de datos `investigacion.db`
- Define todas las entidades (Institución, Departamento, Investigador, Publicación)
- Establece las relaciones entre entidades
- Crea las tablas en la base de datos

#### 2. Poblar la Base de Datos

```bash
python poblar_base.py
```

Los datos de ejemplo agregados son:
- 3 Instituciones
- 4 Departamentos
- 5 Investigadores
- 8 Publicaciones

#### 3. Ejecutar Consultas

##### Consulta con ALL()
```bash
python consulta_all.py
```
Muestra todos los registros de cada entidad.

##### Consulta con FILTER()
```bash
python consulta_filter.py
```
Filtra registros según condiciones específicas.

##### Consulta con ORDER_BY()
```bash
python consulta_order_by.py
```
Ordena registros según atributos.

##### Consulta con AND_()
```bash
python consulta_and.py
```
Filtra registros que cumplan TODAS las condiciones.

##### Consulta con OR_()
```bash
python consulta_or.py
```
Filtra registros que cumplan AL MENOS UNA condición.

## Ejemplos de Consultas Implementadas

### ALL()
- Obtener todas las instituciones
- Obtener todos los investigadores
- Obtener todas las publicaciones

### FILTER()
- Instituciones por país
- Investigadores por área de investigación
- Publicaciones por tipo

### ORDER_BY()
- Instituciones ordenadas por nombre
- Investigadores ordenados por apellido
- Publicaciones ordenadas por fecha

### AND_()
- Instituciones en ciudad específica Y país específico
- Investigadores en área específica Y con email de dominio específico
- Publicaciones de tipo específico Y del año específico

### OR_()
- Instituciones en ciudad A O ciudad B
- Investigadores en área A O área B
- Publicaciones de tipo A O tipo B
