from propialpes.seedwork.aplicacion.comandos import Comando, ComandoHandler

class ActualizarPropiedad(Comando):
    multimedia: str
    tipoConstuccion: str
    dimensiones: str
    dimensiones: str
    zonificacion: str
    registroCatastral: str


class ActualizarPropiedadHandler(ComandoHandler):
    ...