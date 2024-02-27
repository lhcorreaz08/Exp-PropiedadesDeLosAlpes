from propialpes.seedwork.aplicacion.comandos import Comando, ComandoHandler    

class AgregarPropiedad(Comando):
    id_propiedad: uuid.UUID

class AgregarPropiedadHandler(ComandoHandler):
    ...