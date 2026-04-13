# Administrador de Productos

Aplicación web/API en Python para administrar productos en memoria.

## Características

- Listar productos
- Crear productos
- Consultar producto por ID
- Actualizar producto
- Eliminar producto

## Instalación

1. Crear un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

La API quedará disponible en `http://127.0.0.1:8000`.

## Documentación automática

Una vez en ejecución, puedes ver la documentación interactiva en:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Endpoints principales

- `GET /products`
- `GET /products/{product_id}`
- `POST /products`
- `PUT /products/{product_id}`
- `DELETE /products/{product_id}`
