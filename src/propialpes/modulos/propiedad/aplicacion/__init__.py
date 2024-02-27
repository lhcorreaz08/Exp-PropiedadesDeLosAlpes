from pydispatch import dispatcher
from .handlers import HandlerPropiedadDominio

dispatcher.connect(HandlerPropiedadDominio.handle_reserva_creada, signal='PropiedadCreadaDominio')
