from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from config.database import Base


auto_modificacion = Table(
    'auto_modificacion',
    Base.metadata,
    Column('auto_id', Integer, ForeignKey('autos.id', ondelete="CASCADE"), primary_key=True),
    Column('modificacion_id', Integer, ForeignKey('modificaciones.id', ondelete="CASCADE"), primary_key=True)
)


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    foto_perfil = Column(String(255), nullable=True)  # Ruta de la imagen

    autos = relationship("Auto", back_populates="dueno", cascade="all, delete-orphan")


class Auto(Base):
    __tablename__ = "autos"
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    anio = Column(Integer, nullable=False)
    foto_auto = Column(String(255), nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)

    dueno = relationship("Usuario", back_populates="autos")
    modificaciones = relationship("Modificacion", secondary=auto_modificacion, back_populates="autos")


class Modificacion(Base):
    __tablename__ = "modificaciones"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)  # Motor, Estética, Suspensión
    foto_mod = Column(String(255), nullable=True)

    autos = relationship("Auto", secondary=auto_modificacion, back_populates="modificaciones")


    #a