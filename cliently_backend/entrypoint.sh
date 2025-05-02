#!/bin/sh

echo "Esperando a que la base de datos esté lista (intento de conexion con migrate)..."

/app/wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Base de datos conectada."

echo "Ejecutando migraciones de base de datos..."

PYTHONPATH=/app python manage.py migrate --noinput

echo "Inicializacion de base de datos finalizada."

echo "Iniciando servidor de aplicacion..."

exec "$@"