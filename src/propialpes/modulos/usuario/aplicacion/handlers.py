

from propialpes.modulos.vuelos.dominio.eventos import UsuarioCreada
from propialpes.seedwork.aplicacion.handlers import Handler

class HandlerUsuarioDominio(Handler):

    @staticmethod
    def handle_usuario_creada(evento):
        print('================ USUARIO CREADA ===========')
        

    