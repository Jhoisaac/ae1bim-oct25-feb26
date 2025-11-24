from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from configuracion import engine

# Crear la base declarativa
Base = declarative_base()


class Institucion(Base):
    """
    Entidad Institución
    Representa una institución educativa o de investigación
    """
    __tablename__ = 'instituciones'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    pais = Column(String, nullable=False)
    
    # Relación uno a muchos con Departamento
    departamentos = relationship("Departamento", back_populates="institucion")
    
    def __repr__(self):
        return "Institución: id=%d nombre=%s ciudad=%s país=%s" % (
            self.id,
            self.nombre,
            self.ciudad,
            self.pais
        )


class Departamento(Base):
    """
    Entidad Departamento
    Representa un departamento dentro de una institución
    """
    __tablename__ = 'departamentos'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    # Clave foránea hacia Institución
    institucion_id = Column(Integer, ForeignKey('instituciones.id'), nullable=False)
    
    # Relaciones
    institucion = relationship("Institucion", back_populates="departamentos")
    investigadores = relationship("Investigador", back_populates="departamento")
    
    def __repr__(self):
        return "Departamento: id=%d nombre=%s código=%s institución_id=%d" % (
            self.id,
            self.nombre,
            self.codigo,
            self.institucion_id
        )


class Investigador(Base):
    """
    Entidad Investigador
    Representa un investigador asociado a un departamento
    """
    __tablename__ = 'investigadores'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, nullable=False)
    area_investigacion = Column(String, nullable=False)
    # Clave foránea hacia Departamento
    departamento_id = Column(Integer, ForeignKey('departamentos.id'), nullable=False)
    
    # Relaciones
    departamento = relationship("Departamento", back_populates="investigadores")
    publicaciones = relationship("Publicacion", back_populates="investigador")
    
    def __repr__(self):
        return "Investigador: id=%d nombre=%s apellido=%s email=%s área=%s departamento_id=%d" % (
            self.id,
            self.nombre,
            self.apellido,
            self.email,
            self.area_investigacion,
            self.departamento_id
        )


class Publicacion(Base):
    """
    Entidad Publicación
    Representa una publicación científica realizada por un investigador
    """
    __tablename__ = 'publicaciones'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    fecha_publicacion = Column(String, nullable=False)  # Formato 'YYYY-MM-DD'
    doi = Column(String)
    tipo_publicacion = Column(String, nullable=False)  # Artículo, Tesis, Conferencia
    # Clave foránea hacia Investigador
    investigador_id = Column(Integer, ForeignKey('investigadores.id'), nullable=False)
    
    # Relación
    investigador = relationship("Investigador", back_populates="publicaciones")
    
    def __repr__(self):
        return "Publicación: id=%d título=%s fecha=%s tipo=%s investigador_id=%d" % (
            self.id,
            self.titulo,
            self.fecha_publicacion,
            self.tipo_publicacion,
            self.investigador_id
        )


# Crear todas las tablas en la base de datos
Base.metadata.create_all(engine)

print("Base de datos y tablas creadas exitosamente")
