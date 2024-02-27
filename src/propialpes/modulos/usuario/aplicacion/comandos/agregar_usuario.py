from propialpes.seedwork.aplicacion.comandos import Comando, ComandoHandler    

class AgregarPropiedadUsuario(Comando):
    id_usuario: uuid.UUID
    id_reserva: uuid.UUID

class AgregarPropiedadUsuarioHandler(ComandoHandler):
    ...