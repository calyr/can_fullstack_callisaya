# Prueba Técnica: Procesamiento de Links con Microservicios



## Puertos
```plaintext
| Servicio  | Puerto |
|-----------|--------|
| frontend  | 9999   |
| hub       | 9010   |
| scraper   | 9020   |
| notifier  | 9030   |
| postgres  | 9040   |
| redis     | 9050   |
```

## Endpoints Principales

**Hub API**
- `POST /register`: Registro de usuarios.
- `POST /upload`: Subida de archivos CSV.
- `GET /files`: Listado de archivos subidos por el usuario.
- `GET /files/{file_id}/links`: Listado de links procesados.

- Opcional: `POST /login`: Inicio de sesión y obtención de JWT.

**Servicio de Scrapeo**
- `POST /process`: Procesar un archivo.

**Servicio de Notificaciones**
- `POST /notify`: Enviar notificación de finalización.

## Caracteristicas de la Solución
- `frontend`: Se levanta en el puerto localhost:9999, tecnologias utilizadas ( react + vite + typescript)
  Pasos para ralizar las pruevas de test

              
- `hub`: Se levanta en el puerto localhost:9010, se utilizo YARP (Reverse Proxy) service para la generación del apigateway
      - Se habilito los CORS para que la web pueda acceder al mismo
      - Se habilito los endpoint hacia el scraper-service
- `scraper`: Se levanta en el puerto localhost:9020, se utilizo FastAPI, se utilizo el patron Repository, se tiene un worker.py que es el encargado de ejecutar la cola para esto se debera ingresar a la consola del servicio scraper-server y ejecutar el siguiente comando: python worker.py

#python worker.py# 


- `notifier`: Se levanta en el puerto localhost:9030, este servicio es consumido desde el procesador de url para la correspondiente notificación, solo se tiene la estructura y se utilizo el patron de compartamiento Strategy.

**Implementaciones pendientes**
- Jaeguer para la trazabilidad de los microservicios
- Prometeus para las metricas de los microservicios
- Sentry para el registro de excepciones
- Keycloak para el manejo de autenticación y autorización
- Configuration Server: Para poder centralizar todos las configuraciones de los microservicios


**Pasos para levantar los microservicios**

1. Ingresar a la carpeta donde esta la solucion del proyecto  : SGCAN-F-1-2025/solution
    docker compose up --build
2. Pasos https://docs.google.com/document/d/1XSPjnBPUzkePb84b9QF8piqsxqhUq6R_2ZUHYOxPGvU/edit?usp=sharing




## Author

- Roberto Carlos Callisaya

