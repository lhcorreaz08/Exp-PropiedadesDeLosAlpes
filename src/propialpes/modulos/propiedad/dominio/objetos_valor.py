"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from propialpes.seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass

@dataclass(frozen=True)
class Caracterizacion(ObjetoValor):
    multimedia: str
    tipoConstuccion: str
    dimensiones: str
    dimensiones: str
    zonificacion: str

    
@dataclass(frozen=True)
class Geoinformacion(ObjetoValor):
    registroCatastral: str

