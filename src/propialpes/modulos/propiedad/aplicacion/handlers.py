

from propialpes.modulos.vuelos.dominio.eventos import PropiedadCreada
from propialpes.seedwork.aplicacion.handlers import Handler

class HandlerPropiedadDominio(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        print('================ PROPIEDAD CREADA ===========')
        

    