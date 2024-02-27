"""Entidades del dominio de cliente

En este archivo usted encontrará las entidades del dominio de cliente

"""

from datetime import datetime
from propialpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass, field

from .objetos_valor import Caracterizacion, Geoinformacion

@dataclass
class Propiedad(Entidad):
    Caracterizacion: Caracterizacion = field(default_factory=Caracterizacion)

@dataclass
class Geoinformacion(Usuario):
    Geoinformacion: Geoinformacion = field(default_factory=Geoinformacion)
