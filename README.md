# Tutorial 6 - Change Data Capture (CDC) & Outbox

Repositorio con código base para servicio de aplicación Propiedades de los Alpes

Este repositorio está basado en el repositorio de [(CDC) & Outbox](https://github.com/MISW4406/tutorial-6-cdc) en el tutorial 6 del curso. 

## Estructura del proyecto


- El **src/propiealpes** Cuenta con los diferentes módulos del aplicativo del servicio de propiedades
- **src/propiealpes/modulos** contiene los dos modulos princpales del servicio propiedades (Porpiedad/Usuario)


Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/propiealpes/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/propialpes/api --debug run
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 5000:5000 propialpes/flask
```